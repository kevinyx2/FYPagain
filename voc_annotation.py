import os
import argparse
import xml.etree.ElementTree as ET

def convert_voc_annotation(data_path, data_type, anno_path, use_difficult_bbox=True):

    classes = ['sell', 'buy']
    img_inds_file = os.path.join(data_path, 'images', data_type + '.txt')
    with open(img_inds_file, 'r') as f:
        txt = f.readlines()
        image_inds = [line.strip() for line in txt]

    with open(anno_path, 'a') as f:
        for image_ind in image_inds:
            image_path = os.path.join(data_path, image_ind + '.jpg')
            annotation = image_path
            label_path = os.path.join(data_path, 'images/Annotation', image_ind + '.xml')
            root = ET.parse(label_path).getroot()
            objects = root.findall('object')
            for obj in objects:
                difficult = obj.find('difficult').text.strip()
                if (not use_difficult_bbox) and(int(difficult) == 1):
                    continue
                bbox = obj.find('bndbox')
                class_ind = classes.index(obj.find('name').text.lower().strip())
                #if class_ind == 'buy':
                    #int buycount +1
                    #print('buy' + buycount)
                #if class_ind == 'sell':
                    #int sellcount +1
                    #print('sell' + sellcount)
                xmin = bbox.find('xmin').text.strip()
                xmax = bbox.find('xmax').text.strip()
                ymin = bbox.find('ymin').text.strip()
                ymax = bbox.find('ymax').text.strip()
                annotation += ' ' + ','.join([xmin, ymin, xmax, ymax, str(class_ind)])
            print(annotation)
            newannonation = annotation[74:]
            print(newannonation)
            f.write(newannonation + "\n")
    return len(image_inds)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", default="/Users/user/Downloads/tensorflow_yolo_v3-master/tensorflow_yolo_v3-master/training_data/")
    parser.add_argument("--train_annotation", default="/Users/user/Downloads/tensorflow_yolo_v3-master/tensorflow_yolo_v3-master/training_data/images/voc_train.txt")
    parser.add_argument("--test_annotation",  default="./data/dataset/voc_test.txt")
    flags = parser.parse_args()

    if os.path.exists(flags.train_annotation):os.remove(flags.train_annotation)
    if os.path.exists(flags.test_annotation):os.remove(flags.test_annotation)

    num1 = convert_voc_annotation(os.path.join(flags.data_path), 'trainval', flags.train_annotation, False)
    
