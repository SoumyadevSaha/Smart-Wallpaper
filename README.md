# Smart-Wallpaper
Smart Wallpaper Using Emotion Detection

- An Emotion Detection model is trained on the dataset from [Link to Emotion Detction Dataset](https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer)
- Check the `Emotion_Detect.ipynb` fro more details on the model architechture.
- Then, the user's face is captured in real-time using the `opencv-python` module, and their emotion is detected.
- Accordingly, the wallpaper for the device is updated in real-time.

## Getting Started

- Clone the Repo
- Create account in Kaggle, and download the kaggle.json after creating an api-key
- Upload the kaggle.json in a new google colab or similar environment, and run the cells of `Emotion_Detect.ipynb` file sequentially.
- Finally download the `model_emotion_detect.h5` and `model_weights_emo_detect.h5` files that were created.
- Paste both the files in the folder where `smart_wallpaper.py` file is present.
- Ensure that you have a <b>wallpapers folder</b> in the same directory as the script with images named `angry.jpg`, `disgust.jpg`, `fear.jpg`, `happy.jpg`, `neutral.jpg`, `sad.jpg`, and `surprise.jpg` corresponding to each emotion.
- Finally run the `smart_wallpaper.py` file, and minimize the window.
- Your wallpapers shall get updated automatically with your emotions.
