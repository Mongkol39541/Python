import cv2

class TestModel_image2:
    def detect(cap, classifier, id_numbertrain, scale_factor, minNeighbors, color, clf, list_namemodel):
        gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scale_factor, minNeighbors)
        for (axis_x, axis_y, wide, high) in features:
            for loop_pre in range(id_numbertrain):
                _, con = clf[loop_pre].predict(gray[axis_y : axis_y + high, axis_x : axis_x + wide])
                if con <= 100:
                    cv2.rectangle(cap, (axis_x, axis_y), (axis_x + wide, axis_y + high), color, 2)
                    cv2.putText(cap, list_namemodel[loop_pre], (axis_x, axis_y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(cap, str(int(con)) + "%",(axis_x, axis_y + 20 + high), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                if (con < 100):
                    con = "{0}".format(round(100 - con))
                else:
                    con = "{0}".format(round(100 - con))
        return cap

class TestModel_image:
    def set_testmodel(face_model, name_of_fileimage, id_numbertrain):
        face_cascade = cv2.CascadeClassifier("data_Model/" + face_model + ".xml")
        cap = cv2.imread("test_image/" + str(name_of_fileimage) + ".jpg")
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
            clf.read("data_Model/"+list_id[loop_read] + ".xml")
            list_clf.append(clf)
        TestModel_image2.detect(cap, face_cascade, id_numbertrain, 1.2, 5, (0,255,0), list_clf, list_namemodel)
        cv2.imshow('frame', cap)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#face_model = input("Face of model : ")
#name_of_fileimage = input("Name of Testimage : ")
#id_numbertrain = int(input("Number of Testmodel tested : "))
#TestModel_image.set_testmodel(face_model, name_of_fileimage, id_numbertrain)