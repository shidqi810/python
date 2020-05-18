a=int(input("Masukin angkamu : "))
n = (a*2)
i = 0
print("Hasilnya \n ")
for i in range(n):
    if (i==0 or i==n):
        print("* "*n)

    if (i== a-2 or i == a):
        print("* "*a)

    if (i==n-1):
        print("* "*n)
    
    else:
        print("* "+"  "*(n-2)+"*")
