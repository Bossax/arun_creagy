from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

import geopandas as gpd
import rasterio
from rasterio.features import geometry_window
from rasterio.mask import mask


@dataclass
class ProvinceFailure:
    province_code: str
    province_name_th: str
    error_type: str
    error_message: str
    geom_is_valid: bool
    geom_is_empty: bool
    geom_area_deg2: float
    geom_bounds: tuple[float, float, float, float]
    raster_window_col_off: int | None
    raster_window_row_off: int | None
    raster_window_width: int | None
    raster_window_height: int | None
    window_read_ok: bool
    window_read_error_type: str | None
    window_read_error_message: str | None


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> int:
    script_path = Path(__file__).resolve()
    base_dir = script_path.parent.parent

    raster_path = base_dir / "data/0_bronze/worldpop/tha_ppp_2020.tif"
    gpkg_path = base_dir / "data/1_silver/dopa/stage3_dopa_province_geometry_enriched.gpkg"
    out_json = base_dir / "artifacts/reports/stage3_worldpop_raster_diagnose.json"

    gdf = gpd.read_file(gpkg_path.as_posix(), layer="province_enriched")

    with rasterio.open(raster_path.as_posix()) as src:
        if gdf.crs is None:
            raise RuntimeError("Province CRS is missing")
        if src.crs is None:
            raise RuntimeError("Raster CRS is missing")

        gdf = gdf.to_crs(src.crs)
        gdf["province_code"] = gdf["province_code"].astype(str).str.zfill(2)
        gdf = gdf[gdf["match_status"].astype(str).str.lower() == "matched"].copy()

        failures: list[ProvinceFailure] = []
        successes = 0

        for rec in gdf[["province_code", "province_name_th", "geometry"]].itertuples(index=False):
            geom = rec.geometry
            code = str(rec.province_code).zfill(2)
            name = str(rec.province_name_th)

            try:
                _masked, _ = mask(src, [geom], crop=True, nodata=src.nodata, filled=False)
                successes += 1
                continue
            except Exception as exc:  # noqa: BLE001
                mask_error_type = type(exc).__name__
                mask_error_message = str(exc)

            window_col_off = None
            window_row_off = None
            window_width = None
            window_height = None
            window_read_ok = False
            window_read_error_type = None
            window_read_error_message = None

            try:
                win = geometry_window(src, [geom], pad_x=0, pad_y=0)
                window_col_off = int(win.col_off)
                window_row_off = int(win.row_off)
                window_width = int(win.width)
                window_height = int(win.height)
                _ = src.read(1, window=win, masked=True)
                window_read_ok = True
            except Exception as win_exc:  # noqa: BLE001
                window_read_error_type = type(win_exc).__name__
                window_read_error_message = str(win_exc)

            failures.append(
                ProvinceFailure(
                    province_code=code,
                    province_name_th=name,
                    error_type=mask_error_type,
                    error_message=mask_error_message,
                    geom_is_valid=bool(geom.is_valid),
                    geom_is_empty=bool(geom.is_empty),
                    geom_area_deg2=float(geom.area),
                    geom_bounds=tuple(float(x) for x in geom.bounds),
                    raster_window_col_off=window_col_off,
                    raster_window_row_off=window_row_off,
                    raster_window_width=window_width,
                    raster_window_height=window_height,
                    window_read_ok=window_read_ok,
                    window_read_error_type=window_read_error_type,
                    window_read_error_message=window_read_error_message,
                )
            )

        block_failures = []
        for _, win in src.block_windows(1):
            try:
                _ = src.read(1, window=win, masked=True)
            except Exception as block_exc:  # noqa: BLE001
                block_failures.append(
                    {
                        "col_off": int(win.col_off),
                        "row_off": int(win.row_off),
                        "width": int(win.width),
                        "height": int(win.height),
                        "error_type": type(block_exc).__name__,
                        "error_message": str(block_exc),
                    }
                )

        output = {
            "generated_utc": utc_now_iso(),
            "inputs": {
                "raster": raster_path.as_posix(),
                "province_enriched_geometry": gpkg_path.as_posix(),
            },
            "raster_meta": {
                "driver": src.driver,
                "width": src.width,
                "height": src.height,
                "count": src.count,
                "dtype": str(src.dtypes[0]),
                "crs": str(src.crs),
                "nodata": None if src.nodata is None else float(src.nodata),
                "bounds": {
                    "left": float(src.bounds.left),
                    "bottom": float(src.bounds.bottom),
                    "right": float(src.bounds.right),
                    "top": float(src.bounds.top),
                },
                "block_shapes": [list(shape) for shape in src.block_shapes],
            },
            "province_count": int(len(gdf)),
            "mask_success_count": int(successes),
            "mask_failure_count": int(len(failures)),
            "mask_failures": [asdict(f) for f in failures],
            "raster_block_failure_count": int(len(block_failures)),
            "raster_block_failures": block_failures,
        }

    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"diagnostic_json": out_json.as_posix(), "mask_failure_count": output["mask_failure_count"], "raster_block_failure_count": output["raster_block_failure_count"]}, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

