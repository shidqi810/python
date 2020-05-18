# break

for letter in 'Python':     # First Example
    if letter == 'h':
        break
    print('Current letter: {}'.format(letter))

var = 10                    # Second Example
while var > 0:             
    print('Current variable value: {}'.format(var))
    var = var - 1
    if var == 5:
        break


# continue (melewati statement yang terpilih, dan melanjutkan perulangan)

for letter in 'Python':     # First Example
    if letter == 'h':
        continue
    print('Current letter: {}'.format(letter))

for a in [0, 1, -1, 2, -2, 3, -3]:     #Second Example
    if a <= 0:
        continue
    print('Elemen positif: {}'.format(a))

var = 10                    # Third Example
while var > 0:             
    var = var -1
    if var == 5:
        continue
    print('Current variable value: {}'.format(var))


# else setelah for dan while (statement else akan dijalankan ketika semua if nya bernilai false.
# meskipun di tingkatan yang berbeda)

for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()

n = 5
while n > 0:
    n = n - 1
    if n == 2:
        break
    print(n)
else:
    print("Loop is finished")



# pass (membiarkan program tetap berjalan tanpa menghilangkan statement apapun)

for letter in 'Python':
    if letter == 'h':
        pass
        print ("This is pass block")
    print('Current letter: {}'.format(letter))



# List Comprehension (membuat list dengan inline loop dan if / memasukkan nya langsung ke dalam value list)

#Cara 1
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
  squares.append(n**2)	# memanggil method append
print(squares)

#Cara 2 List Comprehension
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]	#bisa langsung ke dalam value nya
print(squares)

#Contoh3 menemukan bilangan yang ada di kedua list
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = []
for a in list_a:
  for b in list_b:
    if a == b:	# cek angka nya, apakah bernilai sama
      common_num.append(a)
     
print(common_num)  # Output [2, 3, 4]

#Contoh4 Implementasi dengan list comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num) # Output: [2, 3, 4]

# Contoh 5 kecilkan semua huruf
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [_.lower() for _ in list_a]		# underscore merupakan penamaan variabel yang valid
print(small_list_a) # Output: ['hello', 'world', 'in', 'python']


list_a = range(1,10,2)
x = [ [a**2, a**3] for a in list_a]
print(x)