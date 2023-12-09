import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)


for index, row in df.iterrows():
    df.at[index, 'Gaji'] = (lambda x: x * 1.05)(row['Gaji'])

print("Peningkatan Gaji 5%:")
print(df)
print("\nRingkasan:")
print(df[['Nama', 'Gaji']])

for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = (lambda x: x * 1.02)(row['Gaji'])


print("\nPeningkatan Gaji Tambahan:")
print(df)
print("\nRingkasan setelah peningkatan gaji tambahan:")
print(df[['Nama', 'Gaji']])