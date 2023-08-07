import requests

def get_server_time_milliseconds(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            server_time = int(response.headers['Date'])
            return server_time
    except (requests.ConnectionError, requests.Timeout, KeyError):
        pass

    return None

if __name__ == "__main__":
    server_url = 'https://sugang.dongguk.edu/'  # 실제 서버 URL로 교체해야 합니다.

    server_time_milliseconds = get_server_time_milliseconds(server_url)

    if server_time_milliseconds is not None:
        print(f"서버 시간 (밀리초): {server_time_milliseconds}")
    else:
        print("서버 시간을 가져올 수 없습니다.")
