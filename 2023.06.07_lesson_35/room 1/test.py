# import requests
# import multiprocessing
# import time
#
# session = None
#
#
# def set_global_session():
#     global session
#     if not session:
#         session = requests.Session()
#
#
# def download_site(url):
#     with session.get(url) as response:
#         name = multiprocessing.current_process().name
#         print(f"{name}:Read {len(response.content)} from {url}")
#
#
# def download_all_sites(sites):
#     with multiprocessing.Pool(initializer=set_global_session) as pool:
#         pool.map(download_site, sites)
# #
# #
# # if __name__ == "__main__":
# #     sites = [
# #         "https://www.jython.org",
# #         "http://olympus.realpython.org/dice",
# #     ] * 80
# #     start_time = time.time()
# #     download_all_sites(sites)
# #     duration = time.time() - start_time
# #     print(f"Downloaded {len(sites)} in {duration} seconds")
#
# # ---------------------------------------------------------------------------------------------
#
#
# import requests
# import multiprocessing
# import time
# #
# #
# # def usd():
# #     url_usd = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20230605&end=%2020230605&valcode=usd&sort=exchangedate&order=desc&json'
# #
# #     rez_usd = requests.get(url_usd)
# #
# #     print(rez_usd.text)
# #
# #
# # def eur():
# #     url_eur = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20230605&end=%2020230605&valcode=eur&sort=exchangedate&order=desc&json'
# #
# #     rez_eur = requests.get(url_eur)
# #
# #     print(rez_eur.text)
# #
# #
# # def gbp():
# #     url_f = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20230605&end=%2020230605&valcode=gbp&sort=exchangedate&order=desc&json'
# #
# #     rez_f = requests.get(url_f)
# #
# #     print(rez_f.text)
# #
# #
# # start = time.time()
# # usd()
# # eur()
# # gbp()
# # finish = time.time() - start
# # print(finish)
# #
# # usd_ = multiprocessing.Process(target=usd)
# # eur_ = multiprocessing.Process(target=eur)
# # gbp_ = multiprocessing.Process(target=gbp)
# #
# # if __name__ == '__main__':
# #     start = time.time()
# #     usd_.start()
# #     eur_.start()
# #     gbp_.start()
# #     usd_.join()
# #     eur_.join()
# #     gbp_.join()
# #     finish = time.time() - start
# #     print(finish)
#
# def fibonacci(n):
#     if n in {0, 1}:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# # start1 = time.time()
# # print(fibonacci(35))
# # print(fibonacci(36))
# # print(fibonacci(33))
# # finish1 = time.time() - start1
# # print(finish1)
#
#
# q = multiprocessing.Pool()
# usd_ = multiprocessing.Process(target=fibonacci, args=(35,))
# eur_ = multiprocessing.Process(target=fibonacci, args=(36,))
# gbp_ = multiprocessing.Process(target=fibonacci, args=(33,))
#
# if __name__ == '__main__':
#
#     # start = time.time()
#     # usd_.start()
#     # eur_.start()
#     # gbp_.start()
#     # usd_.join()
#     # eur_.join()
#     # gbp_.join()
#     # finish = time.time() - start
#     # print(finish)
#
#     start1 = time.time()
#     print(fibonacci(35))
#     print(fibonacci(36))
#     print(fibonacci(33))
#     finish1 = time.time() - start1
#     print(finish1)


