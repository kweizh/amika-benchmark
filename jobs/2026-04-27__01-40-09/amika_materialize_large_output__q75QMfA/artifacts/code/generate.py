#!/usr/bin/env python3
import json
import datetime

data = []
for i in range(1, 10001):
    data.append({
        "id": i,
        "timestamp": datetime.datetime.now().isoformat()
    })

with open("report.json", "w") as f:
    json.dump(data, f)
