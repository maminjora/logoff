Bu program okullar ve eğitim için kullanılabilir.
Sınıflardaki akıllı tahtalarınızı bu programla tenefüs saatlerinde ve öğle aralarında otomatik kilitleyebilirsiniz.
Program belli olduğu üzere belli saatler için programlandı.Bu saatleri tenefüs başlama ve 
bitirme sürelerini saat ve dakika cinsinden arada herhangi bir işaret olmadan sayı olarak değiştirirseniz,program çalıştığında
bilgisayar otomatik olarak kilitlenecektir.

programı exe formatına çevirmek için önce pip ile pyinstaller kurup sonrasında : pyinstaller --onefile --noconsole --icon=fav.ico logoff.py şeklinde exe ye çevirebilirsiniz.
programı ücretsiz olarak çevirdiğiniz için yani bir lisansınız olmadığı için windows bu uygulamayı zararlı olarak tanımlayacaktır.bilgisayarlarda programı çalıştıracağınız klasörü 
windows virüs koruma ayarlarından dışarıda bırakılanlar klasörüne eklerseniz program sorunsuz çalışacaktır.

This program for school's and education places.
If teacher want to lock class computers at specific time,you can change times and you can use.After all you can install pyinstaller and write this code for make exe:
pyinstaller --onefile --noconsole --icon=fav.ico logoff.py

Codes:

-----------------------------------------------------------------------------------
    
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

-----------------------------------------------------------------------------------
