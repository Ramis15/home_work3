import math


def fizz_buzz(start, stop):
    summ = 0
    for i in range(start, stop + 1):
        if i % 3 == 0 and i % 5 == 0:
            summ += i
    return summ

print('0-3:', fizz_buzz(0, 3))
print('0-5:', fizz_buzz(0, 5))
print('15-15:', fizz_buzz(15, 15))
print('1000-20000:', fizz_buzz(1000, 20000))

def plural_form(number, form1, form2, form3):
    if int(str(number)[-1]) == 1 and number != 11:
        return form1
    elif int(str(number)[-1]) == 2 or int(str(number)[-1]) == 3:
        return form2
    else:
        return form3
print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))  


def html(tag, **kwargss):

    def decorator(decorated_function):

        def wrapper(input_value):
            utr = ''
            for key in kwargss.keys():
                 utr += f' {key}="{kwargss[key]}"'
            return f"<{tag}{utr}>{decorated_function(input_value)}</{tag}>"

        return wrapper

    return decorator
@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))
#