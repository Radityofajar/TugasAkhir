import cv2
import sys

if len(sys.argv) == 1:
    print('Masukan Nama Berkas: ')
else:
    berkas = sys.argv[1]

    citra = cv2.imread(berkas, cv2.IMREAD_UNCHANGED)

    if citra is None:
        print('Tidak dapat membaca berkas', berkas)
    
    else:
        info = citra.shape
        if len(info) == 2:
            print('Citra Berskala Keabu-abuan')
        else:
            print("Citra Berwarna")