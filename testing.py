import classify
import base64


imagePath = "testing.png"
imageFile = open(imagePath, "rb")
imageBytes = base64.b64encode(imageFile.read())

imgdata = base64.b64decode(imageBytes)
with open("write_test.png", 'wb') as f:
    f.write(imgdata)

