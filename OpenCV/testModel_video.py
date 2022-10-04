import cv2

class TestModel_video4:
    def draw_boundary(video, classifier, id_numbertrain, scaleFactor, minNeighbors, color, clf, list_namemodel):
        gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
        for (axis_x, axis_y, wide, high) in features:
            for loop_pre in range(id_numbertrain):
                _, con = clf[loop_pre].predict(gray[axis_y : axis_y + high, axis_x : axis_x + wide])
                if con <= 100:
                    cv2.rectangle(video, (axis_x, axis_y), (axis_x + wide, axis_y + high), color, 2)
                    cv2.putText(video, list_namemodel[loop_pre], (axis_x, axis_y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(video, str(int(con)) + "%",(axis_x, axis_y + 20 + high), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                if (con < 100):
                    con = "{0}".format(round(100 - con))
                else:
                    con = "{0}".format(round(100 - con))
        return video

class TestModel_video3:
    def detect(video, face_cascade, id_numbertrain, clf, list_namemodel):
        video = TestModel_video4.draw_boundary(video, face_cascade, id_numbertrain, 1.2, 5, (0,255,0), clf, list_namemodel)
        return video

class TestModel_video2:
    def red_clf(video, face_cascade, clf, id_numbertrain, list_namemodel):
        while(video.isOpened()):
            ret, frame = video.read()
            if ret == True:
                frame = TestModel_video3.detect(frame, face_cascade, id_numbertrain, clf, list_namemodel)
                cv2.imshow('frame', frame)
                if(cv2.waitKey(1) & 0xFF == ord('q')):
                    break
            else:
                break
        return video

class TestModel_video:
    def set_testmodel(face_model, name_of_filevideo, id_numbertrain):
        face_cascade = cv2.CascadeClassifier("data_Model/"+face_model+".xml")
        video = cv2.VideoCapture("test_video/"+str(name_of_filevideo)+".mp4")
        list_id = []
        list_clf = []
        list_namemodel = []
        for _ in range(id_numbertrain):
            readFile = str(input("ModelFile : "))
            name_model = str(input("Name of Model : "))
            list_id.append(readFile)
            list_namemodel.append(name_model)
        for loop_read in range(id_numbertrain):
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("data_Model/"+list_id[loop_read]+".xml")
            list_clf.append(clf)
        TestModel_video2.red_clf(video, face_cascade, list_clf, id_numbertrain, list_namemodel)
        video.release()
        cv2.destroyAllWindows()

#face_model = input("Face of model : ")
#name_of_filevideo = input("Name of Testvideo : ")
#id_numbertrain = int(input("Number of Testmodel tested : "))
#TestModel_video.set_testmodel(face_model, name_of_filevideo, id_numbertrain)