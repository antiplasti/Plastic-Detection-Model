import requests
import io

def postImg():

    imgPath = "testing.png"    
    imgObj = {'file': open(imgPath, 'rb')}
    response = requests.post(
		"http://174.138.58.241/detect",
		files=imgObj
	)
    print(response)
    # utilData = response.json()
    # print(utilData)
            
def main():
    postImg()

if __name__ == '__main__':
    main()