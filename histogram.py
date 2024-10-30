import imageio
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar grayscale
image = imageio.imread(r"C:\Users\ASUS\Desktop\oliversky.jpg")

# Memastikan gambar grayscale (jika berformat RGB, konversi ke grayscale)
if len(image.shape) == 3:
    image = np.dot(image[..., :3], [0.2989, 0.587, 0.114])

# Menghitung histogram untuk intensitas 0-255
hist, bins = np.histogram(image, bins=256, range=(0, 255))

# Menampilkan histogram
plt.figure(figsize=(10, 6))
plt.bar(bins[:-1], hist, width=1, edgecolor="black")
plt.title('Histogram of Grayscale Image Intensities')
plt.xlabel('Pixel Intensity (0-255)')
plt.ylabel('Frequency')
plt.show()

# a. Jumlah total piksel untuk setiap intensitas
for i, count in enumerate(hist):
    print(f"Intensitas {i}: {count} piksel")

# b. Intensitas dominan
dominant_intensity = np.argmax(hist)
print(f"Intensitas yang dominan adalah {dominant_intensity} dengan {hist[dominant_intensity]} piksel.")