import os, json
from pathlib import Path

def get_preferences():
    pref_file = os.getcwd() + os.path.sep + "files" + os.path.sep + "preferences.json"
    Path(os.getcwd() + os.path.sep + "files").mkdir(parents=True, exist_ok=True)
    if not os.path.exists(pref_file) or not os.path.isfile(pref_file):
        default = {"bot_token": ""}
        with open(pref_file, "w+") as f:
            f.write(json.dumps(default, sort_keys=True, indent=4, separators=(',', ': ')))
        return default
    else:
        with open(pref_file, "r") as f:
            results = json.loads(f.read().replace('\n',''))
        return results