# Shared Sensor Data Contract (v1)

**Agreement required:** Members 1–5 should approve this before developing drivers.

We use **one JSON object per observation**. It lets sensors report independently and avoids waiting for slower readers such as DHT22.

```json
{
  "schema_version": 1,
  "device_id": "agresta-pi-01",
  "sensor_id": "feed-hx711-01",
  "timestamp_utc": "2026-11-26T08:30:00Z",
  "metric": "feed_weight_kg",
  "value": 2.45,
  "unit": "kg",
  "quality": "ok"
}
```

## Allowed metrics and units
| Metric | Unit | Source | Notes |
|---|---|---|---|
| `feed_weight_kg` | `kg` | Load cell/HX711 | After calibration; negative readings invalid |
| `water_distance_cm` | `cm` | Ultrasonic | Direct observed distance |
| `water_level_pct` | `%` | Ultrasonic + tank geometry | Calculated, not a direct measurement |
| `water_flow_lpm` | `L/min` | Flow sensor | Requires pulse calibration and adequate flow |
| `water_volume_l` | `L` | Flow sensor | Cumulative water passed; define reset behavior |
| `temperature_c` | `degC` | DHT22 | Respect sensor sample interval |
| `humidity_pct` | `%` | DHT22 | Physical range 0–100 |

## Validation rules
- `schema_version` must be 1; `device_id`, `sensor_id` are nonempty.
- `timestamp_utc` must be valid ISO 8601 with UTC offset (`Z` preferred).
- `metric` must appear in the table, and `unit` must match the table exactly.
- `value` must be finite numeric (not NaN or infinity), or `null` when `quality` is `error` or `stale`.
- `quality` is `ok`, `error`, `stale`, or `uncalibrated`.
- Humidity and percentages are 0–100; measurements otherwise obey physical and sensor-specific limits.
- Recorded timestamps are **observation times**, not forecast times.

## Reader interface
A sensor driver exposes `read() -> list[dict]` for a single collection cycle; it must return records matching this contract or clearly report an error. Integration code must not import Raspberry Pi GPIO modules when running on a laptop in mock mode.

## Sensor sampling guidance
The system should support independent sampling rates. DHT22 should not be sampled excessively (typically about once every two seconds), while flow pulses should be counted with appropriate precision. Final schedules depend on drivers and course template.

## Handoffs
- Member 2: `feed_weight_kg`.
- Member 3: `water_distance_cm`, optional calculated `water_level_pct`, `water_flow_lpm`, `water_volume_l`.
- Member 4: `temperature_c`, `humidity_pct`.
- Member 5: consume validated history to define predictions and recommendation inputs.
