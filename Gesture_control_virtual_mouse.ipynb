import cv2 as cv
import mediapipe
import pyautogui

capture_hands=mediapipe.solutions.hands.Hands()
drawing_options=mediapipe.solutions.drawing_utils
screen_width,screen_height=pyautogui.size()
camera= cv.VideoCapture(0)
x1 = y1 = x2 = y2 = x3 = y3 = 0
while True:
    _,image=camera.read()
    image_height,image_width,_=image.shape
    image=cv.flip(image,1)
    rgb_image=cv.cvtColor(image,cv.COLOR_BGR2RGB)
    output_hands=capture_hands.process(rgb_image)
    all_hands=output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_options.draw_landmarks(image,hand)
            one_hand_landmarks=hand.landmark
            for id,lm in enumerate(one_hand_landmarks):
                x=int(lm.x * image_width)
                y=int(lm.y * image_height)
                #print(x,y)
                if id == 8:
                    mouse_x = int(screen_width/image_width * x)
                    mouse_y = int(screen_height/image_height * y)
                    cv.circle(image,(x,y),12,(0,255,255))
                    pyautogui.moveTo(mouse_x,mouse_y)
                    x1 = x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y
                    cv.circle(image,(x,y),12,(0,255,255))
                if id == 12:
                    cv.circle(image,(x,y),12,(0,255,255))
                    x3 = x
                    y3 = y
                    
        dist = y2 - y1
        rclick = y3 - y1
        #print(dist)
        if(dist<20):
            pyautogui.click()
        if(rclick<5):
            pyautogui.click(button='right')
    cv2.imshow("Hand movement captured ",image)
    key = cv.waitKey(100)
    
    if key == 27:
        break
camera.release()
cv.destroyAllWindows()
