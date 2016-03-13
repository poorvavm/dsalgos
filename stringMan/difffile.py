# Difference of two files
f1 = open("file1.txt",'r')
f2 = open("file2.txt",'r')

line1 = f1.readline()
line2 = f2.readline()

while (line1 and line2):
    line1 = line1.rstrip()
    line2 = line2.rstrip()

    if line1 != line2 and len(line1) > len(line2):
        print line1
    elif line1 != line2 and len(line2) > len(line1):
        print line2

    line1 = f1.readline()
    line2 = f2.readline()