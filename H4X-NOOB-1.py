import os, platform, time

print('\x1b[1;36m[●] Checking Update.....');time.sleep(0.5)
os.system('git pull')
def Update():
    exit('\033[1;31m[●] Commands On Update Please Wait For Update ❤ ')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            print("\x1b[1;95m[●] Congratulations ! Your Device Support this Tools")
            print('[●] Follow My Github First')
            os.system('xdg-open https://github.com/H4X-GG')
            import DATA64
        elif bit == '32bit':
            print("\n\x1b[1;92m[●] Congratulations ! Your Device Support this Tools")
            print('[●] Follow My Github First')
            os.system('xdg-open https://github.com/H4X-GG')
            import DATA32
        else:
            exit('\033[1;31m[●] Connection & Network Error')
Run()
