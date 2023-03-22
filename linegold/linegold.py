import requests
from bs4 import BeautifulSoup
weburl = "https://www.goldtraders.or.th/default.aspx"
r = requests.get(weburl)
r.encoding = 'utf-8'
sup = BeautifulSoup(r.text,'lxml')

Linetoken = "mSZxdp4OmaUapVnbiRLbJXjX4NzhuQXGcaaxfuG6v2V"

def LineNotifyMessage(message):
    payload = {'message':message}
    return LineNotify(payload)
def LineNotify(payload,file=None):
    url = 'https://notify-api.line.me/api/notify'
    token = Linetoken
    headers = {'Authorization':'Bearer ' + token}
    return requests.post(url, headers=headers , data = payload, files=file)
def goldpricecheck():
    LineNotifyMessage("ประกาศจากสมาคมค้าทองคำ" + "\nประจำวันที่ "+ sup.find(id = 'DetailPlace_uc_goldprices1_lblAsTime').text + "\nทองคำแท่ง 96.5%" + "\nขายออก " + sup.find(id= 'DetailPlace_uc_goldprices1_lblBLSell').text + "\nรับซื้อ " + sup.find(id= 'DetailPlace_uc_goldprices1_lblBLBuy').text + "\nทองรูปพรรณ 96.5%" + "\nขายออก " + sup.find(id= 'DetailPlace_uc_goldprices1_lblOMSell').text + "\nรับซื้อ " + sup.find(id= 'DetailPlace_uc_goldprices1_lblOMBuy').text)
    
goldpricecheck()
