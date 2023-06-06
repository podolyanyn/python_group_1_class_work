import threading
import requests
import time

#request = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&valcode=EUR&date=20230605"

#r = requests.get(request)
#print(r.text)
currency = ["GBP", "EUR", "USD"]

start = time.perf_counter()
for i in currency:
   req = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&valcode={i}&date=20230605")
   print(req.json())
end = time.perf_counter()

print(f"\n3 requests took: {end - start} seconds")

threads = list()

start = time.perf_counter()
def rqst(curr):
    req = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&valcode={curr}&date=20230605"
    request = requests.get(req)
    print(request.json())


for i in currency:
    tmp = threading.Thread(target = rqst, args=(i, ))
    threads.append(tmp)
    tmp.start()

for thread in threads:
    thread.join()
end = time.perf_counter()

print(f"\n3 requests with threads took: {end - start} seconds")


###################################################

import threading
import time

def fibb(num):
    a = 0
    b = 1
    c = 0

    for i in range(num - 1):
        c = a + b
        a = b
        b = c

    return c

start = time.perf_counter()

for i in range(5):
    fibb(20000)

end = time.perf_counter()

print(f"Without threading: {end-start} seconds")

threads = list()
start = time.perf_counter()

for i in range(5):
    tmp = threading.Thread(target=fibb, args=(20000,))
    threads.append(tmp)
    tmp.start()

for t in threads:
    t.join()

end = time.perf_counter()
print(f"With threading: {end-start} seconds")