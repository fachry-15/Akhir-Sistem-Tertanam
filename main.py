import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

def normalize(df):
    result = df.copy()
    for feature_name in df.columns[1:]:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

def save_to_excel(sorted_data):
    file_path_output = 'HasilPeringkat.xlsx'  # Nama file untuk menyimpan hasil peringkat

    # Ubah nama kolom
    sorted_data = sorted_data.rename(columns={'Alternatif': 'Nama Mahasiswa', 'Total': 'Nilai Akhir Perangkingan'})

    sorted_data.to_excel(file_path_output, index=False)
    print(f"\nHasil peringkat disimpan ke dalam file: {file_path_output}")

def main():
    # Membaca data dari file Excel
    file_path = 'Daftar Pendaftar Beasiswa.xlsx'  # Ganti dengan lokasi dan nama file Anda
    data_excel = pd.read_excel(file_path)

    # Menampilkan data dari file Excel
    print("\nData dari File Excel:")
    print(tabulate(data_excel, headers='keys', tablefmt='fancy_grid'))

    # Normalisasi matriks keputusan
    normalized_data = normalize(data_excel)
    weights = [0.2, 0.2, 0.2, 0.2, 0.2]  # Atur bobot sesuai kebutuhan
    weighted_data = normalized_data.copy()
    for i, feature_name in enumerate(normalized_data.columns[1:]):
        weighted_data[feature_name] = normalized_data[feature_name] * weights[i]

    # Menampilkan hasil normalisasi
    print("\nMatriks Normalisasi:")
    print(tabulate(normalized_data, headers='keys', tablefmt='fancy_grid'))

    # Menampilkan bobot normalisasi
    print("\nBobot Normalisasi:")
    print(tabulate(weighted_data, headers='keys', tablefmt='fancy_grid'))

    # Menghitung nilai akhir untuk setiap alternatif
    weighted_data['Total'] = weighted_data.iloc[:, 1:].sum(axis=1)

    # Menambahkan kolom 'Alternatif' ke DataFrame weighted_data
    if 'Alternatif' in data_excel.columns:
        weighted_data['Alternatif'] = data_excel['Alternatif']
    else:
        print("Kolom 'Alternatif' tidak ditemukan dalam data. Pastikan nama kolomnya benar.")

    if 'Total' in weighted_data.columns:
        # Menampilkan hasil akhir
        sorted_weighted_data = weighted_data[['Alternatif', 'Total']].sort_values(by='Total', ascending=False)
        print("\nHasil Akhir:")
        print(tabulate(sorted_weighted_data, headers='keys', tablefmt='fancy_grid'))

        # Simpan hasil peringkat ke file Excel
        save_to_excel(sorted_weighted_data)

        # Visualisasi hasil menggunakan grafik batang
        plt.figure(figsize=(15, 10))
        plt.bar(sorted_weighted_data['Alternatif'], sorted_weighted_data['Total'], color='skyblue')
        plt.title('Peringkat Hasil Akhir SAW')
        plt.xlabel('Alternatif')
        plt.ylabel('Nilai Total')
        plt.xticks(rotation=45, ha='right') 
        plt.show()
    else:
        print("Kolom 'Total' tidak ditemukan dalam data. Pastikan perhitungan nilai akhir sudah benar.")
        
        

if __name__ == "__main__":
    main()
