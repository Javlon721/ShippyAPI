from random import randint, shuffle

def get_random_positions(diff=0, l=-100, r=100):
    """
    Возвращает массив из двух рандомных чисел в диапазоне от l до r включительно,
    второе число всегда на diff больше чем у первого
    
    Параметры:
        diff (int) - разница одного числа от другого (defaul=0)
        l (int) - наименьшее желанное число (defaul=-100)
        r (int) - наибольшее желанное число (defaul=100)
    """
    #* Cделал shuffle чтобы корабли находились в рандомном положении (правее или левее друг друга)
    pos1 = randint(l, r)
    pos2 = pos1 + diff
    shuffle_pos = [pos1, pos2]
    shuffle(shuffle_pos)
    return shuffle_pos
