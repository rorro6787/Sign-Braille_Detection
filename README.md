# Sign&Braille Language Detection

<div align="center">
  <p>
    <a href="https://github.com/ultralytics/assets/releases/tag/v8.2.0" target="_blank">
      <img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png" alt="YOLO Vision banner"></a>
  </p>
</div>

This repository contains code and resources for training a computer vision model using the YOLO (You Only Look Once) architecture to detect and recognize human hands forming various gestures in both Braille language and sign language. The project also includes functionality to translate these detected gestures into corresponding Braille or sign language interpretations and perform related processing and logic.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Dataset](#dataset)
- [Contributing](#contributing)

## Introduction

The goal of this project is to create a system that can automatically detect and track human hands forming gestures in both Braille language and sign language. The system is designed to recognize these gestures and accurately translate them into their corresponding Braille or sign language meanings. When the input image for our model includes hands displaying gestures, the system will interpret the gestures and provide the appropriate translation or feedback. This can be useful for educational purposes, accessibility tools, automated translation systems, and more.

## Features

- Detection and tracking of signs using YOLO
- Preprocessing and augmentation of training data
- Training scripts for custom YOLO models
- Evaluation scripts to assess model performance
- Inference the result of the game

## Requirements

- Python 3.x
- Ultralytics YOLOv8+

## Installation

1. Clone the repository:
   
    ```sh
    git clone https://github.com/yourusername/repository_name.git
    ```
3. Navigate to the project directory:
   
    ```sh
    cd repository_name
    ```
6. (Optional) Create a virtual environment:

   ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On macOS/Linux use 'python -m venv venv
                                                   source venv/bin/activate'
    ```

5. Select venv as your python interpreter (in VSC):
   
    ```sh
    > Python: Select Interpreter
    .\venv\Scripts\python.exe # On macOS/Linux use './venv/bin/python'
    ```
8. Install the required packages:
   
    ```sh
    pip install -r requirements.txt
    ```

7. If you want to do a pull request which implies adding more dependencias, remember to update the requirements file using:
   
    ```sh
    pip freeze > requirements.txt
    ```
    
## Dataset

The dataset should consist of video frames or images containing human hands forming various gestures in Braille and sign language, annotated with bounding boxes. You can use existing datasets, such as those available on the Roboflow platform, or manually annotate your own dataset. If you successfully train the model with your dataset, it can achieve accuracy comparable to ours in detecting and interpreting Braille and sign language gestures, similar to how our model tracks rock, paper, and scissors gestures.

## Contributors
- [![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/rorro6787) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/emilio-rodrigo-carreira-villalta-2a62aa250/) **Emilio Rodrigo Carreira Villalta**

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## Acknowledgements

- Inspired by various tutorials and resources on the YOLO documentation




