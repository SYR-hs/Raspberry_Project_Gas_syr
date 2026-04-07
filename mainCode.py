from gpiozero import Buzzer, DigitalInputDevice
import time

bz = Buzzer(18)                  # 변수 지정 및 부저 클래스를 사용하여 GPIO 18번 핀에 부저를 연결.
gas = DigitalInputDevice(17)     # 가스 센서의 디지털출력핀(DO)을 GPIO 17번에 연결. 센서의 상태를 0 또는 1로 읽어옴.

try:
    while True:
        if gas.value == 0:       # 0 = 가스 감지 (LOW) -> 평상시에 1(High)을 유지하다가 가스를 감지하면 0(Low) 신호를 내보내는 Active Low 방식으로 작동.
                                 # 0일 때 "가스 감지됨"이라고 판단.
            print("가스 감지됨")
            bz.on()              # 가스 감지시 부저 작동 on
        else:                    # 1 = 정상 (HIGH)
            print("정상")
            bz.off()             # 가스 미감지시 부저 작동 off

        time.sleep(0.2)          # time.sleep 함수를 통해 0.2초(200ms) 프로그램 동작을 멈춤으로서 센서의 값 출력 속도를 조절.

except KeyboardInterrupt:        # 프로그램 종료 시 부저 작동 off
    pass

bz.off()
