import os
import time

# 現在時刻を取得
current_time = time.localtime()

# 3時かどうかを判定
if current_time.tm_hour == 15 and current_time.tm_min == 0:
    print("Hello Snack!")
else:
    print("Hello World!")