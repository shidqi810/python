l = [1,2,3,3,4,4,4,4,5,6] # merupakan sebuah list

# mengubah list menjadi set
s = set(l)
x = "Hello, World"
 
print(l)
print(len(l))
 
print(s)
print(len(s))
 
print(x)
print(len(x))


# ------------------------------------------------------------------------------------------------------------
# penggabungan dan replika

print([1, 2, 3] + ['A', 'B', 'C'])

print(['X', 'Y', 'Z'] * 3)

spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

arr = [0]*10
print(len(arr))
print(arr)


# ------------------------------------------------------------------------------------------------------------
# penggunaan method range untuk pengulangan

# Fungsi range() memberikan deret bilangan dengan pola tertentu.
# Untuk melakukan perulangan (misalnya for) dalam mengakses elemen list, Anda dapat menggunakan fungsi range()
for i in range(9):
    print(i)

for i in range(3, 9):	# membuat sebuah deret angka dari angka 3 hingga 9
    print(i)

# membuat deret bilangan yang dimulai dari n,
# hingga sebelum p (bilangan p tidak ikut), dengan setiap elemennya memiliki selisih q
for i in range(1, 9, 2):  # list comprehension
	print(i)


# ------------------------------------------------------------------------------------------------------------
# in and not in

'howdy' in ['hello', 'hi', 'howdy', 'heyas']

spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam

'cat' not in spam


# ------------------------------------------------------------------------------------------------------------
# mengubah nilai beberapa variabel sekaligus di dalam list dan tuple

# satu persatu memanggil index nya dan memberi nilai
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# memberikan nilai sekaligus berdasarkan urutan index nya, dan banyak nya data harus sesuai dengan jumlah index
cat = ['fat', 'orange', 'loud'] # From List
size, color, disposition = cat
cat = ('fat', 'orange', 'loud')  # From Tuple
size, color, disposition = cat

# tukar nilai
a, b = 'Alice', 'Bob'
a, b = b, a
print(a)
print(b)


# ------------------------------------------------------------------------------------------------------------
# Sort. sort tidak bisa untuk mengurutkan variabel yg berbeda tipe

# tidak bisa di urutkan karena berbeda tipe variabel
# z = [1, 3, 2, 4, 'Alice', 'Bob']
# z.sort()

# mengurutkan angka
x = [2, 5, 3.14, 1, -7]
x.sort()
print(x)

# mengurutkan hurufnya
y = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
y.sort()
print(y)

y.sort(reverse=True)	# membalik urutannya
y
print(y)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)	# memanggil fungsi lower
print(spam)


# ------------------------------------------------------------------------------------------------------------
# Manipulasi String

# \'          Single quote
# \"          Double quote
# \t          Tab
# \n         Newline (line break)
# \\          Backslash

st = 'Say hi to Bob\'s mother.'		# backslash berfungsi untuk membuat petik tersebut terbaca sebagai string
print(st)

print("Hello there!\nHow are you?\nI\'m doing fine.")

# multi line string, bisa dengan 3x kutip dua. atau 3x kutip satu
multi_line = """Hello there!
How are you?
I'm fine."""
print(multi_line)

# raw string
print(r'That is Carol\'s cat.')