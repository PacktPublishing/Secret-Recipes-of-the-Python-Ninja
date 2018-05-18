import urllib.request
import urllib.error
import time

def single_thread_retrieval():
    start_time = time.time()
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
    try:
    	for url in urls:
    		urllib.request.urlopen(url)
    except urllib.error.HTTPError:
    	pass
    return time.time() - start_time
