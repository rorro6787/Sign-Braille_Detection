import cv2
import os
import sys
from ultralytics import YOLO
import shutil
import random
from zipfile import ZipFile
import gdown
import time

cd = os.getcwd()
model = YOLO(os.path.join(cd, 'best.pt'))

def inference_over_image(sourcePath):
    results = model(sourcePath, save = True, project=os.path.join(cd, 'predictions'))
    print("Image in path:" + sourcePath + " analysed")

def main():
    if len(sys.argv) == 3 and 'ii' in sys.argv:
        if sys.argv[-1].startswith("--source="):
            # Remove "--source=" prefix
            sourcePath = sys.argv[-1][9:]
            inference_over_image(sourcePath)
        else:
            # Handle invalid argument format
            print(f"Invalid argument format: {sys.argv[-1]}  :( Expected format: --source=sourcePath...")

if __name__ == "__main__":
    main()    