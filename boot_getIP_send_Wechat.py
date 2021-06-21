# -*- coding: utf-8 -*-
# author : ziheng_wind

"""
感谢前人留下的资料
学无止尽
"""
import requests
import socket
import time


def getip():

    time.sleep(15)
    ip = requests.get('http://ip.42.pl/raw').text
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip_1 = s.getsockname()[0]
    finally:
        s.close()
    desp = "- 公网IP"+ip + "- 局域网IP"+ip_1
    print(desp)
    data = {
        'text': '俺上线啦 这是俺的IP 还有局域网IP',
        'desp': desp
    }
    req = requests.post('https://sc.ftqq.com/YOUR_KRY.send', data=data)




if __name__ == "__main__":
    getip()
