#!/usr/bin/env python3
import json
import datetime

def main():
    data = []
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    for i in range(1, 10001):
        data.append({"id": i, "timestamp": now})
    
    with open("report.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()
