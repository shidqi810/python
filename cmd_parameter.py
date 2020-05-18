# Berkas ini dapat dipanggil sebagai skrip di konsol atau command prompt,
# serta dapat ditambahkan parameter tambahan saat memanggil skrip tersebut

# yg dapat membuat parameter pada cmd itu berada pada sys.argv
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
print(sys.argv[1])