f = open("test.txt", "r")

line = f.readlines()

for s in line:
    print (s)
f.close()

'''
with open("test.txt", "r") as fr:
    for line in fr:
        print(line
        print(line.strip())
'''
