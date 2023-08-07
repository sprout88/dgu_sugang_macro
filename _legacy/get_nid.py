import requests

url = "https://nf.dongguk.edu/ts.wseq"
params = {
    "opcode": "5004",
    "key": "3BE2E5E597F9BC7E9CECD35AB10245AC2B115E2B61562DB35B3D387F307F219776B9D831E9F17EA22818615DCB08CACC0986A6C9CB8F3043086C969D6525D5976A16A170870F7530ADBF9279AABD975FF6F4072BE805A8BF33B6EDD584C0CF0BD9FE538FD9FA6384F0DC80C40785784F3AB2C009AB68E9221B82D7F8C07DC2F5746572",
    "nfid": "0",
    "prefix": "NetFunnel.gRtype=5004;",
    "js": "yes",
    "1691370578570": ""
}

headers = {
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
    "Connection": "close",
}

response = requests.get(url, params=params, headers=headers)

print(response.status_code)
print(response.text)
