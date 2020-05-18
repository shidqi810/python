# prosedur adalah fungsi yang tidak ada return
# fungsi adalah sebuah fungsi yang ada return
# method adalah sebuah fungsi yang di panggil melalui import file atau class dan bersifat oop

# fungsi dengan argumen yang dinamin (dapat berubah ubah)

# Argumen posisi dapat bersifat dinamis dengan menambahkan sintaksis tanda bintang (*),
# untuk menampung kontainer (Tuple).
# Kontainer (Tuple) ini bisa bersifat opsional, artinya tidak wajib diisi (boleh kosong),
# jika memang tidak ada argumen yang perlu ditambahkan.

def rungsi_dinamis(fixed, *args):
    
    print('argumen yang tetap = {}'.format(fixed))
    for a in args:
        print('argumen posisi {}'.format(a))
 
# Panggil rungsi_dinamis 
rungsi_dinamis(10)
rungsi_dinamis(70, 60, 50)


# bintang 1 untuk menggunakan tuple sebagai argumen
# bintang 2 untuk menggunakan dictionary sebagai argumen

def printinfo(*args, **kwargs):
    for a in args:
        print('argumen posisi {}'.format(a))
    for key, value in kwargs.items():
        print('argument kata kunci {}:{}'.format(key, value))
 
 
# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{'i':7, 'j':8, 'key':2})	# key itu nama nya, jadi untuk memanggilnya kita panggil nama key nya



# ------------------------------------------------------------------------------------------------------------------
# Fungsi Anonim (anonymous)
# tidak dideklarasikan seperti halnya fungsi pada umumnya dengan kata kunci def,
# melainkan menggunakan kata kunci (keyword) lambda.
# Sebuah fungsi lambda dapat menerima argumen dalam jumlah berapa pun,
# namun hanya mengembalikan satu nilai expression. Fungsi Lambda tidak dapat memuat perintah atau ekspresi lainnya,
# misalnya tidak bisa melakukan print.

sum = lambda arg1, arg2: arg1 + arg2

print ("Hasil fungsi sum : ", sum( 10, 20 ))
print ("Hasil fungsi sum : ", sum( 20, 20 ))



# ------------------------------------------------------------------------------------------------------------------
# Cakupan Variabel

total = 0  # This is global variable.
# fungsi didefinisikan di bawah ini
def sum(arg1, arg2):
    global total
    total = arg1 + arg2 # variabel lokal total
    print('Inside the function local total: ', total)
    return total
 
sum(10, 20)
print('Outside the function (global) total: ', total)