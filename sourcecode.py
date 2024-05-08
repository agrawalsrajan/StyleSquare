import cvzone
import cv2
import os
from cvzone.PoseModule import PoseDetector
imgsz = (1280, 720)
cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
if type(imgsz) is tuple:
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, imgsz[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, imgsz[1])
detector=PoseDetector()
shirtpath="Shirts"
listShirts= os.listdir(shirtpath)
fixedratio=262/190
shirtratioheightwidth= 581/440

while True:
    success, img= cap.read()
    img = detector.findPose(img)
    img= cv2.flip(img,1)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)    
    if lmList:   
        center = bboxInfo["center"]
        cv2.circle(img, center, 0, (0.5, 0, 0.5), cv2.FILLED)
        ln11=lmList[11][1:3]
        ln12=lmList[12][1:3]
        imgShirt= cv2.imread(os.path.join(shirtpath,listShirts[1]), cv2.IMREAD_UNCHANGED)
        ShirtWidth=int((ln11[0]-ln12[0])*fixedratio)
        imgShirt=cv2.resize(imgShirt,(ShirtWidth, int(ShirtWidth*shirtratioheightwidth)),None,0.5,0.5)
        currentscale=(ln11[0]-ln12[0])/190
        offset= int(44*currentscale), int(48*currentscale)

        try:
          img= cvzone.overlayPNG(img,imgShirt,(ln12[0]-offset[0], ln12[1]-offset[1]))
        except:
           pass

    cv2.imshow("Image",img)
    cv2.waitKey(1)