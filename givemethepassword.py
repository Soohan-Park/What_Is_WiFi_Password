import os


def main():
    # Shell별 상이한 명령어로 인해 clear 명령 수행 생략.
    # os.system("clear")

    print("=== GIVE ME THE PASSWORD ===")

    WiFiName = os.popen("netsh wlan show interfaces")
    while True:
        target = WiFiName.readline()
        if "SSID" in target:
            target = target.split(':')[1].strip()
            break

    print("SSID :: {}".format(target))

    finalKey = None
    data = os.popen("""netsh wlan show profile name="{}" key=clear""".format(target))
    for _ in range(100):
        dataLine = data.readline()
        if "키 콘텐츠" in dataLine:
            finalKey = finalKey.split(':')[1].strip()
            break

    if finalKey is None:
        print("현재 네트워크에 사용되고 있는 패스워드를 찾지 못하였습니다!")
    else:
        print("지금 WiFi 비밀번호 : {}".format(finalKey))
        os.system("Pause")


if __name__ == "__main__":
    main()
