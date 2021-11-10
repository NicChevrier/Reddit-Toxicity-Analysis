import io
import os
import csv
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/nicholaschevrier/Downloads/vision-238320-c46644db27b4.json"
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud import vision_v1
# Instantiates a client
GOOGLE_APPLICATION_CREDENTIALS="/Users/nicholaschevrier/Downloads/vision-238320-c46644db27b4.json"

client = vision.ImageAnnotatorClient()
file_path = os.path.join(os.path.dirname(__file__), "/Users/nicholaschevrier/Downloads/Coding/Images")

def detect_text(path):
    """Detects text in the file."""
    with io.open(path, "rb") as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        try:
            text = texts[0].description
        except Exception as e:
            text = ""
        return text
        # return texts[0].description
    # for text in texts:
    #     print('\n"{}"'.format(text.description))

   # for text in texts:
     #  print('\n"{}"'.format(text.description))

# open csv file

with open("imagetextuser.csv", "w") as file:
    writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for image in os.listdir(file_path):
        print(image)

        image_text = detect_text(f"images/{image}")
        writer.writerow([image, image_text])
        # write to csv file

