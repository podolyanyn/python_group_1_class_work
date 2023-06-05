# / Стандартна однопоточна програма
# import requests
# import time
#
#
# def download_site(url, session):
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")
#
#
# def download_all_sites(sites):
#     with requests.Session() as session:
#         for url in sites:
#             download_site(url, session)
#
#
# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")

#
# import concurrent.futures
# import requests
# import threading
# import time
#
#
# thread_local = threading.local()
#
#
# def get_session():
#     if not hasattr(thread_local, "session"):
#         thread_local.session = requests.Session()
#     return thread_local.session
#
#
# def download_site(url):
#     session = get_session()
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")
#
#
# def download_all_sites(sites):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
#         executor.map(download_site, sites)
#
#
# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")

import requests
import threading
import time


def usd():
    url_usd = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20230605&end=%2020230605&valcode=usd&sort=exchangedate&order=desc&json'

    rez_usd = requests.get(url_usd)

    print(rez_usd.text)

def eur():
    url_eur = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20230605&end=%2020230605&valcode=eur&sort=exchangedate&order=desc&json'

    rez_eur = requests.get(url_eur)

    print(rez_eur.text)

def gbp():
    url_f = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20230605&end=%2020230605&valcode=gbp&sort=exchangedate&order=desc&json'

    rez_f = requests.get(url_f)

    print(rez_f.text)

# start = time.time()
# usd()
# eur()
# gbp()
# finish = time.time() - start
# print(finish)

# usd_ = threading.Thread(name='usd', target=usd)
# eur_ = threading.Thread(name='eur', target=eur)
# gbp_ = threading.Thread(name='gbp', target=gbp)


# start = time.time()
# usd_.start()
# eur_.start()
# gbp_.start()
# usd_.join()
# eur_.join()
# gbp_.join()
# finish = time.time() - start
# print(finish)

def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


usd_ = threading.Thread(target=fibonacci_of, args=(35,))
eur_ = threading.Thread(target=fibonacci_of, args=(33,))
gbp_ = threading.Thread(target=fibonacci_of, args=(31,))

start1 = time.time()
usd_.start()
eur_.start()
gbp_.start()
usd_.join()
eur_.join()
gbp_.join()
finish1 = time.time() - start1
print('thread"s time: ', finish1)



start = time.time()
print(fibonacci_of(35))
print(fibonacci_of(33))
print(fibonacci_of(31))

finish = time.time() - start
print('simple time: ',finish)






