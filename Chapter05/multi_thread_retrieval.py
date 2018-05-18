import time 
import threading 
import queue 
import urllib.request, urllib.error 

class Receiver(threading.Thread): 
    def __init__(self, queue): 
        threading.Thread.__init__(self)
        self._queue = queue 

    def run(self):
        while True: 
            url = self._queue.get() 
            if isinstance(url, str) and url == 'quit':
                break
            try:
    	        urllib.request.urlopen(url)
            except urllib.error.HTTPError:
    	        pass


def Creator():
    urls = ["https://www.python.org", 
            "https://www.google.com", 
			"https://www.techdirt.com",
			"https://www.facebook.com",
			"https://www.ibm.com",
			"https://www.dell.com",
			"https://www.amd.com",
			"https://www.yahoo.com",
			"https://www.microsoft.com",
			"https://www.apache.org"]
  
    cue = queue.Queue()
    worker_threads = build_worker_pool(cue, 4)
    start_time = time.time()

    for url in urls: 
        cue.put(url)  

    for worker in worker_threads:
        cue.put('quit')
    for worker in worker_threads:
        worker.join()

    print('Done! Time taken: {}'.format(time.time() - start_time))

def build_worker_pool(cue, size):
    workers = []
    for _ in range(size):
        worker = Receiver(cue)
        worker.start() 
        workers.append(worker)
    return workers

if __name__ == '__main__':
  Creator()
