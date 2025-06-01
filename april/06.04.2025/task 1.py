# <p><b>Привет</b></p>
def bold(func):
    def wrapper():
        stroka = func()
        return f"<b>{stroka}</b>"
    return wrapper

def italic(func):
    def wrapper():
        stroka = func()
        return f"<i>{stroka}</i>"
    return wrapper

def paragraph(func):
    def wrapper():
        stroka = func()
        return f"<p>{stroka}</p>"
    return wrapper

@bold
@italic
@paragraph
def get_text_form_user():
    s = input("Введите текст для вставки на сайт: ")
    return s

new_text = get_text_form_user()
print(new_text)

print(get_text_form_user())