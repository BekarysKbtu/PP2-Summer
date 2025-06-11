import json

with open("/Users/bekaryssherman/Desktop/PP2-Summer/Lab4/Git tasks/JSON/sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn = attrs.get("dn", "")
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")
