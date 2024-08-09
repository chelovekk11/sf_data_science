import numpy as np
def game_core_v3(number: int = 1) -> int:
    """Угадывание числа с использованием бинарного поиска.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100
    predict = (low + high) // 2
    
    while number != predict:
        count += 1
        if number > predict:
            low = predict + 1
        elif number < predict:
            high = predict - 1
        
        predict = (low + high) // 2

    return count

# Функция для оценки качества алгоритма
def score_game(game_core):
    """Запускает игру несколько раз и выводит среднее количество попыток.
    
    Args:
        game_core (function): Функция угадывания числа.
    """
    np.random.seed(1)  # Установка seed для воспроизводимости
    random_numbers = np.random.randint(1, 101, size=(1000))  # Случайные числа для тестирования
    scores = [game_core(number) for number in random_numbers]
    score_mean = int(np.mean(scores))
    print(f'Ваш алгоритм угадывает число в среднем за {score_mean} попыток.')

# Оценим качество вашего алгоритма
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
  