import cv2

class TestModel_capture3:
    def detect(cap, classifier, id_numbertrain, scale_factor, min_neighbors, color, clf, list_namemodel):
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scale_factor, min_neighbors)
        listcon = []
        for (axis_x, axis_y, wide, high) in features:
            for loop_pre in range(id_numbertrain):
                _, con = clf[loop_pre].predict(gray[axis_y : axis_y + high, axis_x : axis_x + wide])
                listcon.append(int(con))
            arr = [listcon,list_namemodel]
            con = max(listcon)
            for loop_che in range(id_numbertrain):
                if arr[0][loop_che] == con:
                    nameModel = arr[1][loop_che]
            if con <= 100:
                cv2.rectangle(cap, (axis_x, axis_y), (axis_x + wide, axis_y + high), color, 2)
                cv2.putText(cap, nameModel, (axis_x, axis_y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                cv2.putText(cap, str(int(con)) + "%", (axis_x, axis_y + 20 + high), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        return cap

class TestModel_capture2:
    def red_clf(cap, face_cascade, clf, id_numbertrain, list_namemodel):
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                frame = TestModel_capture3.detect(frame, face_cascade, id_numbertrain, 1.2, 5, (0,255,0), clf, list_namemodel)
                cv2.imshow('frame', frame)
                if(cv2.waitKey(1) & 0xFF == ord('q')):
                    break
            else:
                break
        return cap

class TestModel_capture:
    def set_testmodel(face_model, id_numbertrain):
        face_cascade = cv2.CascadeClassifier("data_Model/"+face_model+".xml")
        cap = cv2.VideoCapture(0)
        list_id = []
        list_clf = []
        list_namemodel = []
        for _ in range(id_numbertrain):
            readFile = str(input("ModelFile : "))
            name_model = str(input("Name of Model : "))
            list_id.append(readFile)
            list_namemodel.append(name_model)
        for list_read in range(id_numbertrain):
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("data_Model/" + list_id[list_read] + ".xml")
            list_clf.append(clf)
        TestModel_capture2.red_clf(cap, face_cascade, list_clf, id_numbertrain, list_namemodel)
        cap.release()
        cv2.destroyAllWindows()

#face_model = input("Face of model : ")
#id_numbertrain = int(input("Number of Testmodel tested : "))
#TestModel_capture.set_testmodel(face_model, id_numbertrain)