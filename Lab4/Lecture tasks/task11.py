import json

json_string = '{"course": "Python", "level": "beginner"}'

data = json.loads(json_string)

print(data["course"])  
