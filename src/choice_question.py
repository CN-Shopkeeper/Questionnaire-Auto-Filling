import random
import numpy as np
from scipy.stats import triang


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

    @classmethod
    def from_average_variance(self, _optionCount, _average, _variance, _options, _errorPrecision=0.05):
        if _optionCount != len(_options):
            raise Exception("XuanZe: (optionCount={0})!=(len(_options)={1})".format(
                _optionCount, len(_options)))

        # 定义三角分布的参数：最小值、最大值和众数
        a = _options[np.argmin(_options)] - 1
        b = _options[np.argmax(_options)]
        c = _average

        # 创建三角分布对象
        triangular_dist = triang(c=(c-a)/(b-a), loc=a, scale=b-a)

        sortedOptions = np.array(sorted(_options))

        # 计算每一个Option的概率
        probabilities = []
        for index, option in enumerate(sortedOptions):
            probabilities.append(triangular_dist.cdf(option))
        for index, option in reversed(list(enumerate(sortedOptions))):
            if 0 != index:
                probabilities[index] -= probabilities[index-1]
        probabilities = np.array(probabilities)

        # 计算平均值
        def getExpection():
            return np.sum(sortedOptions*probabilities)

        # 计算方差
        def getVariance():
            average_ = getExpection()
            return np.sum((sortedOptions - average_)**2 * probabilities)

        # 微调平均值
        averageDiff = _average - getExpection()
        if averageDiff > 0:
            index_ = np.argmax(sortedOptions)
            while averageDiff > _errorPrecision:
                # for probability in probabilities:
                #     print(probability)
                # print(averageDiff)
                if probabilities[index_]+0.01 <= 1 and probabilities[index_-1] - 0.01 >= 0:
                    probabilities[index_] += 0.01
                    probabilities[index_-1] -= 0.01
                averageDiff = _average - getExpection()
                index_ -= 1
                if index_ == np.argmin(sortedOptions):
                    index_ = np.argmax(sortedOptions)
        else:
            index_ = np.argmin(sortedOptions)
            while abs(averageDiff) > _errorPrecision:
                # for probability in probabilities:
                #     print(probability)
                # print(averageDiff)
                if probabilities[index_]+0.01 <= 1 and probabilities[index_+1] - 0.01 >= 0:
                    probabilities[index_] += 0.01
                    probabilities[index_+1] -= 0.01
                averageDiff = _average - getExpection()
                index_ += 1
                if index_ == np.argmax(sortedOptions):
                    index_ = np.argmin(sortedOptions)

        # 微调方差
        varianceDiff = _variance-getVariance()
        sophtonCenterRight = np.searchsorted(sortedOptions, _average, "left")
        sophtonCenterLeft = sophtonCenterRight-1
        index_ = 0
        if varianceDiff < 0:
            while abs(varianceDiff) > _errorPrecision:
                # print("varianceDiff before tune variance: ", varianceDiff)
                # print("Expection before tune variance: ", getExpection())
                # print(probabilities)

                # Shopkeeper的虹吸算法
                influence = 0
                dpRight = 0.01/(sophtonCenterLeft+1)
                for i in range(sophtonCenterRight):
                    if probabilities[i]-dpRight >= 0 and probabilities[sophtonCenterRight]+dpRight <= 1:
                        probabilities[i] -= dpRight
                        probabilities[sophtonCenterRight] += dpRight
                        influence += dpRight*(sophtonCenterRight-i)

                while not np.isclose(influence, 0):
                    dpLeft = influence / \
                        np.sum(range(1, len(sortedOptions)-1-sophtonCenterLeft+1))
                    for i in range(sophtonCenterRight, len(sortedOptions)):
                        if probabilities[i]-dpLeft >= 0 and probabilities[sophtonCenterLeft]+dpLeft <= 1:
                            probabilities[i] -= dpLeft
                            probabilities[sophtonCenterLeft] += dpLeft
                            influence -= dpLeft

                varianceDiff = _variance-getVariance()
                # print("varianceDiff after tune variance: ", varianceDiff)
                # print("Expection after tune variance: ", getExpection())
                # print(probabilities)

        else:
            # print("varianceDiff before tune variance: ", varianceDiff)
            # print("Expection before tune variance: ", getExpection())
            # print(probabilities)

            while varianceDiff > _errorPrecision:
                # Shopkeeper的虹吸算法(逆)
                influence = 0
                dpRight = 0.01/(sophtonCenterLeft+1)
                # print(dpRight)
                for i in range(sophtonCenterRight):
                    if probabilities[i]+dpRight <= 1 and probabilities[sophtonCenterRight]-dpRight >= 0:
                        probabilities[i] += dpRight
                        probabilities[sophtonCenterRight] -= dpRight
                        influence += dpRight*(sophtonCenterRight-i)

                while not np.isclose(influence, 0):
                    # print(len(options)-1-sophtonCenterLeft)
                    # exit
                    dpLeft = influence / \
                        np.sum(range(1, len(sortedOptions)-1-sophtonCenterLeft+1))
                    for i in range(sophtonCenterRight, len(sortedOptions)):
                        if probabilities[i]+dpLeft <= 1 and probabilities[sophtonCenterLeft]-dpLeft >= 0:
                            probabilities[i] += dpLeft
                            probabilities[sophtonCenterLeft] -= dpLeft
                            influence -= dpLeft

                varianceDiff = _variance-getVariance()
                # print("varianceDiff after tune variance: ", varianceDiff)
                # print("Expection after tune variance: ", getExpection())
                # print(probabilities)

        # 微调完了，赋值回去
        optionProbability = []
        for _option in _options:
            optionProbability.append(
                probabilities[np.where(sortedOptions == _option)[0]].item())

        return DanXuan(_optionCount, optionProbability, _options)

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
    danxuan = DanXuan(4, [0.1, 0.2, 0.3, 0.4], ['A', 'B', 'C', 'D'])
    for i in range(10):
        print(danxuan.getAnswer())

    print("test duoxuan...")
    duoxuan = DuoXuan(4, [0.8, 0.7, 0.6, 0.4], ['A', 'B', 'C', 'D'])
    for i in range(10):
        print(duoxuan.getAnswer())

    print("test danxuan from average and variance...")
    danxuan = DanXuan.from_average_variance(5, 4.1, 0.6, [1, 2, 3, 4, 5])
    for i in range(10):
        print(danxuan.getAnswer())
