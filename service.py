import requests
import picamera
import io
import time

def postImg():
    
    imgBytes = io.BytesIO()
	
    with picamera.PiCamera() as camera:
        time.sleep(2)
        camera.campture(imgBytes, 'jpeg')
    
    headers = {
        'content-type': 'image/jpeg'
    }
    
    response = requests.post(
		"http://174.138.58.241/detect",
		data=imgBytes,
		headers=headers
	)
	
    utilData = response.json()
    print(utilData)
            
def main():
    while True:
        postImg()

if __name__ == '__main__':
    main()