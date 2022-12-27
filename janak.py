f=open("abd.txt")
data=f.readline()
while True:
    if not data:
        break
    else:
        print(data[-1::-1])
        data=f.readline()


