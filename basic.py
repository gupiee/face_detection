import cv2
img=cv2.imread("C:/Users/admin/Pictures/Screenshots/ty.jpg",1)

cv2.imshow("Tony",img)
cv2.waitKey(2000000)
cv2.destroyAllWindows()