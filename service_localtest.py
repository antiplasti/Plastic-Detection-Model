import requests
import io
import base64

def postImg():

    imgPath = "testing.png"    
    
    imagePath = "testing.png"
    imageFile = open(imagePath, "rb")
    imageBytes = base64.b64encode(imageFile.read())
    

    response = requests.post(
		"http://174.138.58.241/detect",
		data=imageBytes
	)
    print(response)
    # utilData = response.json()
    # print(utilData)
            
def main():
    postImg()

if __name__ == '__main__':
    main()