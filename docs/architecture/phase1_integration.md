# Phase 1 Integration Checklist and Demonstration

## Priorities from the CSCI410 rubric
- **30%:** all chosen sensors display actual readings.
- **30%:** multithreading follows the supplied course template.
- **20%:** architecture, functional/non-functional requirements, use cases, sensor interfaces and platform.
- **20%:** clear AI/DSS integration plan, data, models, metrics and value.

## Member 1 tasks before hardware arrives
1. Review `requirements.md`, `architecture.md` and `sensor_contract.md` with Members 2–5.
2. Agree metric names, units, pin ownership and error semantics.
3. Run laptop-only mock demonstration and tests.
4. Document use cases, architecture and test acceptance criteria.
5. Prepare a short integration checklist and meeting notes.

## Once hardware is available
1. Confirm common ground, Pi voltage safety, correct pinout and appropriate sensor power.
2. Individually verify and calibrate feeding, water and environment readings.
3. Swap mock drivers for real drivers **without changing the shared contract**.
4. Run all readers concurrently via the course's exact required template.
5. Verify live display of each sensor; simulate one sensor failure and show graceful handling.
6. Capture screenshots, recorded outputs and a short backup video.

## Demonstration script
- Present architecture and the physical sensors.
- Place a known weight on the load cell; observe changed value.
- Change ultrasonic target distance; show changed distance/level.
- Safely pass water through flow sensor; show pulses/flow.
- Show DHT22 temperature/humidity.
- Explain threads, queue/locks and error handling in code.
- Present DSS *plan*: water-balance consistency, resource forecast, anomaly detection and recommendations.

## Risks to escalate
- **Missing sensor/module:** contact TA immediately; course minimum is three sensors but our proposed scope is four modules.
- **No usable water flow:** test sensor range and hydraulic setup; don't treat zero as a valid calibrated flow automatically.
- **No threading template:** obtain the exact required template before claiming full compliance.
- **Time pressure:** prioritize real readings and threading over polished frontend.

## Completion evidence for Member 1
- Requirements, architecture, data contract, test checklist reviewed by team.
- Passing mock integration tests, with clear "mock only" label.
- Actual integration demonstrated by the team on Pi and recorded.
- All members understand how their modules exchange measurements.
