import cv2
import sys
import numpy as np

if len(sys.argv) != 3:
    print('Masukan nama berkas gambar dan threshold value')
else:
    berkas = sys.argv[1]
    threshold = int(sys.argv[2])
    citra = cv2.imread(berkas, cv2.IMREAD_GRAYSCALE)

    if citra is None:
        print('Tidak dapat membaca berkas')
    else:
        jumBaris = citra.shape[0]
        jumKolom = citra.shape[1]
        hasil = np.zeros((jumBaris, jumKolom), np.uint8)

        for baris in range(jumBaris):
            for kolom in range(jumKolom):
                if citra[baris, kolom] >= threshold:
                    hasil[baris, kolom] = 255

        cv2.imshow('Asli', citra)
        cv2.imshow('Hasil', hasil)
        cv2.imwrite('biner.png', hasil)
        cv2.waitKey(0)