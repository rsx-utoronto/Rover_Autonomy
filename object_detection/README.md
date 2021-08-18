# Object Detection using TensorFlow 2 API
Using a pre-trained Faster R-CNN model for the purpose of object detection.

Implemented with the use of the [TensorFlow 2 Object Detection API](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md).

The code has been adapted from the [TensorFlow 2 Object Detection API tutorial](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/auto_examples/object_detection_camera.html).

## Installation
Navigate to the desired directory for installation and clone the TensorFlow Models repository.
```bash
git clone https://github.com/tensorflow/models.git
```

### Python Package Installation
```bash
cd models/research
protoc object_detection/protos/*.proto --python_out=.
cp object_detection/packages/tf2/setup.py .
python3 -m pip install --use-feature=2020-resolver .
```

### Download Detection Script
Clone the **Rover_Autonomy** repository in a desired directory and navigate to the **object_detection** folder. Create a copy of **object_detection.py** and move it into your **research** folder from the package installation step.

## Tweaks

### Model Selection
The pre-trained detection model can be switched out for any model provided in the [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md).

Right-click on the desired model and copy the link. Paste it into the search bar without hitting enter. Replace **MODEL_DATE** and **MODEL_NAME** as shown below with the date and name of the model found in the copied link.

![Imgur](https://i.imgur.com/9NLwRUM.png)

### Threshold
The threshold can be adjusted so that detection is stricter. Change **min_score_thresh** to the desired value.

![Imgur](https://i.imgur.com/AJim0It.png)