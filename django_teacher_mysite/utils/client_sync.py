import requests, time

start = time.time()
for i in range(5):
    res = requests.get("http://localhost:8000/app_1/index_1/") # 0.08-0.1s (5 requests), when sleep(1) - 5.07
    # res = requests.get("http://localhost:8000/app_1/") # 0.38- 0.4s (5 requests)
    print(f'res {i} = {res}')

print(f'time = {time.time() - start}')

