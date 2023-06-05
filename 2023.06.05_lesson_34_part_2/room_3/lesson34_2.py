import requests
import threading
from time import time
#
#
#
#
# def get_curr(cur):
#     url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&date=20230605"
#     response = requests.get(url)
#     data = response.json()
#     for _ in data:
#         if _['cc'] == cur:
#             print(_['txt'], ':', _['rate'])
#
#
# if __name__ == '__main__':
#     start = time()
#     get_curr('MXN')
#     get_curr('MDL')
#     get_curr('ILS')
#     # currencies = ['USD', 'EUR', 'TRY']
#     # currencies = ['PLN', 'INR', 'CAD']
#     # for _ in currencies:
#     #     t = threading.Thread(target=get_curr, args = (_,))
#     #     t.start()
#     end = time()
#     print((end-start))
#
#
#     return sm
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
# #
# # poslidovno = 0.001993894577026367
# # threading = 0.002992868423461914
# if __name__ == '__main__':
#     start = time()
#     # recur_fibo(5)
#     # recur_fibo(10)
#     # recur_fibo(20)
#     # ns_ = [5000, 10000, 100000]
#     ns_ = [5, 10, 20]
#     for _ in ns_:
#         t = threading.Thread(target=recur_fibo, args = (_,))
#         t.start()
#     end = time()
#     print((end-start))
