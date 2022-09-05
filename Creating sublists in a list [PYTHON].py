words = ['Broom', 'Being', 'Boring', 'Breeding', 'Dreaming', 'Doing', 'Dancing', 'Drinking',
     'Freezing', 'Falling', 'Flooding', 'Fearing', 'Saying', 'Sleeping', 'Standing',
     'Screaming', 'Running', 'Reading', 'Rolling', 'Rushing', 'Twerking', 'Telling']

def make_rows(row_size: int) -> list:
    row_size = abs(int(row_size)); index = 0; amount = len(words)
    # Найти кол-во групп / Calculate the amount of sublists
    if row_size>amount: row_size=amount
    if row_size > 0:
        subs = (amount // row_size) + 1 if amount % row_size > 0 else amount // row_size
        print(f'Слов: {len(words)} | | Ячеек: {subs}\n')
        # Создать найденное кол-во групп / Create the found amount of sublists
        rows = [[] for i in range(subs)]
        for x in range(amount):
            rows[index].append(words[x])
            if len(rows[index]) == row_size: index += 1
        return rows
    else: return words
        
print(make_rows(2))
