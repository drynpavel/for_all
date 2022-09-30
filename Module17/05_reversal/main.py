input_text = 'hhqwerh'


index_h =[i for i in range(len(input_text)) if input_text[i] == 'h']
new_list = input_text[(index_h[len(index_h) - 1] - 1):index_h[0] :-1]

print(index_h[len(index_h) - 1])
print(index_h)
print('Развёрнутая последовательность между первым и последним h:',new_list)

