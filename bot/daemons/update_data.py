import threading, requests, time

class UpdateData(object):
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            self.req = requests.get('https://api.covid19api.com/summary')
            self.results = self.req.json()
            print("Covid data updated, response code {}".format(self.req.status_code))
            time.sleep(30)