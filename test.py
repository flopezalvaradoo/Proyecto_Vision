import cv2
from picamera2 import Picamera2

def stream_video():
    picam = Picamera2()
    picam.preview_configuration.main.size=(320, 180)
    picam.preview_configuration.main.format="RGB888"
    picam.preview_configuration.align()
    picam.configure("preview")
    picam.start()
    frames = []


    while True:
        frame = picam.capture_array()
        cv2.imshow("picam", frame)
        frames.append(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def take_picture():
    picam = Picamera2()
    picam.preview_configuration.main.size=(320, 180)
    picam.preview_configuration.main.format="RGB888"
    picam.preview_configuration.align()
    picam.configure("preview")
    picam.start()
    picam.start_and_capture_file("calibration/picture3.jpg")

def load_images(filenames: List) -> List:
    return [imageio.imread(filename) for filename in filenames]

def calibrate_camera():
    imgs_path = glob.glob('/data/left/*jpg')
    imgs = load_images(imgs_path)

if __name__ == "__main__":
    take_picture()


