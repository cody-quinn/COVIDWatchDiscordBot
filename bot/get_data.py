import os, json

def get_data():
    data_file = os.getcwd() + os.path.sep + "files" + os.path.sep + "data.json"
    if not os.path.exists(data_file) or not os.path.isfile(data_file):
        return {"Status": 404}
    else:
        try:
            with open(data_file, "r") as f:
                results = json.loads(f.read().replace('\n', ''))
            return {"Status": 200, "Result": results}
        except:
            return {"Status": 500}