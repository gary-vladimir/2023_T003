from time import sleep
import cyberpi

def move(left, right):
    cyberpi.mbot2.drive_power(left*-1, right)

def stop():
    cyberpi.mbot2.EM_stop()

@cyberpi.event.is_press("left")
def followLine():
    KD = 15
    KP = 70
    SPEED = 80
    POS = 0
    PreviousPOS = 0
    PreviousError = 0
    while(True):
        lineStatus = cyberpi.quad_rgb_sensor.get_line_sta(index=1)
        s1 = 0 if (lineStatus & (1 << 3)) == 0 else 1
        s2 = 0 if (lineStatus & (1 << 2)) == 0 else 1
        s3 = 0 if (lineStatus & (1 << 1)) == 0 else 1
        s4 = 0 if (lineStatus & (1 << 0)) == 0 else 1
        if(not s1 and not s2 and not s3 and not s4):
            move(80,80)
            continue
        suma = s1 + s2*3 + s3*5 + s4*7
        pesos = s1 + s2 + s3 + s4
        if(pesos > 0):
            POS = suma/pesos
            PreviousPOS = POS
        else:
            POS = PreviousPOS
        error = POS-4
        P = KP*error
        D = KD * (error-PreviousError) 
        move(SPEED + P + D, SPEED - P + D)
        PreviousError=error
    stop()

