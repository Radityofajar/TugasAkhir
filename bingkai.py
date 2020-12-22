import cv2

citra = cv2.imread('goldhill.png')
hasil = citra.copy()

TEBAL = 20
HITAM = 0

jumBaris = hasil.shape[0]
jumKolom = hasil.shape[1]

#atas
for baris in range(TEBAL):
    for kolom in range(jumKolom):
        hasil[baris, kolom] = HITAM

#bawah
for baris in range(jumBaris - TEBAL - 1, jumBaris):
    for kolom in range(jumKolom):
        hasil[baris, kolom] = HITAM

#kiri
for baris in range(TEBAL, jumBaris-TEBAL-1):
    for kolom in range(TEBAL):
        hasil[baris, kolom] = HITAM

#kanan
for baris in range(TEBAL, jumBaris-TEBAL-1):
    for kolom in range(jumKolom - TEBAL -1, jumKolom):
        hasil[baris, kolom] = HITAM

cv2.imshow('Gambar asal', citra)
cv2.imshow('Gambar Hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindow()