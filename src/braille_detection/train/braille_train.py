import cv2
import os
import sys
from ultralytics import YOLO
import shutil
import random
from zipfile import ZipFile
import gdown
import zipfile

cd = os.getcwd()

def train_model(yaml_file, epochs, project):
    """
    Trains the YOLO model on the provided dataset and saves the training metrics.

    Args:
        yaml_file (str): Path to the YOLO configuration YAML file.
        epochs (int): Number of training epochs.
        project (str): Path to the project directory where the training results will be saved.
    """

    model = YOLO(model="yolov8n.pt", task="detect")
    model.to('cuda')
    model.train(data = yaml_file,
        	  epochs = epochs,
              project = project,
        	  batch = 8,
              name = "train")          # batch = 8 is neccesary because GPU does not support higher

    results2 = model.val(data = yaml_file,
                        project = project,
                        batch = 8,
                        name = "test",
                        split = "test")

    # Crear la ruta completa para el archivo de texto
    metrics_file_path2 = os.path.join(project, "testing_metrics.txt")

    # Escribir las métricas en el archivo de texto
    with open(metrics_file_path2, 'w') as f:
        f.write("Another metrics:\n")
        f.write(" Average precision for all classes: {}\n".format(results2.box.all_ap))
        f.write(" Average precision: {}\n".format(results2.box.ap))
        f.write(" Average precision at IoU=0.50: {}\n".format(results2.box.ap50))
        f.write(" F1 score: {}\n".format(results2.box.f1))
        f.write(" Mean average precision: {}\n".format(results2.box.map))
        f.write(" Mean average precision at IoU=0.50: {}\n".format(results2.box.map50))
        f.write(" Mean average precision at IoU=0.75: {}\n".format(results2.box.map75))
        f.write(" Mean average precision for different IoU thresholds: {}\n".format(results2.box.maps))
        f.write(" Mean precision: {}\n".format(results2.box.mp))
        f.write(" Mean recall: {}\n".format(results2.box.mr))
        f.write(" Precision: {}\n".format(results2.box.p))
        f.write(" Precision values: {}\n".format(results2.box.prec_values))
        f.write(" Recall: {}\n".format(results2.box.r))

def main():
    import gdown
    url = 'https://drive.google.com/uc?export=download&id=1zrs5J8MXCt39mTKeYxcop0pTYIml_7Fb'
    gdown.download(url,"braille.zip",quiet=False)

    ruta_zip = cd + '/braille.zip'
    ruta_destino = cd + str('/braille_dataset')
    os.makedirs(ruta_destino, exist_ok=True)

    with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
        zip_ref.extractall(ruta_destino)

    print("Descompresión completa.")

    # train_model(cd + "/sign_dataset/data.yaml",32,"Sign_Language_Detection_Model")

if __name__ == "__main__":
    main()
