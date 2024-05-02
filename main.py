from random import randint


def is_valid(num, max_num):
    try:
        num = int(num)
        if 1 <= num <= max_num:
            return True
        else:
            print(f'Число должно быть от 1 до {max_num}')
            return False
    except ValueError:
        print('Введите целое число')
        return False


def play_game(max_num):
    attempts = 0
    secret_number = randint(1, max_num)
    print(f'Добро пожаловать в числовую угадайку (от 1 до {max_num})')

    while True:
        user_input = input('Введите число: ')
        if not is_valid(user_input, max_num):
            continue
        user_guess = int(user_input)
        attempts += 1

        if user_guess < secret_number:
            print('Ваше число меньше загаданного, попробуйте еще раз')
        elif user_guess > secret_number:
            print('Ваше число больше загаданного, попробуйте еще раз')
        else:
            print(f'Вы угадали число {secret_number} с {attempts} попыток!')
            break

    return attempts


def main():
    while True:
        max_num = input('Введите правую границу для генерации числа: ')
        if not is_valid(max_num, float('inf')):
            continue
        max_num = int(max_num)
        attempts = play_game(max_num)

        play_again = input('Хотите сыграть еще раз? (да/нет): ')
        if play_again.lower() != 'да':
            print(f'Спасибо за игру! Общее количество попыток: {attempts}')
            break


if __name__ == "__main__":
    main()
