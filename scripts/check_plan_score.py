import json
with open("C:/Users/Alexa/Desktop/SandBox/judge_results/plans_audit.json") as f:
    data = json.load(f)
for p in data["results"]:
    if "comprehensive-implementation" in p.get("file", ""):
        print(json.dumps(p, indent=2))
        break
