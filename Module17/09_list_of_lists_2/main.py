nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [nice_list[i][j][z]
            for i in range(2)
                for j in range(3)
                    for z in range(3)]
print('Ответ: ',new_list)
