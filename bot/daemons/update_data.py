import threading, requests, time

class UpdateData(object):
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            self.unstable_req = requests.get('https://api.covid19api.com/summary')
            if self.unstable_req.status_code > 199 and self.unstable_req.status_code < 300:
                self.req = self.unstable_req
                self.results = self.req.json()
                print("["+ str(threading.current_thread().getName()) +"] Covid data updated, response code {}".format(self.req.status_code))
            else:
                print("["+ str(threading.current_thread().getName()) +"] Covid data failed to update, reposnse code {}".format(self.req.status_code))
            time.sleep(30)