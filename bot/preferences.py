import os, json

def getPreferences():
    pref_file = os.getcwd() + os.path.sep + "preferences.json"
    if not os.path.exists(pref_file) or not os.path.isfile(pref_file):
        default = {"bot_token": "", "dbl_token": ""}
        with open(pref_file, "w+") as f:
            f.write(json.dumps(default))
        return default
    else:
        with open(pref_file, "r") as f:
            results = json.loads(f.read().replace('\n',''))
        return results