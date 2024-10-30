import imageio
import numpy as np
import matplotlib.pyplot as plt

def extract_red_channel(image_path):
    # Membaca gambar menggunakan imageio
    image = imageio.imread(image_path)
    
    # Mengekstrak channel merah (R)
    red_channel = image[..., 0]
    
    # Mengatur channel hijau dan biru menjadi 0 untuk visualisasi channel merah
    red_image = np.zeros_like(image)
    red_image[..., 0] = red_channel  # Hanya channel merah yang diisi
    
    return red_image, red_channel

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
    
    # Mengekstrak channel merah
    red_image, red_channel = extract_red_channel(path)
    
    # Menampilkan gambar asli
    axes[i, 0].imshow(original_image)
    axes[i, 0].set_title(f'Original Image ({title})')
    axes[i, 0].axis('off')  # Menghilangkan axis
    
    # Menampilkan representasi channel merah
    axes[i, 1].imshow(red_image)
    axes[i, 1].set_title(f'Red Channel ({title})')
    axes[i, 1].axis('off')  # Menghilangkan axis

# Menampilkan semua gambar
plt.tight_layout()
plt.show()