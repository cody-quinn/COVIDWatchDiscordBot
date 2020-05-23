import threading, requests, time
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

        while True:
            self.unstable_req = requests.get('https://api.covid19api.com/summary')
            if 199 < self.unstable_req.status_code < 300:
                self.req = self.unstable_req
                self.results = self.req.json()
            else:
                log("Covid data failed to update, response code {}".format(self.unstable_req.status_code))
            time.sleep(30)