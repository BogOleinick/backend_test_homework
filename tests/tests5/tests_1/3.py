x = 3

# Такой перенос строк всё испортит, при любом x утверждение вернёт True:
assert (2 + x == 4, 'Очень длинная строка, в которой многословно '
                    'и с лирическими отступлениями описывается, '
                    'какой именно тест провален.')
# Isert думает что вся строка - это условие, потому что скобки расставленны
#  неправильно, нельяз брать условие и вывод в одни скобки



x = 3
assert 2 + x == 4, ('Очень длинная строка, в которой многословно '
                    'и с лирическими отступлениями описывается, '
                    'какой именно тест провален.') 
# Вот так было бы правильно
