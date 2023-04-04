from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import numpy as np
import cv2 as CV
import cyberpi

#-------------- COMPUTER VISION --------------#

def takeFoto():
    with PiCamera() as camera:
        camera.resolution = (640, 480)
        foto = PiRGBArray(camera, size=(640,480))
        sleep(1)
        camera.capture(foto, format='bgr')
        return foto.array

def getCircles(image):
    grayFrame = CV.cvtColor(image, CV.COLOR_BGR2GRAY)
    blurredFrame = CV.GaussianBlur(grayFrame, (9,9), 2)
    circles = CV.HoughCircles(blurredFrame, CV.HOUGH_GRADIENT, 1.2, 100, param1=50, param2=32, minRadius=20, maxRadius=250)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

    return circles

def LargestCircle(circles):
    if len(circles) == 0: return None
    return max(circles, key=lambda c: c[2])

@cyberpi.event.is_press("a")
def rescueBalls():
    foto = takeFoto()
    circles = getCircles(foto)
    TargetBall = LargestCircle(circles)
    for circle in circles:
        x, y, r = circle
        CV.circle(foto, (x,y),r,(0,255,0),2)
    if TargetBall is not None:
        x, y, r = TargetBall
        CV.circle(foto, (x,y),r,(255,0,0),4)
        
        
#------------------ CYBERPI -----------------#

def move(left, right):
    cyberpi.mbot2.drive_power(left*-1, right)

def stop():
    cyberpi.mbot2.EM_stop()

@cyberpi.event.is_press("b")
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

