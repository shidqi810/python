# Tip: Python menganggap setiap nilai non-zero dan non-null sebagai True dan nilai zero/null sebagai False.

var1 = 100
if var1:
   print ("Cetak jika benar")
var2 = 0
if var2:
   print ("Cetak jika benar")


# program diskon

belanja = int(input("Masukkan total belanja Anda: "))
if belanja < 1000:
   discount = belanja * 0.05
   print ("Discount",discount)

elif amount<5000:
   discount = amount*0.10
   print ("Discount",discount)

else:
   discount = belanja*0.10
   print ("Discount",discount)
   
print ("Net payable:",belanja-discount)


# genap ganjil

a = 8
if a % 2 == 0:
	# bisa menggunakan cara ini
    print('bilangan %d adalah genap' % (a))
else:
	# bisa menggunakan cara ini
    print('bilangan {} adalah ganjil'.format(a))


# cek nilai 0

a = 0
if a > 0:
    print('bilangan {} adalah positif'.format(a))
elif a < 0:
    print('bilangan {} adalah negatif'.format(a))
else:
    print('bilangan {} adalah nol'.format(a))



# short hand ternary

output = None
msg = output or "No data returned"
print(msg)