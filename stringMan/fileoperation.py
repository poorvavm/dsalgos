# read data from a file and write data to a file in Python
infile = "inputfile.txt"
outfile ="outputfile.txt"

# print each line as read in and striping out last newline character
in_file = open(infile)
for line  in in_file:
    print (line[:-1])

# print each line as read in and print first word
in_file = open(infile)
for line  in in_file:
    row = line.split(" ")
    print (row[0])

# print each line as read in and print line as a list
in_file = open(infile)
for line  in in_file:
    row = line.split(" ")
    for i in range(0, len(row)):
        print (row[i])

# add each line to a list
my_matrix =list[]
in_file = open(infile)
for line  in in_file:
    row = line.split(" ")
    my_matrix.append(row)
print (my_matrix[0][0])


# write makes only to output file
out_file = open(outfile,'a')
for line  in in_file:
    out_file.write(line)
