input_string = input()
# получение фразы без пробелов
phrase = input_string.lower().replace(' ', '')

# разобьем фразу на ее компоненты
alpha = phrase[::2]
betta = phrase[1::2]

#гласные и согласные буквы
vowels = tuple('у е э о а ы я и ю ё'.split(' '))
consonants = tuple('й ц к н г ш щ з х ъ ж д л р п в ф ч с м т ь б'.split(' '))

# получаем число совпадений для компонента
def inspectComponent(component):
    count_vowels = 0
    count_consonants = 0
    for letter in component:
        if letter in vowels:
            count_vowels += 1
        elif letter in consonants:
            count_consonants += 1
        else:
            raise ValueError("Неизвестная буква")
    return {'count_vowels': count_vowels, 'count_consonants': count_consonants}


# для альфа компонента
aplpha_inspect = inspectComponent(alpha)
aplha_count_vowels = aplpha_inspect['count_vowels']
aplha_count_consonants = aplpha_inspect['count_consonants']

# для бетта компонента
betta_inspect = inspectComponent(betta)
betta_count_vowels = betta_inspect['count_vowels']
betta_count_consonants = betta_inspect['count_consonants']

# находим максимальное совпадение для компонент

aplha_max = 0
aplha_variant = None
betta_max = 0
betta_variant = None

if aplha_count_vowels > aplha_count_consonants:
    aplha_max = aplha_count_vowels
    aplha_variant = 'vowels'
else:
    aplha_max = aplha_count_consonants
    aplha_variant = 'consonants'

if betta_count_vowels > betta_count_consonants:
    betta_max = betta_count_vowels
    betta_variant = 'vowels'
else:
    betta_max = betta_count_consonants
    betta_variant = 'consonants'

# смотрим максимальное число совпадений и от этого выбираем вариант компоненты
# подсчитываем колво исправлений 

alpha_replaces = 0
betta_replaces = 0

if aplha_max > betta_max:
    # значит в alpha нужно менять меньше букв
    if aplha_variant == 'vowels':
        # вычитаем из длины число верных букв
        alpha_replaces = len(alpha) - aplha_count_vowels 
        betta_replaces = len(betta) - betta_count_consonants 
    else:
        alpha_replaces = len(alpha) - aplha_count_consonants
        betta_replaces = len(betta) - betta_count_vowels

else:
    # значит меньше букв надо менять в betta
    if betta_variant == 'vowels':
        betta_replaces = len(betta) - betta_count_vowels
        alpha_replaces = len(alpha) - aplha_count_consonants
    else:
        betta_replaces = len(betta) - betta_count_consonants
        alpha_replaces = len(alpha) - aplha_count_vowels

# считаем результат

result = alpha_replaces + betta_replaces

print(result)


    
