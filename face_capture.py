import cv2
import os
import sys

def face_capture(user_id, NUM_IMGS=60, show_window=True):
    """capture face image

    Args:
        user_id (str): user id, primary key of user 
        NUM_IMGS (int, optional): Number of images to capture. Defaults to 60.
        show_window (bool, optional): Whether to show camera. Defaults to True.
    """
    faceCascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(0)
    if not os.path.exists('data'):
        os.mkdir('data')

    if not os.path.exists('data/{}'.format(user_id)):
        os.mkdir('data/{}'.format(user_id))

    cnt = 1
    while cnt <= NUM_IMGS:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        demo_frame = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(128, 128),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        # Draw a rectangle around the faces
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                demo_frame = cv2.rectangle(demo_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            x,y,w,h = faces[0]

            img = gray[y:y+h, x:x+w]
            img = cv2.resize(img, (128,128))
            cnt += 1
             # Store the captured images 
            cv2.imwrite("data/{}/{}{:03d}.jpg".format(user_id, user_id, cnt),img)
        # Display the resulting frame
        if show_window:
            cv2.imshow('Video', demo_frame)
        key = cv2.waitKey(50)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

def clear_capture(user_id):
    """clear captured faces given user id

    Args:
        user_id (str): user id, primary key of user 
    """    
    if os.path.exists('data/{}'.format(user_id)):
        list = os.listdir(f'data/{user_id}')
        for file in list:
            os.remove(f'data/{user_id}/{file}')
        os.rmdir(f'data/{user_id}')
    else :
        print("directory not exist")


if __name__ == '__main__':
    face_capture(sys.argv[1],30)
    #clear_capture('test')