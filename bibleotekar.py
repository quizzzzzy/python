LIBRARY = []
book = {
        "название":  "Грокаем алгоритмы",
        "автор":  "Бхаргава Адитья",
        "год":  2022
}


def add_book() -> None:
    title = input("ведите название книги: ")
    author = input("ведите имя: ")
    year = input("ведите год издания: ")

    if not title:
        print("Ошибка! Нет названия: ")
        return
    if not author:
            print("нет такого автора: ")
            return
    if not year:
        print("нет года издания: ")
        return
    year = input("введите название книги")
    if year.isdigit():
        year = int(year)
    else:
        print("год должен быть целым числом: ")
        return
    book = {
        "название" , title
        "автор" , author
        "год" , year
    }


    LIBRARY.append(book)
    print(f"Книга  успешно добавлена в библиотеку.")

   
def show_books() -> None:
    """ выводит на экран все книги библиотеки, пронумировывая их c 1 """
    if not library:
        print("библиотека пуста")
        return 
    for num, book in enumerate(library, 1):
        print(f"номер на полке:{num}")
        print(f"название: {book[название]}")
        print(f"автор: {book[название]}")
        print(f"год: {book[год]}")


def remove_book() -> None:
    num = input("введите омер книги для удаления: ")
    if  num.isdigit():
            print("номер должен быть целым положительным числом")
            return
    else:
            num = int(num)
        
    if num < 1:
            print("номер должен быть целым положительным числом")
            return

    try:
       library.pop(num - 1)
    except:
        print("нет книги с таким номером")
    else:
        print("книга удалена успешно")


def find_book_by_nomber() -> None:
    """ищет книгу по порядковому номеру и показвает ее """
    
    num = input("введите порядковый номер книги")
      



            


    
    
    