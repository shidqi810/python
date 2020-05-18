# Program untuk pembuatan kristal simple cubic

a = 5		# panjang diagonal sisi segitiga
x = [i*a for i in range(5) for j in range(5) for k in range(5)]
y = [j*a for i in range(5) for j in range(5) for k in range(5)]
z = [k*a for i in range(5) for j in range(5) for k in range(5)]

f = open("simple.xyz", "w+")
f.write("125\n\n")
for i in range(125):
	f.write("{0:>2s} {1:>3.2f} {2:>3.2f} {3:>3.2f}\n".format("Na",x[i],y[i],z[i]))
f.close()
