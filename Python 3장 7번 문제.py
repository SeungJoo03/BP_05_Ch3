Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> now_minute = time.time() // 60
>>> minute = now_minute % 60
>>> hour = now_minute // 60 % 24
>>> 
>>> print("현재 시간 (영국 그리니치 시각) :", hour + 1, "시", minute, "분")
현재 시간 (영국 그리니치 시각) : 18.0 시 36.0 분
