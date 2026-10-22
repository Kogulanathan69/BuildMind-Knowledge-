# BuildMind – Siyambalanduwa Weather Dataset

## Overview
- Location: Siyambalanduwa, Sri Lanka
- Period: September–December 2021
- Sampling interval: 10 minutes
- Available records: 14,112
- Expected records: 17,568
- Timestamp coverage: 80.3%
- Original dataset: 113 columns
- Selected dataset: 7 columns

## Selected Fields
| Field | Unit |
|---|---|
| datetime | Timestamp; timezone unconfirmed |
| temperature_c | Celsius |
| humidity_percent | Percentage |
| wind_speed_ms | m/s |
| wind_direction_deg | Degrees |
| rainfall_mm | mm per recorded interval |
| solar_irradiance_wm2 | W/m² |

## Data Quality
- Selected fields have no empty values.
- Preliminary temperature, humidity, wind speed and rainfall range checks passed.
- All 14,112 solar irradiance readings are numeric.
- Solar minimum: 0.0036 W/m².
- Solar maximum: 1207.9261 W/m².
- No negative solar readings.
- No solar readings above 1500 W/m².
- No duplicate timestamps.
- Missing: October 7–30, 2021 (3,456 readings).

## Limitations
- October missing period must not be filled with invented observations.
- Solar sensor calibration and nighttime readings are not verified.
- Timezone and source redistribution permissions are unconfirmed.
- Represents one location and four months of 2021 only.
- Data is not sufficient for district-wide climate conclusions.
- Clean CSV is structurally verified, not fully quality-certified.

## Files
- DATA_QUALITY_REPORT.md: Quality validation and gaps.
- weather_siyambalanduwa_2021_clean.csv: Local cleaned data; public upload pending permission verification.

## Status
Partially validated – not production-ready.
