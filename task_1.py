# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
additional_information = ''
postal_index = ''
mail_address = ''
# information about the entrepreneur
ogrnip = ''
inn = ''
payment_accout = ''
bank = ''
bik = ''
correspondent_account = ''


def field_validation(number_digits):
    if number_digits == 15:
        while True:
            number = int(input('Введите номер ОГРНИП: '))
            result = number
            count = 0
            while number > 0:
                number //= 10
                count += 1
            if count != number_digits:
                print('ОГРНИП должен содержать 15 цифр')
            else:
                return result

    elif number_digits == 20:
        while True:
            number = int(input('Введите расчетный счет: '))
            result = number
            count = 0
            while number > 0:
                number //= 10
                count += 1
            if count != number_digits:
                print('Расчетный счет должен содержать 20 цифр')
            else:
                return result


def general_info_user(name_parameter, age_parameter, phone_parameter,
                      email_parameter, index_parameter, mail_parameter,
                      info_parameter):
    print(SEPARATOR)
    print('Имя:\t', name_parameter)
    if 11 <= age_parameter % 100 <= 19: years_parameter = 'лет'
    elif age_parameter % 10 == 1: years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4: years_parameter = 'года'
    else: years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail:\t', email_parameter)
    print('Индекс:\t', index_parameter)
    print('Адрес:\t', mail_parameter)
    if additional_information:
        print('')
        print('Дополнительная информация:')
        print(info_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                email = input('Введите адрес электронной почты: ')
                postal_index = input('Введите почтовый индекс: ')
                # filtering the value of the index field
                postal_index = "".join(c for c in postal_index
                                       if c.isdecimal())
                mail_address = input('Введите почтовый адрес (без индекса): ')
                additional_information = input(
                    'Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input information about the entrepreneur
                ogrnip = field_validation(15)
                inn = int(input('Введите номер ИНН: '))
                payment_accout = field_validation(20)
                bank = input('Введите название банка: ')
                bik = int(input('Введите БИК: '))
                correspondent_account = int(
                    input('Введите корреспондентский счет: '))
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, postal_index,
                                  mail_address, additional_information)

            elif option2 == 2:
                general_info_user(name, age, phone, email, postal_index,
                                  mail_address, additional_information)
                # print information about the entrepreneur
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:\t', ogrnip)
                print('ИНН:\t', inn)
                print('Банковские реквизиты')
                print('Р/с:\t', payment_accout)
                print('Банк:\t', bank)
                print('БИК:\t', bik)
                print('К/с:\t', correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
