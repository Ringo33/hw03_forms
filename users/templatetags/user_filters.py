from django import template
# В template.Library зарегистрированы все теги и фильтры шаблонов
# добавляем к ним и наш фильтр
register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})

@register.filter
def uglify(field, css):

    x = field
    y = len(field)
    new_field = []

    for letter in range(y):
        if letter % 2 == 0:
            z = x[letter].lower()
        else:
            z = x[letter].upper()

        new_field.append(z)

    return ''.join(new_field)




# синтаксис @register... , под которой описан класс addclass() -
# это применение "декораторов", функций, обрабатывающих функции
# мы скоро про них расскажем. Не бойтесь соб@к