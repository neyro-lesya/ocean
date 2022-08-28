import os
import random
import time


class Ocean:
    __MIN_SIZE_OCEAN = 5
    __MAX_SIZE_OCEAN = 20
    __MAX_SIZE_TYPE = 3

    __start_program = "в приведенной ниже схеме океана используюются следующие " \
                      "обозначения:\n0-пустота\n1-скала\n2-рыба\n3-креветка "

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        print(self.__start_program)
        self.__size = random.randrange(self.__MIN_SIZE_OCEAN, self.__MAX_SIZE_OCEAN + 1)
        self.__ocean = [[random.randint(0, self.__MAX_SIZE_TYPE) for j in range(self.__size)] for i in
                        range(self.__size)]
        pass

    def print(self):
        for i in range(self.__size):
            print(self.__ocean[i], "\n")
        pass

    # в нижеприведенных функциях будем возвращать массив
    # с количеством рыб и кркветок, где рыбы -0 элемент, а креветки-1

    def __count_fish_shrimps(self, i, j):
        result = [0] * 2
        if j != 0:
            if self.__ocean[i][j - 1] > 1:
                result[self.__ocean[i][j - 1] - 2] += 1
            if i != 0 and self.__ocean[i - 1][j - 1] > 1:
                result[self.__ocean[i - 1][j - 1] - 2] += 1
            if i != self.__size - 1 and self.__ocean[i + 1][j - 1] > 1:
                result[self.__ocean[i + 1][j - 1] - 2] += 1
        if j != self.__size - 1:
            if self.__ocean[i][j + 1] > 1:
                result[self.__ocean[i][j + 1] - 2] += 1
            if i != 0 and self.__ocean[i - 1][j + 1] > 1:
                result[self.__ocean[i - 1][j + 1] - 2] += 1
            if i != self.__size - 1 and self.__ocean[i + 1][j + 1] > 1:
                result[self.__ocean[i + 1][j + 1] - 2] += 1

        if i != 0 and self.__ocean[i - 1][j] > 1:
            result[self.__ocean[i - 1][j] - 2] += 1
        if i != self.__size - 1:
            if self.__ocean[i + 1][j] > 1:
                result[self.__ocean[i + 1][j] - 2] += 1
        return result

    def statick_ocean(self):
        count_changes = 0
        count_walkthroughs = 0
        ocean = [[0 for i in range(self.__size)] for j in range(self.__size)]
        while count_changes != 0 or count_walkthroughs == 0:
            count_changes = 0
            for i in range(self.__size):
                for j in range(self.__size):
                    if self.__ocean[i][j] == 1:
                        ocean[i][j] = self.__ocean[i][j]
                        continue
                    count_shrimps = 0
                    count_fishes = 0
                    array_count = self.__count_fish_shrimps(i, j)
                    count_fishes = array_count[0]
                    count_shrimps = array_count[1]
                    if self.__ocean[i][j] == 0:
                        if count_fishes == 3:
                            ocean[i][j] = 2
                            count_changes += 1
                            continue
                        if count_shrimps == 3:
                            ocean[i][j] = 3
                            count_changes += 1
                            continue
                    if self.__ocean[i][j] == 2:
                        if count_fishes > 3 or count_fishes < 2:
                            ocean[i][j] = 0
                            count_changes += 1
                            continue
                        ocean[i][j] = self.__ocean[i][j]
                        continue
                    if self.__ocean[i][j] == 3:
                        if count_shrimps < 2 or count_shrimps > 3:
                            ocean[i][j] = 0
                            count_changes += 1
                            continue
                    ocean[i][j] = self.__ocean[i][j]
                    continue
            if count_changes != 0:
                count_walkthroughs += 1
                self.__ocean = ocean
                time.sleep(3)
                os.system("cls||clear")
                print(self.__start_program)
                print("после {0} обхода схема океана выглядит следующим образом".format(count_walkthroughs))
                self.print()


ocean = Ocean()
ocean.print()
ocean.statick_ocean()
