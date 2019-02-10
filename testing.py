import classify
import base64


imagePath = "testing.png"
imageFile = open(imagePath, "rb")
imageBytes = base64.b64encode(imageFile.read())
result = classify.analyse(imageBytes)

print(result)