f = open("1.txt", "a")
f.write("xxxxxxxxxxxxxxxxxxxxxxxx")
f.close()
f = open("1.txt", "r")
print(f.read())