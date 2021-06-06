# Importing opencv library for Image processing
import cv2
# Importing pytesseract library for character/text extraction from image
import pytesseract


def extractCharacter(img):
    '''
    Function to extract characters from the image
    '''
    # Converting the color channel from BGR to RGB (OpenCV reads the image as BGR while tesseract works on RGB)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    # shape method is used to obtain height,width,no of channels of the image
    height,width,no_of_channel = img.shape

    # image to boxes method returns string containing recognized characters and their box boundaries
    ocrData = pytesseract.image_to_boxes(img)

    # Iterate through the each line in the string
    for d in ocrData.splitlines():
        d = d.split(' ') 
        print(d)
        x,y,w,h = int(d[1]),int(d[2]),int(d[3]),int(d[4])
        cv2.rectangle(img,(x,height-y),(w,height-h),(0,0,200),2) # draw the box over the recognized character
        cv2.putText(img,d[0],(x,height-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2) # put the recognized character

    return img


if __name__ == "__main__":

    # To run the Tesseract ocr engine 
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    
    img_names = ['123.png','testcase1.jpg']

    # Read the image using imread method
    img = cv2.imread('./{}'.format(img_names[1]))

    processed_img = extractCharacter(img)

    # imshow method to display the image
    cv2.imshow('window',processed_img)

    cv2.waitKey(0)