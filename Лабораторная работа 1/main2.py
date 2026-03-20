
floppy_disk_size = 1.44
number_of_pages_in_the_book = 100
number_of_lines_per_page = 50
number_of_characters_per_line = 25
one_symbol = 4

symbol_in_the_book = number_of_pages_in_the_book * number_of_lines_per_page * number_of_characters_per_line # количсетво символов в книге
Room_for_one = symbol_in_the_book * one_symbol # размер символов в одной книге

the_amount_of_disk_space = floppy_disk_size * (1024 * 1024) # количество байтов

number_of_books = int(the_amount_of_disk_space // Room_for_one) # количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", number_of_books)