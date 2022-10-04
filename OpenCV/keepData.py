import cv2

class KeepData_2:
    def create_dataset(img, id_number, img_id, keep_folder):
        cv2.imwrite(str(keep_folder) + "/pic."+str(id_number) + "."+str(int(img_id/10)) + ".jpg", img)

    def draw_boundary(img, classifier, scale_factor, min_neighbors, color, text):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray, scale_factor, min_neighbors)
        coords = []
        for (axis_x, axis_y, wide, high) in features:
            cv2.rectangle(img, (axis_x, axis_y), (axis_x + wide, axis_y + high), color, 2)
            cv2.putText(img, text, (axis_x, axis_y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            coords = [axis_x, axis_y, wide, high]
        return img, coords

    def detect(img, face_cascade, img_id, che_id, keep_folder, id_number):
        img, coords = KeepData_2.draw_boundary(img, face_cascade, 1.2, 5, (0,0,255), "Face")
        if img_id == che_id:
            che_id += 10
            if len(coords) == 4 :
                result = img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
                KeepData_2.create_dataset(result, id_number, img_id, keep_folder)
        return img, che_id

class KeepData:
    def set_keepdata(faceModel, id_numbertrain, keep_folder):
        face_cascade = cv2.CascadeClassifier("data_Model/" + faceModel+".xml")
        list_file = []
        for loop_video in range(id_numbertrain):
            nameFile = input("Train video at {0} : ".format(loop_video+1))
            list_file.append(nameFile)
        for loop_read in range(id_numbertrain):
            id_number = loop_read + 1
            cap = cv2.VideoCapture("train_video/" + str(list_file[loop_read]) + ".mp4")
            img_id = 0
            che_id = 0
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    frame, che_id = KeepData_2.detect(frame, face_cascade, img_id, che_id, keep_folder, id_number)
                    cv2.imshow(str(keep_folder), frame)
                    img_id += 1
                    if(cv2.waitKey(1) & 0xFF == ord('q')):
                        break
                else:
                    break
        cap.release()
        cv2.destroyAllWindows()

#face_model = input("Face of model : ")
#id_numbertrain = int(input("Number of videos trained : "))
#keep_folder = input("Name of keepfolder : ")
#KeepData.set_keepdata(face_model, id_numbertrain, keep_folder)