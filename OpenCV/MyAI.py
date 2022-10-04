from keepData import KeepData
from createModel import CreateModel
from testModel_video import TestModel_video
from testModel_image import TestModel_image
from testModel_capture import TestModel_capture

# data collection process
start = str(input("start collecting data(yes/no) : "))
if start == "yes":
    face_model = input("detection model : ")
    id_numbertrain = int(input("number of videos trained : "))
    keep_folder = input("name of folder : ")
    KeepData.set_keepdata(face_model, id_numbertrain, keep_folder)

# Modeling process
start = str(input("start building(yes/no) : "))
if start == "yes":
    train_folder = str(input("select folder of train : "))
    crate_File = str(input("createname of testmodel : "))
    CreateModel.train_classifier(train_folder, crate_File)

# Model testing procedures
start = str(input("start testing(video/image/capture) : "))
if start == "video":
    # ทำงานเมื่อคำสั่งเป็น video
    face_Model = input("detection model : ")
    name_of_filevideo = input("name of testvideo : ")
    id_numbertrain = int(input("number of testmodel tested : "))
    TestModel_video.set_testmodel(face_Model, name_of_filevideo, id_numbertrain)
elif start == "image":
    # ทำงานเมื่อคำสั่งเป็น image
    face_Model = input("detection model : ")
    name_of_fileimage = input("name of testimage : ")
    id_numbertrain = int(input("number of testmodel tested : "))
    TestModel_image.set_testmodel(face_Model, name_of_fileimage, id_numbertrain)
elif start == "capture":
    # ทำงานเมื่อคำสั่งเป็น capture
    face_Model = input("detection model : ")
    id_numbertrain = int(input("number of testmodel tested : "))
    TestModel_capture.set_testmodel(face_Model, id_numbertrain)
