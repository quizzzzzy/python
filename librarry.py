LIBRARY = [
book = {
        "название":  "Грокаем алгоритмы",
        "автор":  "Бхаргава Адитья",
        "год":  2022
}
    ]

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
        print(f"название: {book['название']}")
        print(f"автор: {book['название']}")
        print(f"год: {book['год']}")


def remove_book() -> None:
    num = input("введите омер книги для удаления: ")
    if not  num.isdigit():
        print("номер должен быть целым положительным числом")
        return

    num = int(num)
    idx = num - 1
        
    if idx < 0:
        print("номер должен быть целым положительным числом")
        return

    if idx > len(library) :
        print("номер книги слишком большой, в библиотеке столько нет")
        return


    print(f"книга {LIBRARY[idx]} удалена успешно")
    library.pop(num - 1)


def find_book_by_number() -> None:
    """ищет книгу по порядковому номеру и показвает ее """
    if num book <= 0:
        print("ошибка!введен некоректный номер кинги!повторите попытку!")
        num = input("введите порядковый номер книги")


def visit_library() -> None:
    while True:
        os.system("cls")
        print("приветствуем вас в библиотеке, что вы хотите сделать")

        options = [
            "показать книгу",
            "добавить книгу",
            "удалить книгу",
            "показать книгу по порядковому номеру",
            "найти книгу по названию",
            "найти книгу по автору",
            "найти книгу по году издания",
        ]

        for num, option in enumerate(options):
            print(f"{num}. {option}")

            key_library = input("выберите действие и нажмите клавишу ENTER: ")
            if key_library == "1":
                return show_books()
            elif key_library == "2":
                return remove_book()
            elif key_library == "3":
                return add_book()
            elif key_library == "4":
                return find_book_by_number()
            elif key_library == "5":
                return search_by_year()
            elif key_library == "6":
                return search_by_author()
            elif key_library == "7":
                return search_by_title()
            brake




show_books()
remove_book()
show_books()
