import requests
from itertools import cycle

proxies = [
    'http://10.10.1.10:3128',
    'https://10.10.1.11:1080'
]
proxy_pool = cycle(proxies)

url = "https://api.open-meteo.com/v1/forecast?latitude=39.0707&longitude=117.1527&current_weather=true"
proxy = next(proxy_pool)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...'}
proxy_dict = {"http": proxy, "https": proxy}

try:
    # requests 直接支援 proxies 和 headers 參數，並有內建的 .json() 方法
    response = requests.get(url, headers=headers, proxies=proxy_dict, timeout=10)
    response.raise_for_status() # 檢查是否有 HTTP 錯誤
    
    current = response.json()["current_weather"]
    print(f"🌡️ 目前气温: {current['temperature']} °C")
    print(f"💨 目前风速: {current['windspeed']} km/h")
except Exception as e:
    print(f"❌ 抓取失败: {e}")
