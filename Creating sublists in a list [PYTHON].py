a = ['Broom', 'Being', 'Boring', 'Breeding', 'Dreaming', 'Doing', 'Dancing', 'Drinking',
     'Freezing', 'Falling', 'Flooding', 'Fearing', 'Saying', 'Sleeping', 'Standing',
     'Screaming', 'Running', 'Reading', 'Rolling', 'Rushing', 'Twerking', 'Telling']

def make_rows():
    while True: # For repeating
        row_size = int(input('Введите размер ячейки / Enter the size of a sublist '))
        if row_size > 0:
            # Найти кол-во групп / Calculate the amount of sublists
            subs = (len(a) // row_size) + 1 if len(a) % row_size > 0 else len(a) // row_size
            print(f'Слов: {str(len(a))} | | Ячеек: {str(subs)}')
            # Создать найденное кол-во групп / Create the found amount of sublists
            rows = [[] for i in range(subs)]; index = 0
            for x in range(len(a)):
                rows[index].append(a[x])
                if len(rows[index]) == row_size: index += 1
            print('\n' + str(rows) + '\n')
        else: print(a)
make_rows()
