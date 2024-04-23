import numpy as np
import cv2
# import tensorflow as tf
from tensorflow.keras.models import load_model
from keras.preprocessing import image
import sys
import os

# Load the pre-trained model
model = load_model('model_emotion_detect.h5')
model.load_weights('model_weights_emo_detect.h5')

# Function to set the wallpaper
def set_wallpaper(image_path):
    platform = sys.platform
    print(platform)
    print(image_path)
    if platform == "win32":
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
    elif platform == "darwin":
        cmd = f'set-desktop -m {image_path}'
        os.system(cmd)
    elif platform.startswith("linux"):
        cmd = f'gsettings set org.gnome.desktop.background picture-uri file://{image_path}'
        os.system(cmd)

# Dictionary to map label index to emotion
label_dict = {0:'Angry', 1:'Disgust', 2:'Fear', 3:'Happy', 4:'Neutral', 5:'Sad', 6:'Surprise'}

# Accessing the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Preprocess the frame for prediction
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (48, 48))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=-1)

    # Make prediction
    result = model.predict(img)
    result = list(result[0])

    # Get the index of the maximum prediction
    img_index = result.index(max(result))

    # Get the emotion label
    emotion = label_dict[img_index]

    # Display the emotion detected
    cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow('Emotion Detection', frame)

    # Set the wallpaper based on the detected emotion
    if emotion == 'Angry':
        set_wallpaper('wallpapers/angry.jpg')
    elif emotion == 'Disgust':
        set_wallpaper('wallpapers/disgust.jpg')
    elif emotion == 'Fear':
        set_wallpaper('wallpapers/fear.jpg')
    elif emotion == 'Happy':
        set_wallpaper('wallpapers/happy.jpg')
    elif emotion == 'Neutral':
        set_wallpaper('wallpapers/neutral.jpg')
    elif emotion == 'Sad':
        set_wallpaper('wallpapers/sad.jpg')
    elif emotion == 'Surprise':
        set_wallpaper('wallpapers/surprise.jpg')

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
