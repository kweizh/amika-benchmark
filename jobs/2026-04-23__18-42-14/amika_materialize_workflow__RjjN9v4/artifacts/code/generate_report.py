import json

data = {"status": "success", "data": "materialized"}
with open("report.json", "w") as f:
    json.dump(data, f)
