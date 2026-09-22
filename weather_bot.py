import json
import urllib.request

print("🌧️ 開始抓取今日天氣資訊...")

# 使用免費、免密鑰的國際天氣 API 抓取台北天氣（你也可以換成其他城市）
url = "https://open-meteo.com"

try:
    with urllib.request.urlopen(url) as response:
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
