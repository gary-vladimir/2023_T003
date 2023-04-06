#from picamera.array import PiRGBArray
from picamera2 import Picamera2
from time import sleep
import numpy as np
import cv2 as CV
import cyberpi
from robot import Robot
from PIL import Image

#-------------- COMPUTER VISION --------------#
cam = Picamera2()
config = cam.create_still_configuration()
cam.configure(config)

def takeFoto():
    print("starting foto shoot! ")
    cam.start() 
    sleep(2) 
    cam.capture_file("raw.jpg")
    print("done")
    image = Image.open("raw.jpg")
    resized = image.resize((686,378))
    resized.save('foto.jpg')
    return CV.imread("foto.jpg")


def getCircles(image):
    print("finding circles")
    grayFrame = CV.cvtColor(image, CV.COLOR_BGR2GRAY)
    blurredFrame = CV.GaussianBlur(grayFrame, (9,9), 2)
    circles = CV.HoughCircles(blurredFrame, CV.HOUGH_GRADIENT, 1, 100, param1=30, param2=25, minRadius=10, maxRadius=100)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
    print("return circles")
    return circles


def showBalls(image, circles):
    print("procesing circles")
    closestBall = None
    if circles is not None:
        for circle in circles:
            if closestBall == None or closestBall.r < circle.r: closestBall = circle
            x, y, r = circle
            CV.circle(image, (x,y),r,(0,255,0),2)
    CV.circle(image, (closestBall.x, closestBall.y), closestBall.r, (255,0,0),2)
    CV.imwrite('processed.jpg', image)
    print("processed.jpg done")

"""

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
        
"""

#------------------ CYBERPI -----------------#

robot = Robot()

def initRobot():
    robot.startRobot()

@cyberpi.event.is_press("a") # square
def rescueBalls():
    print("square button pressed")
    foto = takeFoto()
    circles = getCircles(foto)
    showBalls(foto, circles)

@cyberpi.event.is_press("b") # triangle
def followLine():
    print("triangle button pressed")
    KD = 15
    KP = 70
    SPEED = 80
    POS = 0
    PreviousPOS = 0
    PreviousError = 0
    while(True):
        lineStatus = robot.lineFollowerRead()
        s1 = 0 if (lineStatus & (1 << 3)) == 0 else 1
        s2 = 0 if (lineStatus & (1 << 2)) == 0 else 1
        s3 = 0 if (lineStatus & (1 << 1)) == 0 else 1
        s4 = 0 if (lineStatus & (1 << 0)) == 0 else 1
        if(not s1 and not s2 and not s3 and not s4):
            #robot.move(80,80)
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
        print(SPEED+P+D, SPEED - P + D)
        #robot.move(SPEED + P + D, SPEED - P + D)
        PreviousError=error 
    robot.stop()

@cyberpi.event.is_press("down")
def lowerClaw():
    robot.LowerClaw()

@cyberpi.event.is_press("left")
def openClaw():
    robot.openClaw()

@cyberpi.event.is_press("right")
def closeClaw():
    robot.closeClaw()

cyberpi.event.start(callback=initRobot)