import requests
import io
import base64
import firebase
import env

def postImg(): 
    
    imagePath = "testing.png"
    imageFile = open(imagePath, "rb")

    imageBytes = base64.b64encode(imageFile.read())

    response = requests.post(
		"http://174.138.58.241/detect",
		data=imageBytes
	)
    print("Response received!")
    response_data = response.json()
    print(response_data)
    
    db = firebase.Firebase()
    db.authenticate()
    db.push(response_data)
            
def main():
    postImg()

if __name__ == '__main__':
    main()