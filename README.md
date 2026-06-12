# real-time-streaming-analytics
Real-time data streaming pipeline using Apache Kafka, Python, ClickHouse, Docker, and Grafana for event processing and analytics.

# Real-Time Streaming Analytics Platform

## Overview

Developed a real-time streaming analytics platform using Apache Kafka, Python, ClickHouse, Docker, and Grafana.

The platform generates streaming order events, ingests them through Kafka, processes records in real time, stores analytical data in ClickHouse, and visualizes business metrics through Grafana dashboards.

## Architecture

Python Producer

↓

Apache Kafka

↓

Python Consumer

↓

ClickHouse

↓

Grafana

## Technology Stack

* Apache Kafka
* Python
* ClickHouse
* Docker
* Grafana

## Features

* Real-time event streaming
* Kafka producer and consumer architecture
* ClickHouse analytical storage
* Interactive Grafana dashboards
* Dockerized deployment

## Dashboard Metrics

* Orders Per Minute
* Revenue By Country
* Top Customers

<img width="1825" height="860" alt="Real_time_order_analytics" src="https://github.com/user-attachments/assets/1fd05858-609d-42de-a1dd-5722803ec56e" />


## Sample Event

```json
{
  "order_id": 1,
  "user_id": 25,
  "amount": 1200,
  "country": "India",
  "event_time": "2026-06-10T10:30:00"
}
```
