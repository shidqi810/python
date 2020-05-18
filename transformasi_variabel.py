# variabel private tidak ada di dalam python, tetapi jika kita menambahkan garis barah pada nama variabel
# maka dia akan berubah menjadi non publik

x=1
type(x)
str(x).zfill(5)
# membuat variabel x menjadi string dan menambah kan 0 sebanyak 5x

p = 'Hello world!'
p = p.upper()
print(p)
p = p.lower()
print(p)

p.isupper()
p.islower()
'HELLO'.isupper()
'abc12345'.islower()

# method nya bisa dilanjutkan dengan method yg lain

print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('HELLO'.lower())
print('HELLO'.lower().islower())


# upper() dan lower() umumnya digunakan untuk memiliki perbandingan yang bersifat case-insensitive.
# ‘Dicoding’, ‘DIcoding’, atau ‘DICODING’ tidak sama satu dengan lainnya,
# namun Anda bisa memastikan karakternya sama jika Anda menggunakan upper() atau lower()
# saat membandingkan

feeling = input('How are you?')
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')


isalpha() # mengembalikan True jika string berisi hanya huruf dan tidak kosong.
isalnum() # mengembalikan True jika string berisi hanya huruf atau angka, dan tidak kosong.
isdecimal() # mengembalikan True jika string berisi hanya angka/numerik dan tidak kosong.
isspace() # mengembalikan True jika string berisi hanya spasi, tab, newline, atau whitespaces lainnya dan tidak kosong.
istitle() # mengembalikan True jika string berisi kata yang diawali huruf kapital dan dilanjutkan dengan huruf kecil seterusnya.

'hello123'.isalnum()


# mengecek kondisi mulai atau akhiran dari sebuah string

'Hello world!'.startswith('Hello')
'Hello world!'.endswith('world!')


# join dan split string

', '.join(['cats', 'rats', 'bats'])

' '.join(['My', 'name', 'is', 'Simon'])

'ABC'.join(['My', 'name', 'is', 'Simon'])

'My name is Simon'.split()

'MyABCnameABCisABCSimon'.split('ABC')

# contoh penerapan dalam pemisahan string multi line

a = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''
a.split('\n')


# teks rata kanan, kiri, atau tengah serta tambahan elemen di dalamnya

'Hello'.rjust(10)
'Hello'.ljust(20)

'Hello'.rjust(20, '*')
'Hello'.ljust(20, '-')

'Hello'.center(20)
'Hello'.center(20, '=')


# menghapus whitespace (spasi)

spam = '    Hello World     '
spam.strip()
spam.lstrip()
spam.rstrip()

spam.strip('Hello')


# string / substring replace

string = "geeks for geeks geeks geeks geeks"
print(string.replace("geeks", "Geeks"))

# 3 itu berfungsi untuk seberapa banyak elemen yg ingin di ganti tersebut
print(string.replace("geeks", "Geeks", 3))