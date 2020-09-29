file1 = open("C:/Users/user/Downloads/tensorflow_yolo_v3-master/tensorflow_yolo_v3-master/training_data/images/trainval.txt", "a")

for x in range(2003):
    file1.write("img" + str(x+1) + "\n")

file1.close()


#for x in range(80):
    #y = 'img'
    #y += x
