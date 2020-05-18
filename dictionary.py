# Dictionary pada Python adalah kumpulan pasangan kunci-nilai (pair of key-value) yang bersifat tidak berurutan.
# Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. Untuk mengakses datanya,
# kita harus mengetahui kuncinya (key). 

# dictionary ini sama seperti aray / list, kita memberikan nama setiap kunci untuk nilai tersebut

# disini nama nya 1 dan key
d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1])
print("d['key'] = ", d['key'])

print()

# nama nya 2 dan key
d = {2:'value','key':2}
print(type(d))
print("d[2] = ", d[2])
print("d['key'] = ", d['key'])

# namanya ratarata dan key
d = {'ratarata': '10.0', 'key': 2}
print(type(d))
print("d['ratarata'] = ", d['ratarata'])
print("d['key'] = ", d['key'])