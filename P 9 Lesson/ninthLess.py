############ ФАЙЛЫ ############
# open() - Метод открытия
# .read() - Метод чтения
# .close() - Метод закрытия
# with open('файл') as переменная:
# .write - Метод записи

############ КЛЮЧИ ############
# R - чтение(ЗЩ УМОЛЧАНИЮ)
# W - запись и создание(Перезапись!)
# X - создание без перезаписи
# A - добавить в конец инфу

############ БИБЛИОТЕКИ #########
# import os
# os.getcwd() - Показать путь
# os.chdir() - Перейти к папке
# os.mkdir() - Создание папки
# os.listdir() - Список файлов и папок
# os.rename('Файл', 'новое имя') - Переименование
# os.remove('Файл') - Удалить 
# os.rmdir('') - Удалить папку


#### Отработка исключений ####
# with open('nine.txt') as file_1:
#     read_file = file_1.read()
#     print(read_file)
####
# try:
#     file_1 = open('nine.txt')
#     read_file = file_1.read()
#     print(read_file)
# finally:
#     file_1.close()

############ ПРИМЕРЫ ############

# with open('nine.txt', 'a') as file_1:
#     file_1.write('AADASD')
####
# import os
# os.chdir('up')
# os.mkdir('ddd')
# print(os.getcwd())
####
# import os
# print(os.listdir('C://Users/Администратор'))
####
# import os
# os.rmdir('oppa.txt')

