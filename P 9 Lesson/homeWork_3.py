# 3. Написать функцию, которая будет открывать файл №1 находить в нем целые числа и записывать их в файл №2 ( файл №1 создать произвольно) 

import os

def findnum(file1,file2):
    with open(file1) as doc1:
      with open(file2, 'a') as doc2:
        read1 = doc1.read()
        for i in read1:
            if i != 0:
                doc2.write(i)

findnum('nine.txt','nine2.txt')



# with open('nine.txt') as doc1:
#     with open('nine2.txt', 'a') as doc2:
#         read1 = doc1.read()
#         for i in read1:
#                 i = int(i)
#                 if i != 0:
#                     i = str(i)
#                     doc2.write(i)


