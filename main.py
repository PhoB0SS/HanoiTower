import os


class HanoiTower:
    """
    Игра "Ханойская башня"

    Даны три стержня, на один из которых нанизаны n колец, причём кольца отличаются размером и лежат меньшее на большем.
    Задача состоит в том, чтобы перенести пирамиду за наименьшее число ходов на другой стержень.

    Количество колец n задается в начале игры.
    Вывод башен производится в консоль.

    Запуск: python -m main.py
    """

    def __init__(self):
        """ Инициализация параметров игры """

        self._count = 0
        self._towers = ([], [], [])
        self._circle_amount = self.input_params()
        self.print_towers()

    def input_params(self) -> int:
        """ Задание величины башни """

        while True:
            circle_amount = input("Введите величину башни: ")
            if circle_amount.isdigit():
                circle_amount = int(circle_amount)
                if circle_amount > 1:
                    [self._towers[0].append(i) for i in range(circle_amount, 0, -1)]
                    return circle_amount
            print("Введите целое число больше 1!")

    def print_towers(self) -> None:
        """ Вывод башен в консоль """

        os.system('cls||clear')
        for i in range(self._circle_amount + 1, 0, -1):
            for k in range(len(self._towers)):
                if len(self._towers[k]) >= i:
                    at_amount = self._towers[k][i - 1]
                else:
                    at_amount = 0
                print(" " * (self._circle_amount - at_amount), "@" * at_amount, "||", "@" * at_amount,
                      " " * (self._circle_amount - at_amount + 3), end="", sep="")
            print()
        print("=" * (self._circle_amount * 6 + 12))

    def is_available(self, tower_from: str, tower_to: str) -> bool:
        """ Проверка возможности сделать ход """

        if tower_from not in ("1", "2", "3") and tower_to not in ("1", "2", "3"):
            print("Введите числа от 1 до 3!")
            return False
        if tower_from == tower_to:
            print("Введите разные числа!")
            return False
        tower_from = int(tower_from)
        tower_to = int(tower_to)
        if not self._towers[tower_from - 1]:
            print(f"В башне {tower_from} нет элементов!")
            return False
        if not self._towers[tower_to - 1]:
            return True
        if self._towers[tower_from - 1][-1] > self._towers[tower_to - 1][-1]:
            print(f"Нельзя поместить большее кольцо на меньшее!")
            return False
        return True

    def move_circles(self) -> None:
        """ Сделать ход """

        while True:
            tower_from = input("Введите башню, с которой переместить кольцо: ")
            tower_to = input("Введите башню, на которую переместить кольцо: ")
            if self.is_available(tower_from, tower_to):
                self._towers[int(tower_to) - 1].append(self._towers[int(tower_from) - 1].pop())
                self._count += 1
                self.print_towers()
                if not self._towers[0] and not self._towers[1]:
                    print(f"Победа! Шагов совершено: {self._count}.")
                    return


def main() -> None:
    """ Запуск игры """

    try:
        game = HanoiTower()
        game.move_circles()
    except KeyboardInterrupt:
        print("\nВыход...")


if __name__ == "main":
    main()
