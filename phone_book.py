def get_user_data() -> list:
    name = input('Введите имя: ')
    sur_name = input('Введите фамилию: ')
    phone_num = input('Введите номер телефона: ')
    desc = input('Введите описание: ')
    return [name,sur_name,phone_num,desc]

def create_record(gb_phone_book: list, user_data: list) -> list:
    gb_phone_book.append(user_data)
    return gb_phone_book

def get_file_name() -> str:
    return input('Введите имя файла c расширением: ')

def create_from_data(gb_phone_book: list,file_name:str,delimiter:str ) -> list:
    path_sourse= os.path.join ('.',file_name)
    with open(path_sourse,'r', encoding='utf-8') as sourse:
        for line in sourse:
            gb_phone_book=create_record(gb_phone_book,line.strip().split(delimiter))
    return gb_phone_book

def create_data_file (data_str:str, file_name:str) -> None:
    path_destination = os.path.join(".", file_name)
    with open(path_destination, "w", encoding="utf-8") as data_destination:
        data_destination.write(data_str)


def create_str_from_list (gb_phone_book) ->str:
    formating_phonebook = [f"{record[0]} {record[1]}, {record[2]}: {record[3]}\n" for record in gb_phone_book]
    result_string = ""
    for el in formating_phonebook:
        result_string += el 
    return result_string

def data_search (gb_phone_book:list) -> list:
    user_search = input("Введите 4 первые буквы фамилии: ")
    for record in range(len(gb_phone_book)):
        surname = f"{gb_phone_book[record][0]}"
        if surname[0:4] == user_search:
            return gb_phone_book[record]

def idx_search (gb_phone_book:list) -> int:
    user_search = input("Введите 4 первые буквы фамилии, из записи, которую хотите удалить: ")
    for idx in range(len(gb_phone_book)):
        surname = f"{gb_phone_book[idx][0]}"
        if surname[0:4] == user_search:
            return idx
    
        
    
                               
def menu():
    phone_book = list()
    while True:
        print('Введите 1 для выхода из справочника')
        print('Введите 2 для создания новой записи')
        print("Введите 3 для вывода на экран")
        print("Введите 4 для импорта данных из файла")
        print("Введите 5 для экспорта данных из файла")
        print("Введите 6 для удаления данных из файла")
        print("Введите 7 для  поиска данных")
        
        choise = int(input('Ваш выбор: '))
        if choise == 1:
            print('Вы выбрали выход')
            return
        if choise == 2:
            phone_book = create_record(phone_book, get_user_data())
        if choise == 3:
            print(create_str_from_list(phone_book))
        if choise==4:
            phone_book=create_from_data(phone_book,get_file_name(),',')
        if choise == 5:
            create_data_file(create_str_from_list(phone_book), get_file_name())
        if choise == 7:
            print(data_search(phone_book))
        if choise == 6:
            phone_book.pop(idx_search(phone_book))
            
            
        

import os
menu()