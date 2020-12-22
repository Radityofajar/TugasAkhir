import cv2
import numpy as np

citra = cv2.imread("biner.png", 0)
citraBerwarna = cv2.merge((citra, citra,citra))

kontur, hierarki = cv2.findContours(citra, 
    cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

x, y, lebar, tinggi = cv2.boundingRect(kontur[1])
cv2.rectangle(citraBerwarna, (x, y),
    (x + lebar, y + tinggi),
    (255, 255, 0), 2)

persegiPanjang = cv2.minAreaRect(kontur[0])

kotak = cv2.boxPoints(persegiPanjang)
kotak = np.int32(kotak)

cv2.drawContours(citraBerwarna, [kotak], 0,
    (255, 255, 255), 2)


#cv2.imshow('Asli', citra)
cv2.imshow('Hasil', citraBerwarna)
cv2.waitKey(0)