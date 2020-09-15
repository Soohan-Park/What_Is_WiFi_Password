import os


def main():
    os.system("clear")

    WiFiName = os.popen("netsh wlan show interfaces")
    while True:
        target = WiFiName.readline()
        if "SSID" in target:
            target = target.split(':')[1].strip()
            break
    
    data = os.popen("""netsh wlan show profile name="{}" key=clear""".format(target))
    while True:
        finalKey = data.readline()
        if "키 콘텐츠" in finalKey:
            finalKey = finalKey.split(':')[1].strip()
            break
    
    print("지금 WiFi 비밀번호 : {}".format(finalKey))
    os.system("Pause")


if __name__ == "__main__":
    main()