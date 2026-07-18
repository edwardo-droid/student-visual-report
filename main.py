import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
print(data)

rata_rata = data["nilai"].mean()
print("Rata-rata Nilai:", rata_rata)

nilai_tertinggi = data["nilai"].max()
nilai_terendah = data["nilai"].min()
print("Nilai tertinggi:", nilai_tertinggi)
print("Nilai terendah:", nilai_terendah)

data["status"] = data["nilai"].apply(
    lambda x: "lulus"if x >= 75 else "tidak lulus"
    )
print(data)

plt.bar(data["nama"], data["nilai"])
plt.title("Grafik Nilai Siswa")
plt.xlabel("Nama")
plt.ylabel("Nilai")
plt.show()