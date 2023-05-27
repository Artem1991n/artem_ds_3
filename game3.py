"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def improve_predict(number: int = 1) -> int:
   
    count = 1
    predict_number = 50  # начинаем с середины диапазона

    while number != predict_number:
        count += 1
        if number > predict_number:
            predict_number += (50 // (2 ** (count - 2)))  # смещаем предполагаемое число на половину от диапазона, который соответствует текущему шагу
        else:
            predict_number -= (50 // (2 ** (count - 2)))
    
    return count


def score_game(predict_number) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_number(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game()
