ip_list = input('Введите IP:').split('.')


chek = True
if len(ip_list) != 4:
    print('Адрес — это четыре числа, разделённые точками.')
    chek = False
else:
    for octet in ip_list:
        if not str(octet).isdigit():
            print(octet, '- это не целое число')
            chek = False
        elif int(octet) > 255:
            print(octet, 'превышает 255')
            chek = False
if chek:
    print('IP-адрес корректен')
