import os, threading, time, requests
from bot import log


class UpdateTopGG(object):
    def __init__(self, client):
        self.client = client
        if os.environ['BOT_TOKEN']:
            self.headers = {
                "content-type": "application/json",
                "authorization": os.environ['BOT_TOKEN'],
                "user-agent": "COVIDWatchDiscordBot/1.1 Python/3.8 requests/2.23.0"
            }

            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()
        else:
            log("No DBL token in preferences, not updating any bot pages.")

    def run(self):
        log("Update Data daemon started.")

        while True:
            payload = {"server_count": len(self.client.guilds)}
            req = requests.post("https://top.gg/api/bots/{}/stats".format(str(self.client.user.id)), json=payload, headers=self.headers)
            if 199 < req.status_code < 300:
                log("Successfully posted '" + str(payload) + "' to TopGG.")
            else:
                log("Failed to post guild count to TopGG, response code {}".format(req.status_code))
            time.sleep(600) # Run every 10 minutes