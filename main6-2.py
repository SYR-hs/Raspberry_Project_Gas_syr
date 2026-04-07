from gpiozero import Buzzer, DigitalInputDevice
import time

bz = Buzzer(18)
gas = DigitalInputDevice(17)

try:
    while True:
        if gas.value == 0:       # 0 = 가스 감지 (LOW) -> 평상시에 1(High)을 유지하다가 가스를 감지하면 0(Low) 신호를 내보내는 Active Low 방식으로 작동.
                                 # 0일 때 "가스 감지됨"이라고 판단.
            print("가스 감지됨")
            bz.on()              # 가스 감지시 부저 작동 on
        else:                    # 1 = 정상 (HIGH)
            print("정상")
            bz.off()             # 가스 미감지시 부저 작동 off

        time.sleep(0.2)

except KeyboardInterrupt:
    pass

bz.off()
