# prosedur adalah fungsi yang tidak ada return
# fungsi adalah sebuah fungsi yang ada return
# method adalah sebuah fungsi yang di panggil melalui import file atau class dan bersifat oop

# fungsi dalam python di definisikan dengan def

# tanpat return
def coba():
    print("coba")

# dengan return none
def printme( str ):
   print(str)
   return

# dengan return tidak none
def sum(arg1, arg2):
    # tambahkan kedua parameter dan kembalikan nilainya
    total = arg1 + arg2
    print('Inside the function: {}'.format(total))
    return total
    # jika tidak di return, maka fungsi ini tidak membawa nilai yg bisa di operasikan

# Panggil sum
# karena sum memiliki return, sehingga terdapat nilai yang dapat di operasikan
total = sum(10, 20);
print('Outside the function: {}'.format(total))

coba()
printme("Ini coba")
printme("Coba Lagi")


# fungsi pada list

def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print('Nilai di dalam fungsi: {}'.format(mylist))
 
# Panggil changeme
mylist = [10, 20, 30]
changeme(mylist)
print('Nilai di luar fungsi: {}'.format(mylist))


# membuat value di fungsi

def printinfo(name, age):
   "This prints a passed info into this function"
   print('Name: ', name)
   print('Age: ', age)
 
# Now you can call printinfo function (with age argument first)
printinfo(age=5, name="Dicoding")

def printinfo(name, age=35):
   "This prints a passed info into this function"
   print('Name: ', name)
   print ('Age: ', age)
 
# Now you can call printinfo function (with optional argument age)
printinfo(age=5, name='Dicoding')
printinfo(name='Data')