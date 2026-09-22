import json
import urllib.request

print("🌧️ 開始抓取今日天氣資訊...")

# Open-Meteo 台北天氣 API
url = "https://api.open-meteo.com/v1/forecast?latitude=25.0330&longitude=121.5654&current_weather=true"

# 建立 Request 物件並加入 User-Agent
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
)

try:
    # 直接使用預設的 urlopen，不需要設定 Proxy
    with urllib.request.urlopen(req) as response:
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
    print(f"❌ 抓取失敗，錯誤原因: {e}")
