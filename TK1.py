import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = [
    (510, 4, 8, 'C', 320),
    (550, 7, 50, 'A', 385),
    (620, 9, 7, 'C', 400),
    (630, 5, 24, 'B', 392),
    (655, 8, 100, 'A', 380),
    (700, 4, 8, 'C', 410),
    (780, 10, 7, 'C', 480),
    (800, 12, 50, 'A', 600),
    (920, 14, 8, 'C', 570),
    (1000, 9, 24, 'B', 620)
]

# Ekstraksi data
ukuran_ruangan = [row[0] for row in data]
tarif_internet = [row[2] for row in data]
tipe_bangunan = [row[3] for row in data]
harga_sewa = [row[4] for row in data]

# a. Visualisasi hubungan antara ukuran dan harga sewa
plt.figure(figsize=(10, 5))
plt.scatter(ukuran_ruangan, harga_sewa, label='Ukuran vs Harga Sewa', color='blue', marker='o')
plt.title('Hubungan Antara Ukuran Ruangan dan Harga Sewa')
plt.xlabel('Ukuran Ruangan (m^2)')
plt.ylabel('Harga Sewa (Rupiah)')
plt.legend()
plt.grid(True)
plt.show()

# b. Visualisasi hubungan antara tarif internet dan tipe bangunan
plt.figure(figsize=(10, 5))
sns.boxplot(x=tipe_bangunan, y=tarif_internet)
plt.title('Hubungan Antara Tarif Internet dan Tipe Bangunan')
plt.xlabel('Tipe Bangunan')
plt.ylabel('Tarif Internet (Mb per detik)')
plt.grid(True)
plt.show()

# c. Visualisasi tren harga sewa di setiap tipe bangunan
plt.figure(figsize=(10, 5))
sns.barplot(x=tipe_bangunan, y=harga_sewa, ci=None)
plt.title('Tren Harga Sewa di Setiap Tipe Bangunan')
plt.xlabel('Tipe Bangunan')
plt.ylabel('Harga Sewa (Rupiah)')
plt.grid(True)
plt.show()
