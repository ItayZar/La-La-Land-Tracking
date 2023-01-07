import cv2
import imutils
import numpy as np
import argparse

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect(frame):
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(8, 8),padding=(16,16) ,scale=1.03)
    indices = cv2.dnn.NMSBoxes(bounding_box_cordinates, weights, 0.1, 0.8)
    bboxes = [bounding_box_cordinates[i] for i in indices]
    bboxes = sorted(bboxes, key=lambda x: x[3], reverse=True)
    bboxes=bboxes[:2]
    labels = [weights[i] for i in indices]

    person = 1
    for x, y, w, h in bboxes:
        if person == 1:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            person += 1
        elif person == 2:
            #for x, y, w, h in bounding_box_cordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,20,147), 2)
            cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            person +=1

    return frame


def detectByPathVideo():
    video = cv2.VideoCapture('La La Land low.avi')
    check, frame = video.read()
    if check == False:
        print('Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided).')
        return
    print('Detecting people...')
    while video.isOpened():
        # check is True if reading was successful
        check, frame = video.read()
        if check:
            frame = imutils.resize(frame,width=min(800, frame.shape[1]))
            frame = detect(frame)
            cv2.imshow("Frame", frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()


detectByPathVideo()
