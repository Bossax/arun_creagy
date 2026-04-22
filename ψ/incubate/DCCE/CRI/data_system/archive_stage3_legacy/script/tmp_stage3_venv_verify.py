from __future__ import annotations

import importlib
import json
import platform
import sys


def main() -> int:
    modules = [
        "numpy",
        "pandas",
        "fiona",
        "geopandas",
        "rasterio",
        "rasterio.mask",
    ]

    result: dict[str, object] = {
        "python_executable": sys.executable,
        "python_version": sys.version,
        "platform": platform.platform(),
        "imports": {},
    }

    imports: dict[str, dict[str, str]] = {}
    for mod in modules:
        try:
            importlib.import_module(mod)
            imports[mod] = {"status": "ok"}
        except Exception as exc:  # noqa: BLE001
            imports[mod] = {
                "status": "fail",
                "error_type": type(exc).__name__,
                "error": str(exc),
            }

    result["imports"] = imports
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

