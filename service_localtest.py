import requests
import io

def postImg():

    imgPath = "@testing.png"    
    response = requests.post(
		"http://174.138.58.241/detect",
		files=imgPath
	)
	
    utilData = response.json()
    print(utilData)
            
def main():
    while True:
        postImg()

if __name__ == '__main__':
    main()