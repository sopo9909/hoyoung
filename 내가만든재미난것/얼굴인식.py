import cv2
import numpy as np
import os
from os import listdir
from os.path import isdir,isfile, join
from PIL import ImageFont, ImageDraw, Image
fontpath = "fonts/gulim.ttc"
font = ImageFont.truetype(fontpath, 20)
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
def face_extractor(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is ():#얼굴이 없으면 
        return None
    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h,x:x+w]
    return cropped_face
cap =cv2.VideoCapture(0,cv2.CAP_DSHOW)
enroll=input('얼굴을 등록하시겠습니까?(y/n)')
if enroll =='y':
    count =0
    name_hy = input('이름을 입력해주세요')
    if not os.path.exists('C:/Users/701/kdigital/lecture/K_digital_lecture/face/'+name_hy):
        os.makedirs('C:/Users/701/kdigital/lecture/K_digital_lecture/face/'+name_hy)
    ##이전에 찍은 것이 없을 때
        print('얼굴인식을 위해 사진을 찍겠습니다. 100장을 찍겠습니다.')
        while True:
            ret , frame = cap.read()
            if face_extractor(frame) is not None:
                print('얼굴을 좌우로 흔들어주세요'+str(100-count)+'장 남았습니다.')
                count += 1
                face = cv2.resize(face_extractor(frame),(200,200))
                face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                file_name_path = 'C:/Users/701/kdigital/lecture/K_digital_lecture/face/'+name_hy+'/user'+str(count)+'.jpg'
                cv2.imwrite(file_name_path,face)
                cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                cv2.imshow('Face Cropper',face)
            else:
                print("Face not Found")
                pass
            if cv2.waitKey(1)==13 or count==100:
                break
    ##이전에 찍은 것이 있을 때
    else:
        count=100
        print('얼굴인식을 위해 사진을 찍겠습니다. 100장을 찍겠습니다.')
        while True:
            ret , frame = cap.read()
            if face_extractor(frame) is not None:
                print('얼굴을 좌우로 흔들어주세요'+str(200-count)+'장 남았습니다.')
                count += 1
                face = cv2.resize(face_extractor(frame),(200,200))
                face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                file_name_path =  'C:/Users/701/kdigital/lecture/K_digital_lecture/face/'+name_hy+'/user'+str(count)+'.jpg'
                cv2.imwrite(file_name_path,face)
                cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                cv2.imshow('Face Cropper',face)
            else:
                print("Face not Found")
                pass
            if cv2.waitKey(1)==13 or count==200:
                break
    cap.release()
    cv2.destroyAllWindows()
    print('100장을 다 찍었습니다.')
def train(name_hy):
    data_path = 'C:/Users/701/kdigital/lecture/K_digital_lecture/face/'+name_hy+'/'
    face_pics = [f for f in listdir(data_path) if isfile(join(data_path,f))]
    Training_Data, Labels = [], []
    for i, files in enumerate(face_pics):
        image_path = data_path + face_pics[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if images is None:
            continue    
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
    if len(Labels) == 0:
        print("학습할 데이터가 없어요")
        return None
    Labels = np.asarray(Labels, dtype=np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(Training_Data), np.asarray(Labels))
    print(name_hy + " : 모델 학습이 완료되었어요!")
    return model
def trains():
    data_path = 'C:/Users/701/kdigital/lecture/K_digital_lecture/face/'
    model_dirs = [f for f in listdir(data_path) if isdir(join(data_path,f))]
    models = {}
    for model in model_dirs:
        print('model :' + model)
        result = train(model)
        if result is None:
            continue
        print('model2 :' + model)
        models[model] = result
    return models    
def face_detector(img, size = 0.5):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3,5)
        if faces is():
            return img,[]
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
            roi = img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (200,200))
        return img,roi  
def run(models):    
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        image, face = face_detector(frame)
        try:            
            min_score = 999       #가장 낮은 점수로 예측된 사람의 점수
            min_score_name = ""   #가장 높은 점수로 예측된 사람의 이름
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            for key, model in models.items():
                result = model.predict(face)                
                if min_score > result[1]:
                    min_score = result[1]
                    min_score_name = key       
            if min_score < 500:
                confidence = int(100*(1-(min_score)/300))
                display_string = str(confidence)+'% Confidence it is ' + min_score_name
            cv2.putText(image,display_string,(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)
            if confidence > 75:
                ###누구인지 확인되었을 때
                cv2.putText(image, " WHO : " + min_score_name, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Face Cropper', image)
            else:
                cv2.putText(image, " WHO ARE YOU", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Face Cropper', image)
        except:
            cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('Face Cropper', image)
            pass
        if cv2.waitKey(1)==13:
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    models = trains()
    run(models)