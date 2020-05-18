for letter in 'Python':  # First Example
    print('Current Letter: {}'.format(letter))

fruits = ['banana', 'apple', 'mango']

for fruit in fruits:  # Second Example
    print('Current fruit: {}'.format(fruit))


fruits = ['banana', 'apple', 'mango']
# memanggil angka panjang nya fruits
for index in range(len(fruits)):
	# memanggil index nya list fruits
    print('Current fruit: {}'.format(fruits[index]))


# while

count = 0
while (count < 5):
    print('The count is: {}'.format(count))
    count = count + 1

# python tidak memiliki statement do while


for i in range(3, 9):	# membuat sebuah deret angka dari angka 3 hingga 9
    print(i)

# range(n,p,q) membuat deret bilangan yang dimulai dari n,
# hingga sebelum p (bilangan p tidak ikut), dengan setiap elemennya memiliki selisih q
for i in range(1, 9, 2):  # list comprehension
	print(i)

# perulangan bertingkat

for i in range(0, 5): # method range memanggil deret nilai yang di mulai dari angka 0 hingga 5
    for j in range(0, 5 - i):
        print('*', end='') # Secara default, karakter end ini adalah newline ('\n')
    print()