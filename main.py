import requests

response = requests.get('https://httpbin.org/get')
print(response.status_code)
print(response.text)

with open('result.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
