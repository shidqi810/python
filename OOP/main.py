# prosedur adalah fungsi yang tidak ada return
# fungsi adalah sebuah fungsi yang ada return
# method adalah sebuah fungsi yang di panggil melalui import file atau class dan bersifat oop

# memasukkan file lain ke dalam python (memanggil file python yg lain)
import hello

# panggil method di dalam file
hello.world()

# panggil variabel -> variabel tidak ada tanda kurung
print(hello.nama)

# memanggil class di hello
	# Nama_file.Nama_class
diko = hello.Reviewer("Diko", "Python")
diko.review()


# --------------------------------------------------------------------------------------------------------------------
# bisa juga dengan mengimport file dan pilih method nya atau pilih bintang atau seluruh nya
# from hello import world
from hello import *

# dan kita bisa memanggil method nya secara langsung
world()

# panggil langsun variabel
print(nama)

# bila memanggil seluruh nya, kita hanya perlu memanggil class saja, tanpa memanggil nama file nya
coba = Reviewer("budi", "python")
coba.review()



# --------------------------------------------------------------------------------------------------------------------
# Memanggil file python dari direktori lain

import sys
sys.path.append('D:/D/Python/masuk/')

sys.hello()