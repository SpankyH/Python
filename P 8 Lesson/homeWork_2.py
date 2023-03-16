# 2. Написать функцию, для удаления всех дубликатов в произвольном массиве.

# В списке маркировки продукции с моей работы

spisok = [70,280,89,210,'CBBA','CBBH','CBCA','CBCH',
        25,105,62,70,'CBBB','CBBI','CBBA','CBCI',
        140,350,123,210,'CBBC', 'CBBH']
spis = set(spisok)
print(str(spis))



spisok2 = [70,280,89,210,70,105]
def delete(clear):
        pustoi = []
        for i in clear:
                pustoi.append(i)
                if i in pustoi:
                        clear.remove(i)
        print(clear)
        
delete(spisok2)




# spisok = [70,280,89,210,70,105]
# pustoi = []
# for i in spisok:
#     pustoi.append(i)
#     if i in pustoi:
#         spisok.remove(i)
# print(spisok)

# spisok = [70,280,89,210,70,105]
####
# x = 0
# for i in spisok:
#     if i in spisok:
#         x = i
#         if x == i:
#             spisok.remove(i)



# ЧЕСТНО, все что ниже, я ЗАГУГЛИЛ =(

spisok3 = [70,280,89,210,'CBBA','CBBH','CBCA','CBCH',
        25,105,62,70,'CBBB','CBBI','CBBA','CBCI',
        140,350,123,210,'CBBC', 'CBBH']
spisokNoDub = list(set(spisok3))
print(spisokNoDub)