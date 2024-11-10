def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if not("@" in sender and "@" in recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif not recipient.endswith(('.com', '.ru', '.net')) or not sender.endswith(('.com', '.ru', '.net')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>")

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')























