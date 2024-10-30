import imageio
import numpy as np
import matplotlib.pyplot as plt

def convert_to_threshold(image_path, threshold=128):
    # Membaca gambar menggunakan imageio
    image = imageio.imread(image_path)
    
    # Jika gambar memiliki 3 channel (RGB), konversi ke grayscale terlebih dahulu
    if len(image.shape) == 3:
        grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    else:
        grayscale_image = image
    
    # Mengonversi gambar grayscale menjadi biner menggunakan threshold
    binary_image = grayscale_image > threshold
    
    return binary_image

# Path gambar daun pepaya, singkong, dan kenikir
image_paths = {
    "Daun Pepaya": r"C:\Users\ASUS\Desktop\DAUN PEPAYA.jpg",
    "Daun Singkong": r"C:\Users\ASUS\Desktop\DAUN SINGKONG.jpg",
    "Daun Kenikir": r"C:\Users\ASUS\Desktop\DAUN KENIKIR.jpg"
}

# Setup grid untuk menampilkan gambar
fig, axes = plt.subplots(len(image_paths), 2, figsize=(12, 8))

# Proses setiap gambar
for i, (title, path) in enumerate(image_paths.items()):
    # Membaca gambar asli
    original_image = imageio.imread(path)
    
    # Mengonversi gambar ke threshold (biner)
    binary_image = convert_to_threshold(path)
    
    # Menampilkan gambar asli
    axes[i, 0].imshow(original_image)
    axes[i, 0].set_title(f'Original Image ({title})')
    axes[i, 0].axis('off')  # Menghilangkan axis
    
    # Menampilkan representasi threshold (biner)
    axes[i, 1].imshow(binary_image, cmap='gray')
    axes[i, 1].set_title(f'Threshold Image ({title})')
    axes[i, 1].axis('off')  # Menghilangkan axis

# Menampilkan semua gambar
plt.tight_layout()
plt.show()
