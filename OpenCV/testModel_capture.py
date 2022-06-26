import cv2
import win32com.client

class TestModel_capture3:
    def detect(cap, classifier, number_of_testID, scaleFactor, minNeighbors, color, listCLF, list_nameModel):
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        for (x, y, w, h) in features:
            for k in range(number_of_testID):
                id,con = listCLF[k].predict(gray[y:y+h, x:x+w])
                if con <= 100:
                    cv2.rectangle(cap, (x, y), (x+w, y+h), color, 2)
                    cv2.putText(cap, list_nameModel[k], (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(cap, str(int(con))+"%" ,(x, y+20+h), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    if(cv2.waitKey(1) & 0xFF == ord('s')):
                        speaker.Speak(list_nameModel[k])
                if (con < 100):
                    con = "{0}".format(round(100 - con))
                else:
                    con = "{0}".format(round(100 - con))
        return cap

class TestModel_capture2:
    def red_clf(cap, face_Cascade, listCLF, number_of_testID, list_nameModel):
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                frame = TestModel_capture3.detect(cap, face_Cascade, number_of_testID, 1.2, 5, (0,255,0), listCLF, list_nameModel)
                cv2.imshow('frame', frame)
                if(cv2.waitKey(1) & 0xFF == ord('q')):
                    break
            else:
                break
        return cap

class TestModel_capture:
    def set_testmodel(face_Model, number_of_testID):
        face_Cascade = cv2.CascadeClassifier("data_Model/"+face_Model+".xml")
        cap = cv2.VideoCapture(0)
        listID = []
        listCLF = []
        list_nameModel = []
        for i in range(number_of_testID):
            readFile = str(input("ModelFile : "))
            name_model = str(input("Name of Model : "))
            listID.append(readFile)
            list_nameModel.append(name_model)
        for j in range(number_of_testID):
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("data_Model/"+listID[j]+".xml")
            listCLF.append(clf)
        TestModel_capture2.red_clf(cap, face_Cascade, listCLF, number_of_testID, list_nameModel)
        cap.release()
        cv2.destroyAllWindows()

#face_Model = input("Face of model : ")
#number_of_testID = int(input("Number of Testmodel tested : "))
#TestModel_capture.set_testmodel(face_Model, number_of_testID)