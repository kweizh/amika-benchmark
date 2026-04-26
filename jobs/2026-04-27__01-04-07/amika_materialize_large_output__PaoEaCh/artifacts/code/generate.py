#!/usr/bin/env python3
import json
from datetime import datetime, timezone

def generate_report():
    report = []
    for i in range(1, 10001):
        report.append({
            "id": i,
            "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        })
    
    with open("report.json", "w") as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    generate_report()
