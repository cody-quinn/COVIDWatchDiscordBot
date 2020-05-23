import threading, datetime

def log(x):
    print("[{}] [{}]: {}".format(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), threading.current_thread().getName(), x), end='\n')