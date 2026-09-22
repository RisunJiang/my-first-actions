import json
import urllib.request
from itertools import cycle

proxies = [
    'http://10.10.1.10:3128',
    'https://10.10.1.11:1080'
]
proxy_pool = cycle(proxies)

print("🌧️ 開始抓取今日天氣資訊...")

# 修正 1：使用真正的 API 網址 (附帶台北的經緯度與開啟 current_weather)
url = "https://api.open-meteo.com/v1/forecast?latitude=25.0330&longitude=121.5654&current_weather=true"

# 修正 2：從 proxy_pool 中取出一個代理伺服器 IP
proxy = next(proxy_pool)

# 修正 3：正確使用 urllib 設定 Proxy 的方式
proxy_handler = urllib.request.ProxyHandler({
    "http": proxy,
    "https": proxy
})
opener = urllib.request.build_opener(proxy_handler)

# 建立 Request 物件並加入 User-Agent，不再傳入 proxies 參數
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
)

try:
    # 修正 4：使用我們帶有 proxy 的 opener 來發送請求，而不是原本的 urlopen
    with opener.open(req) as response:
        data = json.loads(response.read().decode())
        current = data["current_weather"]
        temp = current["temperature"]
        windspeed = current["windspeed"]
        
        print("====== 今日天氣報告 ======")
        print(f"🌡️ 目前氣溫: {temp} °C")
        print(f"💨 目前風速: {windspeed} km/h")
        print("==========================")
        print("🎉 天氣資料抓取成功！")
        
except Exception as e:
    print(f"❌ 抓取失败，错误原因: {e}")
