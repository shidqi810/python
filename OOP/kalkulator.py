class Kalkulator:
    """contoh kelas kalkulator sederhana"""
    i = 12345
    # argumen self adalah argumen pertama sebuah method, dan bisa jg di ubah menjadi nama lain
    # tapi di anjurkan tetap menggunakan nama self
    def __init__(self):
        self.j = 12345
 
    def f(self):
        print('hello world')

    # untuk class method tanda @classmethod harus dibuat agar tidak error
    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)

    # pemanggilannya bisa langsung dari class yang terdefinisi ataupun melalui objek
    # mirip seperti di java
    # tidak perlu argumen self atau argumen awal
    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)

# Dari pembuatan class Kalkulator di atas, di dalamnya ada definisi atribut i dan definisi fungsi f.

# Proses mengacu atribut yaitu Kalkulator.i dan Kalkulator.f sesuai definisi akan mengembalikan nilai integer dan fungsi.
# Pada proses mengacu atribut tersebut juga dapat mengubah nilainya,
# misalnya dengan memberikan bilangan bulat lain ke Kalkulator.i akan mengubah nilai yang ada saat ini.

Kalkulator.i = 1024  # maka nilai atribut i dalam Kalkulator berubah dari 12345 menjadi 1024
print(Kalkulator.i)



# ---------------------------------------------------------------------------------------------------------
# Pembuatan Object dari sebuah class

k = Kalkulator() # membuat instance dari kelas jadi objek, kemudian disimpan pada variabel k
k.i = 2020
print(k.i)
k.f()  # akan mencetak hello world ke layar



# ---------------------------------------------------------------------------------------------------------
# Class method

b = Kalkulator.tambah_angka(1, 2)  # tanpa perlu memberikan masukan untuk argumen cls
print(b)



# ---------------------------------------------------------------------------------------------------------
# static method

a = Kalkulator.kali_angka(2, 3)
print(a)