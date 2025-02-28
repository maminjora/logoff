import ctypes
from datetime import datetime
import time
import os

while True:
    suan = datetime.now()
    gun = suan.weekday()
    simdi = suan.strftime("%H%M")
    simdi = int(simdi)
    time.sleep(0.1)

    if gun == 5 or gun == 6:
        break

    elif gun == 4:
        if simdi == 1600:
            os.system("shutdown /s")

    else:
        if simdi >= 800 and simdi < 840:
            ctypes.windll.user32.LockWorkStation()

        elif simdi >= 921 and simdi < 935:
            ctypes.windll.user32.LockWorkStation()

        elif simdi >= 1016 and simdi < 1025:
            ctypes.windll.user32.LockWorkStation()

        elif simdi >= 1106 and simdi < 1115:
            ctypes.windll.user32.LockWorkStation()

        elif simdi >= 1156 and simdi < 1205:
            ctypes.windll.user32.LockWorkStation()

        elif simdi >= 1246 and simdi < 1330:
            ctypes.windll.user32.LockWorkStation()

        elif simdi >= 1411 and simdi < 1420:
            ctypes.windll.user32.LockWorkStation()

        elif simdi >= 1501 and simdi < 1510:
            ctypes.windll.user32.LockWorkStation()

        elif simdi >= 1551 and simdi < 1600:
            ctypes.windll.user32.LockWorkStation()

        elif simdi >= 1641 and simdi < 1700:
            ctypes.windll.user32.LockWorkStation()
        
        elif simdi >= 1641 and simdi < 1700:
            ctypes.windll.user32.LockWorkStation()

        elif simdi == 1710:
            os.system("shutdown /s")

        else:
            continue

    # by ibrahimkayip.com.tr