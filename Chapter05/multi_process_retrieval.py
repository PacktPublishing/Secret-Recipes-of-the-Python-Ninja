import urllib.request, urllib.error 
from multiprocessing.dummy import Pool 
import time

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

# Make the Pool of workers
pool = Pool(4) 

# Open the urls in their own process
try:
    pool.map(urllib.request.urlopen, urls)
except urllib.error.HTTPError:
    pass

#close the pool and wait for the work to finish 
pool.close() 
pool.join() 

print('Done! Time taken: {}'.format(time.time() - start_time))
