# @author: gitUmaru
import os
import zipfile
import random
from shutil import copyfile
from tqdm import tqdm


DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + '\\'

def split_data(IM_SOURCE, MA_SOURCE, SPLIT_SIZE):
    """
    Function to split data from IM_SOURCE into its respective TRAING and TESTING directories using the desired SPLIT_SIZE
    @param: IM_SOURCE - path to IM_SOURCE dataset folder as String
            TRAINING - path to training folder as String
            TESTING - path to testing fodler as String
            SPLIT_SIZE - percentage of IM_SOURCE data that will become training as int
    @output: void - Sorted file structure ready for tf.keras.preprocessing.image.ImageDataGenerator
    """

    ## shuffle your data and define desired size of train and test data
    data = random.sample(os.listdir(IM_SOURCE),len(os.listdir(IM_SOURCE)))
    SIZE = len(data)

    for i in tqdm(range(SIZE)):
        if(i < round(SPLIT_SIZE*SIZE)):
            copyfile(IM_SOURCE+data[i],TRAINING_im_DIR+data[i])
            copyfile(MA_SOURCE+data[i].split('.jpg')[0]+'_Segmentation.png',TRAINING_ma_DIR+data[i])
        else:
            copyfile(IM_SOURCE+data[i],TESTING_im_DIR+data[i])
            copyfile(MA_SOURCE+data[i].split('.jpg')[0]+'_Segmentation.png',TESTING_ma_DIR+data[i])

def make_file_struct(ROOT,CLASS1, CLASS2):
    """
    Fuction that makes the desired file structure
    @param: ROOT - name of root directory as a String
            CLASS1 - name of first label as a String
            ClASS2 - name of second label as a String
    @output: void - New file structure (relateive to project folder)
    """
    try:
        os.mkdir(DIR_PATH + f'{ROOT}\\')
        os.mkdir(DIR_PATH + f'{ROOT}\\train_{CLASS1}\\')
        os.mkdir(DIR_PATH + f'{ROOT}\\test_{CLASS1}\\')
        os.mkdir(DIR_PATH + f'{ROOT}\\train_{CLASS2}\\')
        os.mkdir(DIR_PATH + f'{ROOT}\\test_{CLASS2}\\')
    except OSError:
        print("There was an OS error, either import os or the directory already exists")
        print(OSError)
        pass

if __name__ == '__main__':
    ROOT = "dataset"
    CLASS1 = "im"
    CLASS2 = "ma"

    make_file_struct(ROOT,CLASS1, CLASS2)

    im_DIR = DIR_PATH + "images\\"
    TRAINING_im_DIR = DIR_PATH + f'{ROOT}\\train_{CLASS1}\\'
    TESTING_im_DIR = DIR_PATH + f'{ROOT}\\test_{CLASS1}\\'

    ma_DIR = DIR_PATH + "masks\\"
    TRAINING_ma_DIR = DIR_PATH + f'{ROOT}\\train_{CLASS2}\\'
    TESTING_ma_DIR = DIR_PATH + f'{ROOT}\\test_{CLASS2}\\'

    split_size = 0.8
    split_data(im_DIR, ma_DIR, split_size)
