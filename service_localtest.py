import requests
import io
from PIL import Image

def postImg():

    imgPath = "testimg.png"
        
    imgBytes = io.BytesIO()
    img = Image.open(imgPath)
    img.convert('RGB').save(imgBytes, 'png')  

    
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