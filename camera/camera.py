from picamera import PiCamera, Color
from time import sleep

def showPreview(sec):
    # Displays RPi camera preview for sec seconds
    # Only works when the RPi is connected to a monitor

    camera = PiCamera()

    camera.start_preview(alpha=150)
    sleep(sec)
    camera.stop_preview()

def takePicture(sec):
    # Displays RPi camera preview for "sec" seconds and then saves photo to "path"
    # Only displays preview when the RPi is connected to a monitor

    path = "/home/pi/Desktop/image.jpg" #Saves "image.jpg" to Desktop
    camera = PiCamera()

    camera.start_preview(alpha=150)

    # Add annotation to image and set styling. Also lots of other configuration within camera, but may not be that important to RSX
    # camera.annotate_background = Color('blue')
    # camera.annotate_foreground = Color('yellow')
    camera.annotate_text = "Annotation"
    camera.annotate_text_size = 160

    sleep(sec)
    camera.capture(path)
    camera.stop_preview()

def recordVideo(sec):
    # Displays RPi camera preview for "sec" seconds and then saves photo to "path"
    # Only displays preview when the RPi is connected to a monitor

    path = "/home/pi/Desktop/video.h264" #Saves "image.jpg" to Desktop
    camera = PiCamera()

    camera.start_preview(alpha=150)
    camera.start_recording(path)
    sleep(sec)
    camera.stop_recording()
    camera.stop_preview()

if __name__ == "__main__":
    # showPreview(2)
    takePicture(3)
    # recordVideo(3)

    # https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
    # Tutorial for RPi camera and Open CV