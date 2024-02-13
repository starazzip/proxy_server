import requests

proxies = {
    'http': 'http://1094357-1.wctv.static-ip.tinp.net.tw:10026',
}

response = requests.get('http://google.com', proxies=proxies)

print(response.text)
