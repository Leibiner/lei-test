# -*- coding: utf-8 -*-
# Author:   leibin
# Api层

import requests
import json

url = "https://test-bms.jaagro.com/jianan/yt-bms-bill/adjust/pay/bill/page"

payload = json.dumps({
  "auditStatus": "1",
  "query": {
    "current": 1,
    "size": 10
  }
})
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOjE0NDI3NjYxMjEzNzY2MDAwNjUsImFjY291bnQiOiJaSDIxMDkyODAwNDA3IiwicGhvbmUiOm51bGwsInV1aWQiOiI4OGIxZDVmNy03NGQ2LTQwY2QtOGEyNS01NTllNjQ4MmFmNWMiLCJzdWIiOiIxNDQyNzY2MTIxMzc2NjAwMDY1IiwiaWF0IjoxNjUxODAyMDg2LCJleHAiOjE2NTI0MDY4ODZ9.VL8az0a64pIPRTKGCD0VZgOJ06tEm_AsSa8fGmRMK20_VPL1vuBRYtn-DLaovkU_oWhUuIG5n847lvM7UGEEGQ',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Cookie': 'UM_distinctid=17f9772d34e22c-028e2b2f7400cd-133a645d-13c680-17f9772d34fa1f',
  'Origin': 'https://test-bms.jaagro.com',
  'Referer': 'https://test-bms.jaagro.com/jaagro/bms/adjustManage/deliver/deliverQueryList',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)



