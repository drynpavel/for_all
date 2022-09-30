spec_symbol_list = [spec
     for spec in '@№$%^&*']
#spec_symbol_list = '@№$%^&*'
file_extension = ['txt', 'doc']


name_file = input('Название файла: ')
print(any(name_file.endswith(end_text) for end_text in file_extension))
if any(name_file.startswith(start_text) for start_text in spec_symbol_list):
    print('Ошибка: название начинается на один из специальных символов')
elif not any(name_file.endswith(end_text) for end_text in file_extension):
    print('неверное расширение файла. Ожидалось .txt или .docx.')



