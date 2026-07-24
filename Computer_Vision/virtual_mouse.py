def v_mouse():
    import cv2
    import numpy as np
    import time
    from Computer_Vision import hand_tracker as ht
    import autopy 
    import pyautogui  

    ### Variables Declaration
    pTime = 0  # Used to calculate frame rate
    width = 640  # Width of Camera
    height = 480  # Height of Camera
    frameR = 100  # Frame Rate
    smoothening = 8  # Smoothening Factor
    prev_x, prev_y = 0, 0  # Previous coordinates
    curr_x, curr_y = 0, 0  # Current coordinates

    cap = cv2.VideoCapture(0) #CAMERA INDEX ID NUMBER OR TEST VIDEO FILE PATH
    cap.set(3, width)  # Adjusting size
    cap.set(4, height)

    detector = ht.handDetector(maxHands=1)  # Detecting one hand at max
    screen_width, screen_height = autopy.screen.size()  # Getting the screen size
    screenshot_path = 'G:\SPARC\DataBase\images\screenshot.png'  # Path to save screenshot

    while True:
        success, img = cap.read()
        img = detector.findHands(img)  # Finding the hand
        lmlist, bbox = detector.findPosition(img)  # Getting position of hand
        if len(lmlist) != 0:
            x1, y1 = lmlist[8][1:]  # Index finger tip
            x2, y2 = lmlist[12][1:]  # Middle finger tip
            x3, y3 = lmlist[16][1:]  # Ring finger tip
            x4, y4 = lmlist[20][1:]  # Pinky finger tip
            fingers = detector.fingersUp()  # Checking if fingers are upwards
            cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255),
                          2)  # Creating boundary box
            if fingers[1] == 1 and fingers[2] == 0:  # If fore finger is up and middle finger is down
                x3_inter = np.interp(x1, (frameR, width - frameR), (0, screen_width))
                y3_inter = np.interp(y1, (frameR, height - frameR), (0, screen_height))
                curr_x = prev_x + (x3_inter - prev_x) / smoothening
                curr_y = prev_y + (y3_inter - prev_y) / smoothening
                autopy.mouse.move(screen_width - curr_x, curr_y)  # Moving the cursor
                cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
                prev_x, prev_y = curr_x, curr_y
            # Check if both middle and ring fingers are raised and close
            if fingers[2] == 1 and fingers[3] == 1:
                length, img, lineInfo = detector.findDistance(12, 16, img)
                if length < 40:  # If both fingers are close to each other
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click(autopy.mouse.Button.RIGHT)  # Right Click action
            # If fore finger & middle finger both are up
            if fingers[1] == 1 and fingers[2] == 1:
                length, img, lineInfo = detector.findDistance(8, 12, img)
                if length < 40:     # If both fingers are really close to each other
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()
            # If all five fingers are raised, take a screenshot
            if fingers == [1, 1, 1, 1, 1]:  # All fingers up
                pyautogui.screenshot(screenshot_path)  # Taking a screenshot
                cv2.putText(img, "Screenshot Taken", (200, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
