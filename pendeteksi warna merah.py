import cv2
import numpy as np

# Membaca gambar
image_path = 'apel.jpg'  # Ganti dengan jalur file gambar Anda
image = cv2.imread(image_path)

# Periksa apakah gambar berhasil dibaca
if image is None:
    print(f"Error: Gambar tidak ditemukan atau tidak dapat dibaca dari path: {image_path}")
else:
    # Konversi gambar ke ruang warna HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Definisikan rentang warna yang ingin dideteksi, misalnya untuk warna merah
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # Buat mask untuk warna merah
    mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # Deteksi kontur di dalam mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Gambar kontur di atas gambar asli
    for contour in contours:
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 3)

    # Tampilkan gambar hasil
    cv2.imshow('Detected Red Color', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
