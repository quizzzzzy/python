LIBRARY = []
book = {
        "название":  "Грокаем алгоритмы",
        "автор":  "Бхаргава Адитья",
        "год":  2022
}


def add_book():
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
    if year.isdigit():
        year = int(year)
    else:
        print("од должен быть целым числом: ")
        book = {
        "название": title,
        "автор": author,
        "год": year,
    }

LIBRARY.append(book)
print(f"Книга { title } { author } { year } успешно добавлена в библиотеку.")

add_book()
print("библиотека: ", LIBRARY)





def show_books():

    for num, book in enumerate("LIBRARY 1")
    print("номер на полке: ", num)
    for k, in book.items():
        print(f"{k}: {v}")







show_books()