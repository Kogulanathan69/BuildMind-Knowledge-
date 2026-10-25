$ErrorActionPreference = 'Stop'
$manifest = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'FILE_MANIFEST.json') -Raw | ConvertFrom-Json
$failed = 0
foreach ($entry in $manifest) {
    $path = Join-Path $PSScriptRoot $entry.path
    if (!(Test-Path -LiteralPath $path -PathType Leaf)) { Write-Host "MISSING $($entry.path)"; $failed++; continue }
    $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $entry.sha256) { Write-Host "MISMATCH $($entry.path)"; $failed++ }
}
if ($failed -gt 0) { Write-Host "$failed missing or mismatched files. Extract both packages before checking full recovery."; exit 1 }
Write-Host 'All manifest file hashes match.'
