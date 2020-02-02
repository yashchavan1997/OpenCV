# import the necessary packages
import imutils
import cv2
 
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("MVIMG.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
 
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)

resized = imutils.resize(image, width=100)
# cv2.imshow("Imutils Resize", resized)
# cv2.waitKey(0)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)
# cv2.waitKey(0)

edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

thresh = cv2.threshold(gray, 49, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

X=[]
Y=[]

for y in range(len(thresh)):
    for x in range(len(thresh[y])):
        if(thresh[y,x]==255) :
            X.append(x)
            Y.append(y)
            # print(".")

(cx,cy)=thresh.shape
Centx=int(sum(X) / len(X))
Centy=int(sum(Y)/len(Y))
print(Centx)
print(Centy)

output = resized.copy()
cv2.circle(output, (Centx, Centy), 10, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)