import json


capitals = {
    "Russia": "Moscow",
    "Japan": "Tokyo",
    "Finland": "Helsinki"
}
filename = "capitals.json"

with open(filename, "w",) as f:
    json.dump(capitals, f)

with open(filename, "r") as f:
    content = json.load(f)
    print content