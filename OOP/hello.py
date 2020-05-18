# prosedur adalah fungsi yang tidak ada return
# fungsi adalah sebuah fungsi yang ada return
# method adalah sebuah fungsi yang di panggil melalui import file atau class dan bersifat oop

def world():
	print('hello world')

nama = "Muhammad Shidqi"

class Reviewer:
	# argumen self adalah argumen pertama sebuah method, dan bisa jg di ubah menjadi nama lain
    # tapi di anjurkan tetap menggunakan nama self
    
	# method construct python
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas
    def review(self):
        print("Reviewer " + self.nama + " bertanggung jawab di kelas " + self.kelas)