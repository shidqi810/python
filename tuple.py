# Tuple adalah jenis dari list yang tidak dapat diubah elemennya.
# Umumnya tuple digunakan untuk data yang bersifat sekali tulis, dan dapat dieksekusi lebih cepat.

t = (5,'program', 1+3j)
print(t[1])
print(t[0:3])

# command di bawah akan error jika dijalankan, sebab tuple tidak bisa diubah nilainya
# t[0] = 10