# 3. Напишите функцию, которая берет 2 списка сравнивает их и если есть хотя бы 1 общей компонент выводит надпись TRUE 


spisok = [72,280,89,210,'CBBA','CBBH','CBCA','CBCH',25,105,62,72]
spisok2 = [70,283,91,212,'CBDA','CBDH','CBEA','CBEH',25,115,41,70]


def dubli(set,set2):
    for i in set:
        if i in set2:
            print(True)

dubli(spisok,spisok2)


