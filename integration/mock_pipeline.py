"""Laptop-only integration proof for Phase 1; NOT a hardware or rubric substitute."""
from __future__ import annotations
import json
import math
import queue
import threading
import time
from datetime import datetime, timezone

METRICS = {
    'feed_weight_kg': 'kg', 'water_distance_cm': 'cm',
    'water_level_pct': '%', 'water_flow_lpm': 'L/min',
    'water_volume_l': 'L', 'temperature_c': 'degC',
    'humidity_pct': '%',
}


def record(metric: str, value: float, sensor_id: str) -> dict:
    return {
        'schema_version': 1, 'device_id': 'agresta-pi-01',
        'sensor_id': sensor_id,
        'timestamp_utc': datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'),
        'metric': metric, 'value': value, 'unit': METRICS[metric], 'quality': 'ok',
    }


def validate(x: dict) -> bool:
    if x.get('schema_version') != 1 or not x.get('sensor_id') or not x.get('device_id'):
        return False
    metric = x.get('metric')
    if metric not in METRICS or x.get('unit') != METRICS[metric] or x.get('quality') != 'ok':
        return False
    val = x.get('value')
    if isinstance(val, bool) or not isinstance(val, (float, int)) or not math.isfinite(val):
        return False
    if metric in ('humidity_pct', 'water_level_pct') and not 0 <= val <= 100:
        return False
    if metric in ('feed_weight_kg', 'water_distance_cm', 'water_flow_lpm', 'water_volume_l') and val < 0:
        return False
    try:
        dt = datetime.fromisoformat(x['timestamp_utc'].replace('Z', '+00:00'))
        return dt.tzinfo is not None
    except (KeyError, TypeError, ValueError):
        return False


def demo(duration_seconds: float = 3.0) -> list[dict]:
    """Demonstrate independent mock producers and a thread-safe consumer."""
    q: queue.Queue = queue.Queue(maxsize=128)
    stop = threading.Event()
    results: list[dict] = []
    streams = [
        ('feed-hx711-01', [('feed_weight_kg', 2.5)], 0.25),
        ('water-01', [('water_distance_cm', 12.0), ('water_flow_lpm', 1.1)], 0.3),
        ('environment-dht22-01', [('temperature_c', 27.0), ('humidity_pct', 55.0)], 2.0),
    ]

    def producer(sensor_id, metrics, interval):
        while not stop.is_set():
            for metric, value in metrics:
                try:
                    q.put(record(metric, value, sensor_id), timeout=0.2)
                except queue.Full:
                    pass
            stop.wait(interval)

    threads = [threading.Thread(target=producer, args=s, daemon=True) for s in streams]
    for thread in threads:
        thread.start()
    end = time.monotonic() + duration_seconds
    try:
        while time.monotonic() < end:
            try:
                item = q.get(timeout=0.1)
            except queue.Empty:
                continue
            if validate(item):
                results.append(item)
                print(json.dumps(item, ensure_ascii=False))
            q.task_done()
    finally:
        stop.set()
        for thread in threads:
            thread.join(timeout=1)
    return results


if __name__ == '__main__':
    print('MOCK DATA ONLY — not actual sensor readings or the course template.')
    demo()
