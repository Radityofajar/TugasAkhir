import cv2

citra = cv2.imread('PVHotSpot.jpg')
citra1 = cv2.imread('PVHotSpot.jpg', cv2.IMREAD_GRAYSCALE)
if not citra is None:
   cv2.imshow('Gambar Seek Thermal.png', citra1)
   cv2.imshow('Gambar convert gray scale', citra)
   cv2.waitKey(0)