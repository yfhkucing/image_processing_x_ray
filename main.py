import cv2


Path = "images\WhatsApp Image 2022-12-06 at 11.07.36 (2).jpeg"

def image_filter(path):
    while True :
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.bitwise_not(img)
        cv2.imshow('results',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
if __name__ == "__main__":
    image_filter(Path)