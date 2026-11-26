# Agresta — Phase 1 System Requirements

**Status:** Proposed design; verify with the course TA and the team before implementation.

## Scope
Agresta is a low-cost IoT monitoring and decision-support system for a shared livestock pen on a small farm. The initial prototype monitors feed stock, water-tank level, water flow, and ambient temperature/humidity. It does not diagnose individual animals or directly measure animal intake.

## Stakeholders and use cases
- **Farm worker:** view current feed, water, temperature and humidity; inspect alerts; record refills.
- **Farm manager:** review trends, configure alert thresholds, and investigate unexpected resource loss.
- **Technician:** calibrate sensors, inspect device errors, and restore operation.

## Functional requirements
| ID | Requirement | Phase 1 evidence | Phase 2 behavior |
|---|---|---|---|
| FR-01 | Acquire timestamped feed weight from load cell + HX711 | Live measurement | Calibrated persistent measurement |
| FR-02 | Acquire distance/estimated tank level from ultrasonic sensor | Live measurement | Calibrated level and volume |
| FR-03 | Acquire water flow rate / accumulated volume from flow sensor | Live pulse-based measurement | Calibrated volume history |
| FR-04 | Acquire temperature and relative humidity from DHT22 | Live measurement | Long-term environment tracking |
| FR-05 | Concurrently acquire/validate multiple sensor streams | Run course threading template and display readings | Recoverable continuous acquisition |
| FR-06 | Display actual sensor values with units and timestamps | Simple live display | Full web dashboard |
| FR-07 | Store readings and events | Design only | SQLite/database implementation |
| FR-08 | Detect abnormal resource-use trends | Plan and example scenarios | Tested anomaly analysis |
| FR-09 | Estimate replenishment needs | Model and data plan | Measured forecasting behavior |
| FR-10 | Generate evidence-based recommendations | DSS decision table/mockups | Implemented decision rules and alerts |
| FR-11 | Support MQTT, HTTP, WebSocket | Protocol architecture only | Demonstrate all three |
| FR-12 | Restart and recover from interruptions | Recovery design | Power-cycle and reconnection tests |

## Non-functional requirements (targets, not measured claims)
- **Safety:** Protect 3.3 V Raspberry Pi GPIO from 5 V signals; isolate liquids and electrical power.
- **Availability:** Continue independent readers if another sensor times out; report stale sensor states.
- **Timeliness:** Target a displayed reading within five seconds of collection where sensor sampling allows.
- **Data quality:** Units, UTC timestamps, sensor source, and quality flags in each reading.
- **Concurrency:** Thread-safe producer-consumer design with bounded queues; follow the TA's exact template.
- **Maintainability:** Separate driver interfaces, shared schema, configuration, and tests.
- **Privacy/security:** Restrict backend/broker access on the local network; no secrets in Git.
- **Cost:** Reuse the existing Raspberry Pi and course kit whenever possible.

## Out of scope for Phase 1
Completed miniature farm enclosure, trained predictive models, production dashboard, complete protocol implementation and automatic boot recovery. These are Phase 2 work, although their design is included in Phase 1.

## Phase 1 acceptance checklist
- [ ] Professor/TA approves idea and integration approach.
- [ ] All selected **physical** sensor modules produce real readings; not only mocks.
- [ ] Concurrent sensor acquisition demonstrated using the course's template.
- [ ] Architecture, requirements, sensor interfaces and IoT platform presented.
- [ ] DSS model inputs, outputs, evidence, data plan, baselines and evaluation explained.
- [ ] Every member can describe the full system and major code paths.
