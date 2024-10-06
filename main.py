with open('a.txt') as fp:
    data1 = fp.read()
with open('b.txt') as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2
print("Merging two files...")
with open('MergedFile.txt','w') as fp:
    fp.write(data1)