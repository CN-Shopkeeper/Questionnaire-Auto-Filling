import choice_question as choice


def getAnswersForA():
    answersA_ = []
    # A1
    a1 = choice.DanXuan(2, [0.55, 0.45], range(1, 3))
    a1ans = a1.getAnswer()
    answersA_.append(a1ans)
    # A2
    answersA_.append(choice.DanXuan(
        4, [0.2, 0.2, 0.3, 0.3], range(1, 5)).getAnswer())
    # A3
    if a1ans == a1.options[0]:
        answersA_.append(choice.DanXuan(
            4, [0.4, 0.2, 0.3, 0.1], range(1, 5)).getAnswer())
    else:
        answersA_.append(choice.DanXuan(
            4, [0.4, 0.3, 0.15, 0.15], range(1, 5)).getAnswer())
    # A4
    answersA_.append(choice.DanXuan(
        3, [0.6, 0.3, 0.1], range(1, 4)).getAnswer())
    # A5
    answersA_.append(choice.DanXuan(
        4, [0.13, 0.38, 0.49, 0.0], range(1, 5)).getAnswer())
    # A6
    answersA_.append(choice.DanXuan(
        5, [0.2, 0.35, 0.39, 0.05, 0.01], range(1, 6)).getAnswer())

    return answersA_


def getAnswersForB():

    answersB0_ = []
    answersB1_ = []
    # B0
    answersB0_.append(choice.DanXuan(
        5, [0.2, 0.2, 0.2, 0.2, 0.2], range(1, 6)).getAnswer())

    # B1
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 4.1, 0.6, range(1, 6)).getAnswer())

    # B2
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 4.0, 0.7, range(1, 6)).getAnswer())

    # B3
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 4.1, 0.7, range(1, 6)).getAnswer())

    # B4
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.4, 1.4, range(1, 6)).getAnswer())

    # B5
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.6, 0.9, range(1, 6)).getAnswer())

    # B6
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 4.1, 0.7, range(1, 6)).getAnswer())

    # B7
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.5, 0.9, range(1, 6)).getAnswer())

    # B8
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 2.3, 0.9, range(1, 6)).getAnswer())

    # B9
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 2.7, 1.3, range(1, 6)).getAnswer())

    # B10
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.7, 0.8, range(1, 6)).getAnswer())

    # B11
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.9, 0.7, range(1, 6)).getAnswer())

    # B12
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 2.4, 0.9, range(1, 6)).getAnswer())

    # B13
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.9, 0.5, range(1, 6)).getAnswer())

    # B14
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.8, 0.8, range(1, 6)).getAnswer())

    # B15
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.6, 0.8, range(1, 6)).getAnswer())

    # B16
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.8, 0.8, range(1, 6)).getAnswer())

    # B17
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 4.0, 0.5, range(1, 6)).getAnswer())

    # B18
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.6, 0.8, range(1, 6)).getAnswer())

    # B19
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 4.1, 0.8, range(1, 6)).getAnswer())

    # B20
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.9, 0.5, range(1, 6)).getAnswer())

    # B21
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 4.0, 0.7, range(1, 6)).getAnswer())

    # B22
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 4.0, 0.8, range(1, 6)).getAnswer())

    # B23
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 3.8, 0.6, range(1, 6)).getAnswer())

    # B24
    answersB1_.append(choice.DanXuan.from_average_variance(
        5, 4.1, 0.5, range(1, 6)).getAnswer())

    return answersB0_, answersB1_


def getAnswersForC():

    answersC_ = []
    answersC7_ = []

    # C1
    answersC_.append(choice.DanXuan(
        3, [0.22, 0.73, 0.05], range(1, 4)).getAnswer())

    # C2
    answersC_.append(choice.DuoXuan(
        6, [0.14, 0.16, 0.5, 0.18, 0.06, 0.0], range(1, 7)).getAnswer())

    # C3
    answersC_.append(choice.DuoXuan(
        6, [0.55, 0.77, 0.46, 0.41, 0.28, 0.35], range(1, 7)).getAnswer())

    # C4
    answersC_.append(choice.DanXuan(
        5, [0.14, 0.53, 0.30, 0.02, 0.01], range(1, 6)).getAnswer())

    # C5
    answersC_.append(choice.DanXuan(
        4, [0.10, 0.84, 0.05, 0.01], range(1, 5)).getAnswer())

    # C6
    answersC_.append(choice.DuoXuan(
        6, [0.53, 0.68, 0.37, 0.42, 0.50, 0.0], range(1, 7)).getAnswer())

    # C7 1
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.36, 0.488, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.71, 0.535, range(1, 6), 0.01).getAnswer()])

    # C7 2
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.29, 0.499, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.73, 0.563, range(1, 6), 0.01).getAnswer()])

    # C7 3
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.29, 0.717, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.79, 0.681, range(1, 6), 0.01).getAnswer()])

    # C7 4
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.25, 0.518, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.89, 0.679, range(1, 6), 0.01).getAnswer()])

    # C7 5
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.11, 0.825, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.86, 0.670, range(1, 6), 0.01).getAnswer()])

    # C7 6
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 3.95, 1.143, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.57, 0.940, range(1, 6), 0.01).getAnswer()])

    # C7 7
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.04, 0.799, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.66, 0.883, range(1, 6), 0.01).getAnswer()])

    # C7 8
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.16, 0.756, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.54, 0.835, range(1, 6), 0.01).getAnswer()])

    # C7 9
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.18, 0.658, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.75, 0.736, range(1, 6), 0.01).getAnswer()])

    # C7 10
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.05, 0.891, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.73, 0.745, range(1, 6), 0.01).getAnswer()])

    # C7 11
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.12, 0.693, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.54, 0.981, range(1, 6), 0.01).getAnswer()])

    # C7 12
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.00, 0.800, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.50, 0.945, range(1, 6), 0.01).getAnswer()])

    # C7 13
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.02, 0.709, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.54, 0.726, range(1, 6), 0.01).getAnswer()])

    # C7 14
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.09, 0.628, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.75, 0.591, range(1, 6), 0.01).getAnswer()])

    # C7 15
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.05, 0.633, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.80, 0.670, range(1, 6), 0.01).getAnswer()])

    # C7 16
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.13, 0.511, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.88, 0.766, range(1, 6), 0.01).getAnswer()])

    # C7 17
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.13, 0.657, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.87, 0.948, range(1, 6), 0.01).getAnswer()])

    # C7 18
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.21, 0.608, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.75, 0.627, range(1, 6), 0.01).getAnswer()])

    # C7 19
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.23, 0.545, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.91, 0.665, range(1, 6), 0.01).getAnswer()])

    # C7 20
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 3.93, 0.940, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.63, 0.748, range(1, 6), 0.01).getAnswer()])

    # C7 21
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.18, 0.586, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.80, 0.852, range(1, 6), 0.01).getAnswer()])

    # C7 22
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.00, 0.655, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.70, 0.797, range(1, 6), 0.01).getAnswer()])

    # C7 23
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.27, 0.709, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.91, 0.810, range(1, 6), 0.01).getAnswer()])

    # C7 24
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.32, 0.658, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.89, 0.643, range(1, 6), 0.01).getAnswer()])

    # C7 25
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.04, 0.617, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.84, 0.683, range(1, 6), 0.01).getAnswer()])

    # C7 26
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.00, 0.691, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.66, 0.846, range(1, 6), 0.01).getAnswer()])

    # C7 27
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.34, 0.446, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.84, 0.756, range(1, 6), 0.01).getAnswer()])

    # C7 28
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.32, 0.549, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.91, 0.737, range(1, 6), 0.01).getAnswer()])

    # C7 29
    answersC7_.append([choice.DanXuan.from_average_variance(
        5, 4.16, 0.719, range(1, 6), 0.01).getAnswer(), choice.DanXuan.from_average_variance(
        5, 3.80, 0.452, range(1, 6), 0.01).getAnswer()])

    return answersC_, answersC7_


def getAnswersForD():
    answersD_ = []

    # D1
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.5, 1.7, range(1, 7)).getAnswer())

    # D2
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.3, 1.6, range(1, 7)).getAnswer())

    # D3
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.4, 2.1, range(1, 7)).getAnswer())

    # D4
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.2, 2.0, range(1, 7)).getAnswer())

    # D5
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.3, 2.4, range(1, 7)).getAnswer())

    # D6
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.4, 1.6, range(1, 7)).getAnswer())

    # D7
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 2.8, 1.7, range(1, 7)).getAnswer())

    # D8
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.0, 1.8, range(1, 7)).getAnswer())

    # D9
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.3, 1.8, range(1, 7)).getAnswer())

    # D10
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.1, 1.9, range(1, 7)).getAnswer())

    # D11
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.4, 1.6, range(1, 7)).getAnswer())

    # D12
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 2.9, 1.9, range(1, 7)).getAnswer())

    # D13
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.6, 1.6, range(1, 7)).getAnswer())

    # D14
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 3.5, 1.8, range(1, 7)).getAnswer())

    # D15
    answersD_.append(choice.DanXuan.from_average_variance(
        6, 2.6, 2.0, range(1, 7)).getAnswer())

    return answersD_


def getAnswers():
    a_ = getAnswersForA()
    b0_, b1_ = getAnswersForB()
    c_, c7_ = getAnswersForC()
    d_ = getAnswersForD()
    return a_, b0_, b1_, c_, c7_, d_


if __name__ == '__main__':
    a, b0, b1, c, c7, d = getAnswers()
    print(a, b0, b1, c, c7, d)
