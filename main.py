header = "Mencari Kondisi Cuaca dengan Metode Fuzzy"

horizontal_line = "+" * len(header)

print(horizontal_line)
print(header)
print(horizontal_line)

# Mengambil input suhu, aliran udara, dan cuaca
suhu = float(input("Masukkan suhu (dalam Celsius): "))
aliran_udara = float(input("Masukkan kecepatan aliran udara (dalam km/jam): "))
cuaca = input("Masukkan kondisi cuaca (cerah/hujan/berawan): ")



# Pengendalian inferensi cuaca berdasarkan variabel input
if suhu > 30 and aliran_udara > 15:
    kondisi_cuaca = "Panas dan berangin"
    diagram_cuaca = "☀️🌬️"
elif suhu < 10 and cuaca == "hujan":
    kondisi_cuaca = "Dingin dan hujan"
    diagram_cuaca = "❄️🌧️"
elif suhu < 20 and cuaca == "berawan":
    kondisi_cuaca = "Sejuk dengan cuaca berawan"
    diagram_cuaca = "🌤️☁️"
else:
    kondisi_cuaca = "Kondisi cuaca tidak teridentifikasi"
    diagram_cuaca = "❓"

# Menampilkan output kondisi cuaca dalam bentuk diagram teks
print("Kondisi cuaca saat ini:", diagram_cuaca)
print("Deskripsi: ", kondisi_cuaca)
input("Tekan Enter untuk keluar dari prediksi cuaca...")