param (
    $BaseDir = "C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\incubate\DCCE\CRI\data_system",
    $BronzeDir = "data\0_bronze\dopa",
    $GoldDir = "data\2_gold",
    $VillageFile = "code_village_dopa_2019.xls",
    $OutputFile = "dim_location_master.csv"
)

Add-Type -AssemblyName System.IO.Compression.FileSystem

function Get-XlsxSheetData($path) {
    $zip = [System.IO.Compression.ZipFile]::OpenRead($path)
    
    # 1. Get shared strings
    $ssEntry = $zip.GetEntry("xl/sharedStrings.xml")
    $sharedStrings = @()
    if ($ssEntry) {
        $stream = $ssEntry.Open()
        $reader = New-Object System.IO.StreamReader($stream)
        [xml]$ssXml = $reader.ReadToEnd()
        $reader.Close()
        $stream.Close()
        
        $ns = New-Object Xml.XmlNamespaceManager $ssXml.NameTable
        $ns.AddNamespace("main", "http://schemas.openxmlformats.org/spreadsheetml/2006/main")
        
        foreach ($si in $ssXml.SelectNodes("//main:si", $ns)) {
            $t = $si.SelectSingleNode("main:t", $ns)
            if ($t) {
                $sharedStrings += $t.InnerText
            } else {
                $parts = $si.SelectNodes("main:r/main:t", $ns)
                $text = ""
                foreach ($p in $parts) { $text += $p.InnerText }
                $sharedStrings += $text
            }
        }
    }

    # 2. Get sheet data
    $sheetEntry = $zip.GetEntry("xl/worksheets/sheet1.xml")
    $rows = @()
    if ($sheetEntry) {
        $stream = $sheetEntry.Open()
        $reader = New-Object System.IO.StreamReader($stream)
        [xml]$sheetXml = $reader.ReadToEnd()
        $reader.Close()
        $stream.Close()
        
        $ns = New-Object Xml.XmlNamespaceManager $sheetXml.NameTable
        $ns.AddNamespace("main", "http://schemas.openxmlformats.org/spreadsheetml/2006/main")
        
        foreach ($rowNode in $sheetXml.SelectNodes("//main:row", $ns)) {
            $rowObj = New-Object PSObject
            foreach ($cell in $rowNode.SelectNodes("main:c", $ns)) {
                $ref = $cell.getAttribute("r")
                $col = $ref -replace '\d+', ''
                $valNode = $cell.SelectSingleNode("main:v", $ns)
                if ($valNode) {
                    $val = $valNode.InnerText
                    if ($cell.getAttribute("t") -eq "s") {
                        $val = $sharedStrings[[int]$val]
                    }
                    $rowObj | Add-Member -MemberType NoteProperty -Name $col -Value $val -ErrorAction SilentlyContinue
                }
            }
            $rows += $rowObj
        }
    }
    
    $zip.Dispose()
    return $rows
}

$villagePath = Join-Path $BaseDir (Join-Path $BronzeDir $VillageFile)
$outputPath = Join-Path $BaseDir (Join-Path $GoldDir $OutputFile)

Write-Host "Parsing $villagePath..."
$data = Get-XlsxSheetData $villagePath

Write-Host "Processing $($data.Count) records..."

# Mapping: A: VILL_NO, B: VILL_CODE, C: TAM_CODE, D: AMP_CODE, E: PROV_CODE, F: TAM_T, G: AMP_T, H: PROV_T, I: VILL_T
$canonical = foreach ($r in $data | Select-Object -Skip 1) {
    [PSCustomObject]@{
        location_id = $r.B
        province_code = $r.E
        province_name_th = if ($r.H) { $r.H -replace '^จ\.', '' } else { "" }
        district_code = $r.D
        district_name_th = if ($r.G) { $r.G -replace '^อ\.', '' } else { "" }
        subdistrict_code = $r.C
        subdistrict_name_th = if ($r.F) { $r.F -replace '^ต\.', '' } else { "" }
        village_code = $r.B
        village_name_th = $r.I
        source = "DOPA_2019"
    }
}

$canonical | Export-Csv -Path $outputPath -NoTypeInformation -Encoding UTF8
Write-Host "Successfully created $outputPath"
