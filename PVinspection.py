import cv2
import numpy as np
import matplotlib.pyplot as plt

citra = cv2.imread('PVHotSpot2.jpg')
if citra is None:
    print('Berkas citra tidak ditemukan')
    exit()

plt.subplot(243)
plt.imshow(citra[..., : : -1])
plt.xticks([]), plt.yticks([])
plt.title('Citra Asli')

abuAbu = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)

ambang, citraBiner = cv2.threshold(abuAbu, 200, 255,
    cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
pembukaan = cv2.morphologyEx(citraBiner,
    cv2.MORPH_OPEN, kernel, iterations = 3)

latarBelakang = cv2.dilate(pembukaan, kernel, iterations = 3)

transformJarak = cv2.distanceTransform(pembukaan,
    cv2.DIST_L2, cv2.DIST_MASK_5)

threshold, latarDepan = cv2.threshold(transformJarak,
    0.7 * transformJarak.max(), 255, cv2.THRESH_BINARY)

latarDepan = np.uint8(latarDepan)
daerahTakBertuan = cv2.subtract(latarBelakang, latarDepan)

plt.subplot(244)
plt.imshow(citraBiner, cmap = "gray", vmin = 0, vmax = 255)
plt.xticks([])
plt.yticks([])
plt.title('Citra Biner')

'''
jumBaris = citra.shape[0]
jumKolom = citra.shape[1]
hasil = np.zeros((jumBaris, jumKolom), np.uint8)

for baris in range(jumBaris):
    for kolom in range(jumKolom):
        if citra[baris, kolom] >= 210:
            hasil[baris, kolom] = 255

plt.subplot(244)
plt.imshow(hasil, cmap = "jet")
plt.xticks([]), plt.yticks([])
plt.title('Threshold')
'''

#plt.subplot(246)
#plt.imshow(daerahTakBertuan, cmap = "jet")
#plt.xticks([]), plt.yticks([])
#plt.title('Tak Bertuan')

jumObjek, penanda = cv2.connectedComponents(latarDepan)
print("Jumlah Hotspot", jumObjek - 1)

penanda = penanda + 1

penanda[daerahTakBertuan == 255] = 0

penanda = cv2.watershed(citra, penanda)

citra[penanda == -1] = [255, 0, 0]

tinggi, lebar = citra.shape[:2]

for indeks in range(1, jumObjek):
    mask = np.zeros((tinggi, lebar), np.uint8)
    mask[penanda == indeks + 1] = 1
    objek = citra * mask[:, :, np.newaxis]
    objek = objek[..., : : -1]

    plt.subplot(3, 10, indeks)
    plt.imshow(objek)
    plt.xticks([]), plt.yticks([])
    plt.title(indeks)

citra[penanda == -1] = [255, 200, 100]
plt.subplot(242)
plt.imshow(citra[..., : : -1])
plt.xticks([]), plt.yticks([])
plt.title('Hasil Akhir')

plt.show()

