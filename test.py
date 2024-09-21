import requests
# 設定中央氣象局的API的Token
CWA_API_KEY = 'CWB-FE4AD205-4642-40AD-B7FD-336A53D1ED2A'
# 氣象API的URL
weather_api_url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization={CWA_API_KEY}&limit=100'
# 取得氣象資料
def get_weather_data():
  response = requests.get(weather_api_url)
  if response.status_code == 200:
        data = response.json()
        return data
  else:
        return "無法取得氣象資料"
# 將訊息推送到LINE Notify
def send_line_notify(LINE_NOTIFY_TOKEN,message,image_url=None):
    headers = {
        "Authorization": f"Bearer {LINE_NOTIFY_TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {'message': message}
    line_notify_url = 'https://notify-api.line.me/api/notify'

    if image_url:
        image_payload = {
            'message': '地震報告圖片:',
            'imageThumbnail': image_url,
            'imageFullsize': image_url
        }
        response = requests.post(line_notify_url, headers=headers, params=image_payload)

    # 發送訊息到LINE
    response = requests.post(line_notify_url, headers=headers, params=payload)
    if response.status_code == 200:
        print("成功推送訊息到LINE")
    else:
        print("推送失敗，請檢查Token或訊息格式")
data = get_weather_data()
#print(data)
rcontent = data["records"]["Earthquake"][0]["ReportContent"]
ruri= data["records"]["Earthquake"][0]["ReportImageURI"]
print(rcontent)
print(ruri)
LINE_NOTIFY_TOKEN = 'zRX73owzpWQ0INErvp2DuGtSAYyOvgjF2WTHYeOyJ0T'
send_line_notify(LINE_NOTIFY_TOKEN,rcontent,ruri)
