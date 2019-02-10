import requests
import picamera
import io
import time
import base64

imagePath = "temp.png"

def postImg():
	
    with picamera.PiCamera() as camera:
        time.sleep(2)
        camera.capture(imagePath)
        camera.close()
    
    imageFile = open(imagePath, "rb")
    imageBytes = base64.b64encode(imageFile.read())
    
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