#!/bin/env python

# 1. count the number of rows in a file
# if the file size is small, the best solutio is 
# count = len(open('address.txt', 'rU').readlines() )
count = -1 # in case 0 line
for count, line in enumerate(open('address.txt', 'rU')):
    pass
count += 1
print "# of lines : ", count
# same result can be obtained by
# wc -l address.txt

# change tab to space
# open file line by line
file_obj = open('address.txt', 'rU')
out_obj  = open('address_space.txt', 'w')
try:
    for line in file_obj:
        line = line.expandtabs(1)
        out_obj.write(line)
finally:
    file_obj.close()
    out_obj.close()
# same can be done by
# cat address.txt| tr '\t' ' ' > address_space.txt

# 3. take 1st column and write it to col1.txt, and 2nd column to col2.txt

file_obj = open('address.txt', 'rU')
out_obj1  = open('col1.txt', 'w')
out_obj2  = open('col2.txt', 'w')
try:
    for line in file_obj:
        # remove the last carriage return
        line = line.rstrip('\n')
        col1, col2 = line.split('\t')
        out_obj1.write(col1)
        out_obj1.write('\n')
        out_obj2.write(col2)
        out_obj2.write('\n')
finally:
    file_obj.close()
    out_obj1.close()
    out_obj2.close()

# 4. combine col1.txt and col2.txt with tab separated
# not a best way as it reads everything onto a memory. may fail when a file size is large
file_obj1 = open('col1.txt', 'rU')
file_obj2 = open('col2.txt', 'rU')
out_obj1  = open('col3.txt', 'w')
try:
    line1 = file_obj1.readlines()
    line2 = file_obj2.readlines()
    for i in range(len(line1)):
        out_obj1.write('\t'.join((line1[i].rstrip('\n'), line2[i].rstrip('\n'))))
        out_obj1.write('\n')
finally:
    file_obj1.close()
    file_obj2.close()
    out_obj1.close()
## the same can be done by
## paste col1.txt col2.txt > col3.txt

