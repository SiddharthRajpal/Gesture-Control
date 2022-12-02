import webbrowser
import cv2 as cv
import pyautogui
from cvzone.HandTrackingModule import HandDetector
from time import sleep
cap = cv.VideoCapture(1)
detector = HandDetector(maxHands= 2, detectionCon= 0.8, minTrackCon=0.8)
while True:
    _, frame = cap.read()
    hands , img = detector.findHands(frame)
    if hands:
        
        
        left = hands[0]
        lmlist = left['lmList']
        center = left['center']
        bbox = left['bbox']
        fingers = detector.fingersUp(left)
        print(fingers)
        
        length, info, img = detector.findDistance(lmlist[4][0:2], lmlist[8][0:2],img)
        cv.putText(color = (0,0,0), text = str(int(length)),fontFace= cv.FONT_ITALIC, fontScale= .5, img = img, org= (lmlist[4][0], lmlist[4][1]))
        if len(hands)==2:
            right = hands[1]
            center2 = right['center']
            cv.putText(color = (0,0,0), text = str(int(length)),fontFace= cv.FONT_ITALIC, fontScale= .5, img = img, org= (center[0],center2[1]))
            length2, info2, img = detector.findDistance(center,center2,img)
            if length2 < 80:
                pyautogui.hotkey("win","r")
                thginie = r"C:\Users\siddh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk"
                pyautogui.write(thginie)
                pyautogui.press("enter")
                sleep(2)
                


        if(fingers == [1,0,1,0,0] or fingers == [1,1,0,0,1]):
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            sleep(2)
        if(fingers == [1,0,1,1,1] and length<20):
            webbrowser.open("https://github.com/microsoft/PowerToys")
            sleep(2)
        if(fingers == [0,0,0,0,1]):
            pyautogui.press("volumedown")
        if(fingers == [1,0,0,0,1]):
            pyautogui.press("volumeup")
            
    cv.imshow("Finale", img)
    key = cv.waitKey(5)
    if key == 27:
        break
