import cv2,time

video= cv2.VideoCapture("C://Users//Adwit//Desktop//Test.mp4")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

first_frame=None
a=0
while True:
    check,frame=video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)       #to make the frame captured gray
    gray=cv2.GaussianBlur(gray,(21,21),0)   #to make the motion detection  more efficient

    '''if first_frame is None :               #to capture the first frame
        first_frame= gray
        continue'''

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        resize_face = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('face detector activated',frame)
    a=a+1

    key = cv2.waitKey(1)  # every 1 millisecond it switches to a new frame , waitKey(0)is used to close the current frame at the moment user presses a key
    if key == ord('q'):
        break
print(a)


cv2.destroyWindow()
