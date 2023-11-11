import pandas as pd
from tabulate import tabulate

print('Fachry Rizky Prasetya')
print('E41212057')
# Data dummy langsung dalam bentuk DataFrame Pandas
data_dummy = pd.DataFrame({
    'Alternatif': ['A', 'B', 'C', 'D', 'E'],
    'Kriteria1': [4, 2, 6, 8, 5],
    'Kriteria2': [7, 5, 8, 6, 4],
    'Kriteria3': [5, 8, 4, 7, 6],
    'Kriteria4': [8, 6, 7, 5, 9]
})

# Menampilkan data dummy
print("\nData Dummy:")
print(tabulate(data_dummy, headers='keys', tablefmt='fancy_grid'))

# Normalisasi matriks keputusan
def normalize(df):
    result = df.copy()
    for feature_name in df.columns[1:]:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

# Menghitung bobot normalisasi
normalized_data = normalize(data_dummy)
weights = [0.25, 0.25, 0.25, 0.25]  # Atur bobot sesuai kebutuhan
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
weighted_data['Total'] = weighted_data.sum(axis=1)

# Menampilkan hasil akhir
print("\nHasil Akhir:")
print(tabulate(weighted_data[['Alternatif', 'Total']].sort_values(by='Total', ascending=False), headers='keys', tablefmt='fancy_grid'))
