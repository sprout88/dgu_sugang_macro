import requests

url = "https://nf.dongguk.edu/ts.wseq"
params = {
    "opcode": "5101",
    "nfid": "0",
    "prefix": "NetFunnel.gRtype=5101;",
    "sid": "service_1",
    "aid": "act_1",
    "js": "yes",
    "1691325825842": ""
}

headers = {
    "Host": "nf.dongguk.edu",
    "Sec-Ch-Ua": "",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36",
    "Sec-Ch-Ua-Platform": "",
    "Accept": "*/*",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Dest": "script",
    "Referer": "https://sugang.dongguk.edu/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close"
}

for i in range(0,1000):
    response = requests.get(url, params=params, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        print("Request successful!")
        print("Response content:")
        print(response.text)
    else:
        print(f"Request failed with status code {response.status_code}")
