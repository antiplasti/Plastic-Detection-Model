import requests
import picamera
import io
import time
import base64

imagePath = "temp.png"

def postImg():
	
    with picamera.PiCamera() as camera:
        print("Opening Camera.")
        time.sleep(2)
        camera.capture(imagePath)
        camera.close()
        print("Image Captured!")
    
    imageFile = open(imagePath, "rb")
    imageBytes = base64.b64encode(imageFile.read())
    print("Sending image to cloud server for analysis.")
    response = requests.post(
		"http://174.138.58.241/detect",
		data=imageBytes
	)
	
    print("Response received!")
    response_data = response.json()
    print(response_data)    
            
def main():
    while True:
        postImg()

if __name__ == '__main__':
    main()