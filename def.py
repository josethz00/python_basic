from datetime import datetime, timedelta


def my_first_function(task):
    print(task)


def getName(name, force_uppercase=True):
    if force_uppercase == True: #boolean, don't need to specify
        get_value = name[0:1].upper() #pega a pimeira letra
        print(get_value)
    else:
        get_value = name[0:1]
        print(get_value)
    return get_value



first_name = input("Digite o seu nome   ")
getName(first_name, False)
middle_name = input("Digite o seu segundo nome  ")
getName(middle_name)
last_name = input("Digite o seu último nome ")
getName(last_name, True)






my_first_function('blablablabla')