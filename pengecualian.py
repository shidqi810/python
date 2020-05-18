# pythonn mencoba untuk melakukan perintah ini
try:
    with open('contoh_tidak_ada.py') as file:                   
        print(file.read())

# Jika tidak berhasil atau gagal, maka akan di eksekusi perintah except
except (FileNotFoundError, ):
    print('file tidak ditemukan')


d = {'ratarata': '10.0', 'key': 2}
print('\ntry 1')
try:
    print('rata-rata: {}'.format(d['rata_rata']))
except KeyError:                                 
    print('kunci tidak ditemukan di dictionary')
except ValueError:              
    print('nilai tidak sesuai')
 
print('\ntry 2')
try:
    print('rata-rata: {}'.format(d['ratarata']))
except KeyError:                                 
    print('kunci tidak ditemukan di dictionary')
except (ValueError, TypeError):
    print('nilai atau tipe tidak sesuai')
 
print('\ntry 3')
try:
    print('pembulatan rata-rata: {}'.format(int(d['ratarata'])))
except (ValueError, TypeError) as e:         
    print('penangan kesalahan: {}'.format(e))