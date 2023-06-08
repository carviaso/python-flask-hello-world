import subprocess
import json
data = subprocess.check_output(["pip", "list", "--format", "json"])
parsed_results = json.loads(data)
[(element["name"], element["version"]) for element in parsed_results]

print((element["name"]) for element in parsed_results)