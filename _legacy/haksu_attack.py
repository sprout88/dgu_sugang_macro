import requests
import datetime


current_time = datetime.datetime.now()


# URL to send the POST request to
url = 'https://sugang.dongguk.edu/sugang/d/sugangMode?fake=1691368371161'

# Headers for the POST request

for i in range(1,2):
    haksus = ["PRI4024%4004","PRI4027%4001","EGC7026%4002","RGC0003%4004","ENE2016%4002","SCS2011%4001","SCS2013%4001"]
    # Data to be sent in the POST request\
    for haksu in haksus:
        nid='1'
        headers = {
            'Host': 'sugang.dongguk.edu',
            'Cookie': f'WMONID=ZMCmgWGRz2l; JSESSIONID=3941fd69788040edae0fd5121a91ea624216b9f3eb6f05db1325!1714995062; app-version={{"guid":"9c071b66-caa9-ebaa-a0e6-e149da2cc0fc","timestamp":1691368371061}}; NetFunnel_ID={nid}; NetFunnelID=service_1/act_2',
            'Content-Length': '31',
            'Sec-Ch-Ua': '',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36',
            'Sec-Ch-Ua-Platform': '""',
            'Origin': 'https://sugang.dongguk.edu',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://sugang.dongguk.edu/core/coreMain?fake=1691368230494',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'close'
        }
        data = {
            'params': f'{haksu}',
            'mode': 'insert'
        }

        # Sending the POST request
        response = requests.post(url, headers=headers, data=data)

        # Check the response status
        if response.status_code == 200:
            print(f"학수번호:{haksu}")
            print(response.text)
            print("Current time:", current_time)
        else:
            print(f"Failed to send POST request. Status code: {response.status_code}")