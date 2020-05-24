import threading, requests, time, os, json
from bot import log

class UpdateData(object):
    def __init__(self):
        self.unstable_req = None
        self.req = None
        self.results = None

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        log("Update Data daemon started.")
        url = 'https://api.covid19api.com/all'

        while True:
            last_modified = 0
            datafile = os.getcwd() + os.path.sep + "data.json"
            if os.path.exists(datafile) and os.path.isfile(datafile):
                last_modified = os.path.getmtime(datafile)

            if (time.time() - last_modified) > 3600:
                log("Attempting to update data")
                with requests.get(url, stream=True) as response:
                    with open(datafile, "wb") as f:
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                log("Data update finished")
            time.sleep(60)