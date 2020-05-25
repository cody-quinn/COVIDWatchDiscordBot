import threading, requests, time, os
from pathlib import Path

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
        Path(os.getcwd() + os.path.sep + "files").mkdir(parents=True, exist_ok=True)

        while True:
            last_modified = 0
            datafile = os.getcwd() + os.path.sep + "files" + os.path.sep + "data.json"
            if os.path.exists(datafile) and os.path.isfile(datafile):
                last_modified = os.path.getmtime(datafile)

            if (time.time() - last_modified) > 3600:
                log("Attempting to update data.json")
                with open(datafile, "wb") as f:
                    f.truncate(0)
                    f.write(bytes('{"Regional":', 'utf-8'))
                    with requests.get('https://api.covid19api.com/all', stream=True) as response:
                        if 299 < response.status_code < 200:
                            log("Failed to update data.json; 'https://api.covid19api.com/all' returned a " + str(response.status_code))
                            return
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                    f.write(bytes(', "Global":', 'utf-8'))
                    time.sleep(5)
                    with requests.get('https://api.covid19api.com/summary', stream=True) as response:
                        if 299 < response.status_code < 200:
                            log("Failed to update data.json; 'https://api.covid19api.com/summary' returned a " + str(response.status_code))
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                    f.write(bytes('}', 'utf-8'))

                log("Data.json update finished")
            time.sleep(60)

            #https://api.covid19api.com/summary