import json
import urllib.request

print("🌧️ 開始抓取今日天氣資訊...")

# 使用免費、免密鑰的國際天氣 API 抓取台北天氣
url = "https://open-meteo.com"

# 關鍵改動：建立一個 Request 物件，並加入 User-Agent 標頭，偽裝成一般的電腦 Chrome 瀏覽器
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
)

try:
    # 這裡改成讀取我們偽裝過的 req，而不是原本的 url
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

