import imageio
import numpy as np
import matplotlib.pyplot as plt

def extract_blue_channel(image_path):
    # Membaca gambar menggunakan imageio
    image = imageio.imread(image_path)
    
    # Mengekstrak channel biru (B)
    blue_channel = image[..., 2]
    
    # Mengatur channel merah dan hijau menjadi 0 untuk visualisasi channel biru
    blue_image = np.zeros_like(image)
    blue_image[..., 2] = blue_channel  # Hanya channel biru yang diisi
    
    return blue_image, blue_channel

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
    
    # Mengekstrak channel biru
    blue_image, blue_channel = extract_blue_channel(path)
    
    # Menampilkan gambar asli
    axes[i, 0].imshow(original_image)
    axes[i, 0].set_title(f'Original Image ({title})')
    axes[i, 0].axis('off')  # Menghilangkan axis
    
    # Menampilkan representasi channel biru
    axes[i, 1].imshow(blue_image)
    axes[i, 1].set_title(f'Blue Channel ({title})')
    axes[i, 1].axis('off')  # Menghilangkan axis

# Menampilkan semua gambar
plt.tight_layout()
plt.show()