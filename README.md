# Agresta

**IoT-Based Livestock Resource Monitoring and Decision Support System**

Agresta is an IoT-based system designed to support resource management in small livestock farms through real-time monitoring, predictive analytics, and actionable recommendations.

The project focuses on three essential aspects of livestock management: feed availability, water resources, and environmental conditions.

By combining physical sensors, concurrent data processing, and a decision-support platform, Agresta aims to help farmers identify unusual resource consumption, anticipate shortages, and make more informed management decisions.

## Problem Statement

Small livestock farms often depend on manual observation to monitor feed supplies, water availability, and environmental conditions.

This can make it difficult to recognize unexpected resource losses, predict replenishment needs, or respond promptly to unfavorable conditions.

Agresta explores how an affordable, integrated monitoring system can improve resource visibility and support timely farm-management decisions.

## Proposed Solution

Agresta consists of three primary monitoring modules and an integrated Decision Support System.

### Smart Feeding

- Measure remaining feed using a load cell.
- Track changes in feed weight.
- Analyze consumption trends.
- Estimate when feed replenishment may be required.

### Smart Water

- Measure water-tank levels.
- Monitor water flow and usage.
- Identify inconsistencies that may indicate unexpected water loss.
- Support early detection of unusual consumption patterns.

### Smart Environment

- Monitor temperature and humidity.
- Track environmental changes.
- Identify potentially unfavorable conditions.
- Generate monitoring alerts.

## Decision Support System

Agresta is designed to go beyond displaying sensor readings by interpreting collected measurements and supporting farm-management decisions.

The proposed Decision Support System focuses on:

- **Resource Forecasting:** Estimating when feed or water may require replenishment.
- **Anomaly Detection:** Identifying unusual consumption and resource-use patterns.
- **Water-Loss Analysis:** Comparing water-level changes with measured flow to identify possible unexplained losses.
- **Environmental Assessment:** Evaluating temperature and humidity conditions.
- **Explainable Recommendations:** Presenting the evidence behind alerts and suggesting appropriate checks or actions.

The system is intended to assist farmers and farm workers rather than replace their judgment.

## Proposed System Architecture

Agresta follows a layered architecture:

1. **Sensing Layer:** Physical sensors collect feed, water, and environmental measurements.
2. **Device Layer:** Raspberry Pi handles sensor acquisition and concurrent processing.
3. **Communication Layer:** MQTT, HTTP, and WebSocket support data exchange.
4. **Data Layer:** Sensor measurements and events are stored for analysis and historical monitoring.
5. **Decision Support Layer:** Forecasting, anomaly detection, and recommendation generation.
6. **Application Layer:** Web-based monitoring and decision-support dashboard.

## Planned Hardware

| Component | Purpose |
|---|---|
| Raspberry Pi | Main controller and processing platform |
| Load Cell + HX711 | Feed-weight measurement |
| Ultrasonic Sensor | Water-level measurement |
| Water Flow Sensor | Water usage monitoring |
| DHT22 | Temperature and humidity monitoring |

## Planned Technology Stack

| Layer | Technologies |
|---|---|
| Programming | Python |
| Hardware Interface | Raspberry Pi GPIO |
| Communication | MQTT, HTTP, WebSocket |
| Backend | Flask |
| Database | SQLite |
| Data Processing | NumPy, pandas |
| Predictive Analytics | scikit-learn |
| Visualization | Web-based dashboard |
| Version Control | Git and GitHub |

The selected components and technologies may be adjusted during implementation and testing.

## Development Roadmap

### Phase 1 — System Design and Sensor Integration

- [ ] Define functional and non-functional requirements.
- [ ] Design the system architecture and sensor interfaces.
- [ ] Connect and calibrate physical sensors.
- [ ] Display real-time sensor measurements.
- [ ] Implement concurrent sensor acquisition.
- [ ] Design the Decision Support System.
- [ ] Prepare the forecasting and anomaly-detection integration plan.
- [ ] Complete the initial system demonstration.

### Phase 2 — Complete System Development

- [ ] Assemble the physical miniature farm prototype.
- [ ] Integrate MQTT, HTTP, and WebSocket.
- [ ] Implement data storage and historical monitoring.
- [ ] Develop the web dashboard.
- [ ] Implement resource forecasting and anomaly detection.
- [ ] Integrate explanations and recommendations.
- [ ] Implement automatic startup and recovery.
- [ ] Evaluate the system through controlled experiments.

## Experimental Evaluation

Agresta will investigate whether combining multiple sensor readings and predictive analysis can improve resource monitoring compared with basic threshold-based alerts.

Planned evaluation areas include:

- Feed and water measurement accuracy.
- Forecasting errors.
- Anomaly detection performance.
- False-alert rates.
- Event detection latency.
- Communication reliability and automatic recovery.

## Physical Prototype

A miniature livestock feeding and watering station will be used to demonstrate Agresta.

The prototype will simulate resource consumption, refilling, water loss, and environmental changes using physical sensors.
