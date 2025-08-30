import requests

url = "https://www.google.com"

params = {
    "q":"что покушать на ужин"
}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "cookie": "HSID=ALwVT9LEHrgVrzArZ; SSID=AsYwarzKGkWhlqnI-; APISID=D1TrP1eUpDZTH10U/Ar3QKpy69nTM1fKeL; SAPISID=ytTLpgkN-I0FUN-6/AHLUCoxu0py34mTEs; __Secure-1PAPISID=ytTLpgkN-I0FUN-6/AHLUCoxu0py34mTEs; __Secure-3PAPISID=ytTLpgkN-I0FUN-6/AHLUCoxu0py34mTEs; SEARCH_SAMESITE=CgQI9J0B; SID=g.a0000QjSlc_K466A7QqVQxcJchM2Zd5zJKEHAkDGcyq9J4f1AKSrSNDYpm27-9eCttn1haAt5gACgYKAYQSARcSFQHGX2MijwH-0UeYCEnwYqYPHt7cBhoVAUF8yKodu5njDXV8JdDUNh0YAr6_0076; __Secure-1PSID=g.a0000QjSlc_K466A7QqVQxcJchM2Zd5zJKEHAkDGcyq9J4f1AKSrXOmbL8ZOdxBv8DVGx3lJmQACgYKATkSARcSFQHGX2Mi6DTVmekkCVMVAE35B77T5hoVAUF8yKpCuvTqAPz2t07WMcBVSc7C0076; __Secure-3PSID=g.a0000QjSlc_K466A7QqVQxcJchM2Zd5zJKEHAkDGcyq9J4f1AKSriXhAQ3hHMnIe6aRxpEERDQACgYKAbkSARcSFQHGX2MiAmSOLqEbHxZ2xZnPNz7E4hoVAUF8yKpmn_lDJXs6cVFErhnh1u0w0076; AEC=AVh_V2j6A3XdK_p9Usvz3BHws8TOtWMNSG5ANS4UHIzz5BjIVku5EpIW7A; DV=4y0vgSk7xXxmQAgxTl7ANXbgb7q9j1mdS42dMzB-qAAAAMDFC8fRxHAAqwAAAOw7mDvytuuRSgAAAFgvVcgWkPXiFAAAQOO68tQc_ZSFBQAAAA; NID=525=eN2yZ0FjwJzlzgmTYazx4ZJBO-Ctps7Trdr18OU1NmJuMVJXFZxy15Cj21R-ZQ1c3WebhHiJCqTt6yH-j1gagrmNmPe_9mbNHcAafq0ZMuT74CWDHPtFIMVvSjfOvlS48tqykXXwm1g8u8kfuFc47vooN_C6TX0bdLSccwrRxiFffBmG3aEQKXsR5ufKMa777flh1-vosvBS3x2G6tfyoJsHZ2Get0zUYxrz5kAQwlUglWxHmR5GDcjk52Zvp-ukhwvvxNjKVLw5pj4EYsSlMi1-PBCK6Mnd_hc8DzyYd6i9nvB_i_Vwjh-Ey6tt7mXyMSj3xz9wq6x1kraGYy-UWHro0ewQsPZdFbKAG1NOebAzo0Fpo6qg12cFN6HdxMJYy7iMOoUIsf09237V35nZVryTr9po2Br9uJJssnV1myjZtYqpYYv0CMqXVQ8MUB49zp8uW3UXozFcK2jjMWDkH1yibaJvGjZRNH0R1JaeiiC8ElTk9QFJqw-y6-lE5K2WHmaYWHfrviYh3VYqAkbLlD55XN_NJwRko5lF_UFOeU4-HofbBoc7BqCZ7aC1K-CpEZsuGnnOZKmJQmGeqY3nfrsiFAWV0zxFUrR6UV4G0neDKEvv135wcLu6Epjtp-e6eIM4I5fQe7IUiwobc3-xmVhuNPL5FvODgjahsJ16SCtfwU1haB1DblSGDVGevpbyf2GaodbKoZvCytmVfLnnPN6Z2AlDjfUg; __Secure-1PSIDTS=sidts-Ci8B5H03Pwt6-JNJIdT8cUjG0khvFMILkAPowF0BPrrBCnvhYKFn1IAxfzUS8i5jIhAA; __Secure-3PSIDTS=sidts-Ci8B5H03Pwt6-JNJIdT8cUjG0khvFMILkAPowF0BPrrBCnvhYKFn1IAxfzUS8i5jIhAA; SIDCC=AKEyXzUh6VwarwzyseWrOciP5DCEFyQVAum0-w9T_i7eprU4NpqTgEhQRgIrH-uy_es5vfsikQ; __Secure-1PSIDCC=AKEyXzXFjqgrfwNzhKtidRb3tJ2BDHM8PSTHYJH1ODHckWudigG5dkZSGznjmC3qbcBAkgsgLP4; __Secure-3PSIDCC=AKEyXzUQvLxB-R6C9Xu2oj6y6z77ACLcRnfU867PJ4i1wxsiBqhkN2BYxqntUkbQd1wNkyszlRk"
}

response = requests.get(
    url=url, 
    params=params, 
    headers=headers
    )

print(f"Код ответа: {response.status_code}")

print(f"Тело страницы: {response.text}")

with open("task 2.html", "w", encoding="utf-8") as fl:
    fl.write(response.text)