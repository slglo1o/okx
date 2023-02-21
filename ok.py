import requests
import time
import threading
import queue
import traceback
import random
import datetime
from datetime import datetime


class run_new:
    q = queue.Queue(1100)
    buy = float(2.000)  # 买入价格
    num = float(3.0000)  # 买入数量
    num_thread = 50  # 线程数量 运行次数
    kind = "GMX-USDT"
    kind_url = "https://www.okx.com/trade-spot/gmx-usdt"  # 需要配置
    cookie = 'G_ENABLED_IDPS=google; amp_56bf9d_okx.com=sk_3Dr7Oz_bPxgJVk2wjvX.WFp5TDZnd2FzQkJRSTk0bmd4UzNzQT09..1gf0b4an3.1gf0b4dq5.j.1.k; OptanonAlertBoxClosed=2022-10-11T01:16:42.906Z; amp_21c676=AWBoLlGYivlZF8hkj25xgt...1ghv45v2v.1ghv45v2v.0.0.0; amp_56bf9d=sk_3Dr7Oz_bPxgJVk2wjvX.ZUVyTTVQajNjVGh4M3NWdkszenFoZz09..1glkbs6ku.1glkc3m43.35.6.3b; __zlcmid=1DllV75aOL4DRhB; isLogin=1; first_ref=https%3A%2F%2Fwww.okx.com%2Ftrade-spot%2Froad-usdt; defaultLocale=zh_CN; locale=zh_CN; okg.currentMedia=2xl; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Feb+15+2023+17%3A43%3A55+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202212.1.0&geolocation=%3B&isIABGlobal=false&hosts=&consentId=3969faf8-d243-4328-b4f3-6b9e050da791&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A0%2CC0002%3A0%2CC0001%3A1&AwaitingReconsent=false; _monitor_ext'
    headers = {
        "Host": "www.okx.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
        "x-cdn": "https://static.okx.com",
        "Accept-Language": "zh-CN",
        "sec-ch-ua-mobile": "?0",
        "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJleDExMDE2NzM3MTE0MDg3NTYxQUY4Q0MyNEM4Mzg2NDY3MVNXc3YiLCJ1aWQiOiJpME1JbmFvemFvcXQ5bTdMQjhnRnpBPT0iLCJzdGEiOjAsIm1pZCI6ImkwTUluYW96YW9xdDltN0xCOGdGekE9PSIsImlhdCI6MTY3NjQ3MDE2MiwiZXhwIjoxNjc3MDc0OTYyLCJiaWQiOjAsImRvbSI6Ind3dy5va3guY29tIiwiaXNzIjoib2tjb2luIiwic3ViIjoiQTU1NTg4QjlGMTZEMzREOEY1ODRERDIwOTI1ODA4QjYifQ.8nv99zlMeADjz0dDA8G-c6LOC_iwpGN1NcqxEm2Icx-bpGnxRc1XltIt8DvC8mQcV9ok3aGjyxH2TUUwKalWwQ",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json",
        "x-utc": "8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.186.400 QQBrowser/11.3.5195.400",
        "App-Type": "web",
        "Origin": "https://www.okx.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": kind_url,
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": cookie
    }
    data = {"instId": kind, "tdMode": "cash", "_feReq": True, "side": "buy", "ordType": "limit", "px": buy, "sz": num}
    def queue_uee(self):
        for x in range(1000):
            self.q.put(1)

    def hick_ht(self):

        proxies_list = [
            {'https': 'socks5://sundaydx:silan123@16.162.217.158:32768'},
            {'https': 'socks5://sundaydx:silan123@18.166.178.18:32768'},
            {'https': 'socks5://sundaydx:silan123@18.167.12.53:32768'},
            {'https': 'socks5://sundaydx:silan123@16.163.147.66:32768'},
            {'https': 'socks5://sundaydx:silan123@18.162.169.229:32768'},
            {'https': 'socks5://sundaydx:silan123@18.162.152.213:32768'},
            {'https': 'socks5://sundaydx:silan123@43.198.81.69:32768'},
            {'https': 'socks5://sundaydx:silan123@16.162.22.181:32768'}]
        proxies = random.choice(proxies_list)
        try:
            response = requests.post("https://www.okx.com/priapi/v5/trade/order?t=1676419645086", json=self.data,
                                     headers=self.headers, proxies=proxies)
            w_3 = str(datetime.now().strftime("%a %b %d %H:%M:%S.%f %Y") + response.text)
            print(datetime.now().strftime("%a %b %d %H:%M:%S.%f %Y"), response.json())
            with open('/root/test1_test.txt', 'a', encoding="utf-8") as f1:
                f1.write("%sTRUE,\n" % w_3)
        except Exception as e:
            traceback.print_exc()
            print("!!!!!", e, "!!!!!")

    def start(self):
        threads = []
        while self.q.get(False, 1):
            for i in range(self.num_thread):
                time.sleep(0.013)
                t = threading.Thread(target=self.hick_ht)
                threads.append(t)
                t.start()


run = run_new()
run.queue_uee()

while True:
    a = time.time()
    c = int(round(a * 1000))
    b = "2023,Mon,Feb,16,23:46:58.600000"
    datetime_obj = datetime.strptime(b, "%Y,%a,%b,%d,%H:%M:%S.%f")
    ret_stamp = int(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
    if c == ret_stamp:
        run = run_new()
        run.start()
