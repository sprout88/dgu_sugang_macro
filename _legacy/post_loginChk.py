import requests
import json  # Import the json module to handle JSON data

url = "https://sugang.dongguk.edu/login/loginChk"

# Set the JSESSIONID and NetFunnel_ID as variables
JSESSIONID = "deaf75bb05084602927710f0fd08cd6e4ff1a2fcf89dc5c764ae!-662580245"
NetFunnel_ID = "79E9FE088E2CDBE6BA57078BF411D466BA1DBC4BB0D8D6D7945F273E973B80D22F9FD708113B1C8700824A4043B35D3F2B130F0A676AD1B2EB8C96FE333C493E6A16A170870F7530ADBF9279AABD975FEFF493EACABAB67E3DCB8ACA052C0EE2D9FE538FD9FA6384F0DC80C40785784F3AB2C009AB68E9221B82D7F8C07DC2F5746572"

# Convert the app-version dictionary to a JSON string using json.dumps()
app_version_data = {
    "guid": "f7a2f87c-0ae5-228b-51e5-6ac59e6beba0",
    "timestamp": 1691321889042
}
app_version_str = json.dumps(app_version_data)

headers = {
    "Host": "sugang.dongguk.edu",
    "Cookie": f"WMONID=ZMCmgWGRz2l; JSESSIONID={JSESSIONID}; app-version={app_version_str}; NetFunnel_ID={NetFunnel_ID}; NetFunnelID=service_1/act_1",
    "Content-Length": "48",
    "Sec-Ch-Ua": "",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36",
    "Sec-Ch-Ua-Platform": "",
    "Origin": "https://sugang.dongguk.edu",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://sugang.dongguk.edu/login",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close"
}

payload = {
    "txtUserID": "2018111943",
    "txtPwd": "asdf8971!@",
    "lang": "ko"
}

response = requests.post(url, headers=headers, data=payload)

# Check the response status code
if response.status_code == 200:
    print("Request successful!")
    print("Response content:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
