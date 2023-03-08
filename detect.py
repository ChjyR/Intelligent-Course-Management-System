import numpy as np
import cv2
import pickle
import time

class Detector():
    def __init__(self,):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("model/train.yml")
        self.face_cascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
        with open("model/labels.pickle", "rb") as f:
            self.label_uid = pickle.load(f)
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    def detect(self, threshold=0.999, wait_time=10, show_camera=True, predict_info=True):
        """detect given face in a period of time

        Args:
            threshold (float, optional): How much confidence of the prediction. Defaults to 0.999.
            wait_time (int, optional): Time limit for detection. Defaults to 10.
            show_camera (bool, optional): open a camera window (for debugging). Defaults to True.
            predict_info (bool, optional): show predict info (for debugging). Defaults to True.

        Returns:
            str: user_id if predicted successful, "timeout" if timeout, "unknown" if predicted as unknown
        """    
        
        num_label = len(self.label_uid)
        coef_proir = np.ones(num_label+1)
        coef_proir /= np.sum(coef_proir)
        t_start = time.time()
        while True:
            ret, frame = self.cap.read()
            if not ret:
                cv2.waitKey(50)
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=10,
                minSize=(128, 128),
                flags=cv2.CASCADE_SCALE_IMAGE,
            )
            if len(faces) > 0:
                x,y,w,h = faces[0]
                img = gray[y:y+h, x:x+w]
                img = cv2.resize(img, (128,128))
                id, coef = self.recognizer.predict(img)
                coef -= 1e-5
                for i in range(num_label+1):
                    if i == id:
                        coef_proir[i] *= coef/100
                    else :
                        coef_proir[i] *= (1-coef/100)/num_label
                coef_proir /= np.sum(coef_proir)    #bayes law, update a posterior 

                process = np.log(1-np.max(coef_proir))/np.log(1-threshold)  #process of classification
                print(f"({process*100:.2f}%)\t",end='\n')

                if predict_info:
                    for i in range(num_label):
                        print(f"[user {i}] coef={coef_proir[i]:.3f}\t",end="")
                    print(f"[unknown] coef={coef_proir[-1]:.3f}",end="")
                
                if process > 1:
                    pred_id = np.argmax(coef_proir)
                    self.cap.release()
                    cv2.destroyAllWindows()   
                    if pred_id == num_label: 
                        return "unknown"            #predict as unknown face
                    else :                      
                        return self.label_uid[pred_id]   #predict as certain user_id
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                
            if show_camera:
                cv2.imshow('Video',frame)
            cv2.waitKey(50)
                
            if time.time() - t_start > 10:
                break
        self.cap.release()
        cv2.destroyAllWindows()
        return "timeout"    #time out return

if __name__ == "__main__":
    detector = Detector()
    detector.detect(0.999)