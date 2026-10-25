$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
Get-ChildItem -LiteralPath (Join-Path $root 'datasets') -Recurse -File |
    Where-Object { $_.Extension -in '.xlsx', '.csv', '.json', '.md' } |
    Select-Object FullName, Length,
        @{Name='Status';Expression={'Review source/licence/version before public publishing'}} |
    Export-Csv -LiteralPath (Join-Path $root 'Git_Candidates.csv') -NoTypeInformation -Encoding UTF8
Write-Host 'Created Git_Candidates.csv. No files copied, staged, committed or pushed.'
