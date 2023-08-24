import random
import numpy as np


class XuanZe():

    def __init__(self, _optionCount, _optionProbability, _options=[]) -> None:
        self.options = []
        if _optionCount != len(_optionProbability):
            raise Exception("XuanZe: (optionCount={0})!=(len(optionProbability)={1})".format(
                _optionCount, len(_optionProbability)))

        self.optionCount = _optionCount
        self.optionProbability = _optionProbability
        if (len(_options) == 0):
            for index in range(_optionCount):
                self.options.append(index)
        else:
            self.options = _options


class DanXuan(XuanZe):

    def __init__(self, _optionCount, _optionProbability, _options=[]):
        if (not np.isclose(np.sum(_optionProbability), 1.0)):
            raise Exception("DanXuan: sum of option probability({0}) is not close to 1.0, option probability={1}".format(np.sum(_optionProbability),
                                                                                                                         _optionProbability))
        super(DanXuan, self).__init__(
            _optionCount, _optionProbability, _options)

    def getAnswer(self):
        return random.choices(self.options, self.optionProbability)


class DuoXuan(XuanZe):

    def __init__(self, _optionCount, _optionProbability, _options=[]):
        super(DuoXuan, self).__init__(
            _optionCount, _optionProbability, _options)

    def getAnswer(self):
        result = []
        for index in range(self.optionCount):
            rand_float = random.random()
            if (rand_float <= self.optionProbability[index]):
                result.append(self.options[index])

        if len(result) == 0:
            result.append(self.options[np.argmax(self.optionProbability)])

        return result


if __name__ == '__main__':
    print("test danxuan...")
    danxuan = DanXuan(4, [0.2, 0.2, 0.3, 0.4], ['A', 'B', 'C', 'D'])
    for i in range(10):
        print(danxuan.getAnswer())

    print("test 多选...")
    duoxuan = DuoXuan(4, [0.8, 0.7, 0.6, 0.4], ['A', 'B', 'C', 'D'])
    for i in range(10):
        print(duoxuan.getAnswer())
