from cvzone.HandTrackingModule import HandDetector
import cv2
import serial
import time

#Defining arduino parameters
arduino = serial.Serial('COM7',9600)

# Parameters
width, height = 1280, 720
gestureThreshold = 300


# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand Detector
detectorHand = HandDetector(detectionCon=0.8, maxHands=1)
speaker_pin = 3  

hs, ws = int(120 * 1), int(213 * 1)  
buttonPressed = False

while True:
    success, img = cap.read()

   
    hands, img = detectorHand.findHands(img)  
   

    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 0, 0), 3)
    
    if hands and buttonPressed is False:  

        hand = hands[0]
        cx, cy = hand["center"]
        lmList = hand["lmList"] 
        fingers = detectorHand.fingersUp(hand) 

    
        if cy <= gestureThreshold: 
            if fingers == [1, 1, 1, 1, 1]:
                cv2.putText(img,"Turn On light",(50, 50),cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 0),2,cv2.LINE_AA )
                
                arduino.write(str.encode('1'))
                
            elif fingers == [0, 0, 0, 0, 0]:
                cv2.putText(img,"Turn off light",(50, 50),cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 0),2,cv2.LINE_AA )
                arduino.write(str.encode('0'))
                
                
                
            elif fingers == [0, 1, 0, 0, 0]:
                cv2.putText(img,"Speaker on",(50, 50),cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 0),2,cv2.LINE_AA )
                arduino.write(str.encode('3'))
                

            elif fingers == [0,1,1,0,0]:
                cv2.putText(img,"Speaker off",(50, 50),cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 0),2,cv2.LINE_AA )
                arduino.write(str.encode('4'))
            elif fingers == [0,1,1,1,0]:
                cv2.putText(img,"Increase VOl",(50, 50),cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 0),2,cv2.LINE_AA )
            elif fingers == [0,1,1,1,1]:
                cv2.putText(img,"Decrease VOl",(50, 50),cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 0),2,cv2.LINE_AA )


    cv2.imshow("Output", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break