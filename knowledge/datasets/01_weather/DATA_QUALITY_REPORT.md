# BuildMind Weather Dataset - Data Quality Report

## Dataset Information
- Location: Siyambalanduwa, Sri Lanka
- Period: September to December 2021
- Sampling interval: 10 minutes
- Original columns: 113
- Total available records: 14,112
- Expected records: 17,568
- Missing records: 3,456
- Overall timestamp coverage: 80.3%

## Monthly Records
| Month | Available | Expected | Missing |
|---|---:|---:|---:|
| September 2021 | 4320 | 4320 | 0 |
| October 2021 | 1008 | 4464 | 3456 |
| November 2021 | 4320 | 4320 | 0 |
| December 2021 | 4464 | 4464 | 0 |

## Confirmed Missing Period
- Start: 2021-10-07 00:00
- End: 2021-10-30 23:50
- Missing readings: 3456
- Gap duration: 24 days

## Validation Results
- Timestamp parsing: Passed
- Duplicate timestamps: 0
- Empty values in 7 selected fields: 0
- Preliminary temperature range check: Passed
- Preliminary humidity range check: Passed
- Preliminary wind speed range check: Passed
- Preliminary rainfall range check: Passed

## Pending Validation
- Solar irradiance range and nighttime readings
- Sensor calibration and measurement units
- Source licensing and redistribution permissions
- Source timezone confirmation

## Important AI Usage Rules
1. Never invent missing sensor readings.
2. Never present estimated values as measured observations.
3. Clearly flag October 7-30, 2021 as missing.
4. Do not generalize this station's data to all Sri Lankan districts.
5. Do not treat preliminary range checks as full sensor validation.

## Status
Partially validated. Not yet production-ready.
