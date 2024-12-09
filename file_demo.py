myFile=open('filewrite.txt','w')
myFile.write('Baba Titi\n')
myFile.write('Araoluwa')
myFile.close()

for l in open('filewrite.txt'):
    print(l.upper(),end='')
# print(myf.readline())
# print(myf.readline())