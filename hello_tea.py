import requests

def hello_tea_func():
    response = requests.get('https://app.tea.xyz/')
    print("Hello teaxyzzz6!")
    print("Status teaxyzzz6:", response.url, response.ok)
