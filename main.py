import re

dict1 = {
    'ноль': '0',
    'один': '1',
    'два': '2',
    'три': '3',
    'четыре': '4',
    'пять': '5',
    'шесть': '6',
    'семь': '7',
    'восемь': '8',
    'девять': '9',
    'десять': '10',
    'одиннадцать': '11',
    'двенадцать': '12',
    'тринадцать': '13',
    'четырнадцать': '14',
    'пятнадцать': '15',
    'шестнадцать': '16',
    'семнадцать': '17',
    'восемнадцать': '18',
    'девятнадцать': '19',
    'двадцать': '20',
    'тридцать': '30',
    'сорок': '40',
    'пятьдесят': '50',
    'шестьдесят': '60',
    'семьдесят': '70',
    'восемьдесят': '80',
    'девяносто': '90',
    'сто': '100',
    'двести': '200',
    'триста': '300',
    'четыреста': '400',
    'пятьсот': '500',
    'шестьсот': '600',
    'семьсот': '700',
    'восемьсот': '800',
    'девятьсот': '900',
    'тысяча': '1000',
    'миллион': '1000000',
    'миллиард': '1000000000',
}

dict2 = {
    'тысяч': '1000',
    'миллионов': '1000000',
    'миллиардов': '1000000000',
}

def words_to_digits(text):
    def calculate_sum(words):
        total = 0
        for word in words:
            total += int(dict1[word])
        return total

    words = re.findall(r'\b\w+\b', text.lower())
    result = ''
    multiplier = 1

    i = 0
    while i < len(words):
        if words[i] in dict1:
            sum_words = []
            while i < len(words) and words[i] in dict1:
                sum_words.append(words[i])
                i += 1
            result += str(calculate_sum(sum_words)) + ' '
        elif words[i] in dict2:
            multiplier *= int(dict2[words[i]])
            i += 1
        else:
            result += words[i] + ' '
            i += 1

    return result.strip()

def file_reader(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            replaced_text = words_to_digits(text)
            return replaced_text
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print("Произошла ошибка:", e)

print(file_reader("input.txt"))