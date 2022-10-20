words = ['Broom', 'Being', 'Boring', 'Breeding', 'Dreaming', 'Doing', 'Dancing', 'Drinking',
     'Freezing', 'Falling', 'Flooding', 'Fearing', 'Saying', 'Sleeping', 'Standing',
     'Screaming', 'Running', 'Reading', 'Rolling', 'Rushing', 'Twerking', 'Telling']

""" SHORT VERSION:
def make_chunks(lst: list, n: int):
    result = []
    for i in range(0, len(lst), n):
        res.append(lst[i:i + n])
    return result

print(make_chunks(words, 3))
///////////////////////////
'Handmade' Version: """
def make_chunks(row_size: int = 2) -> list:
    """
    :type row_size: int
    :return list
    """
    index: int = 0
    amount: int = len(words)
    # Найти кол-во чанков / Calculate the amount of chunks
    row_size: int = abs(amount if row_size > amount else row_size)
    if row_size >= 1:
        subs: int = (amount // row_size) + 1 if amount % row_size > 0 else amount // row_size
        print(f'Слов: {len(words)} | | Ячеек: {subs}\n')
        # Создать высчитанное кол-во чанков / Create the calculated amount of chunks
        chunks = [[] for i in range(subs)]
        for x in range(amount):
            chunks[index].append(words[x])
            index += 1 if len(chunks[index]) == row_size else 0
        return chunks
    else:
        return words


print(make_chunks(3))
