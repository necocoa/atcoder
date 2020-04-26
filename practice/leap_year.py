# うるう年を計算する
# 4で割り切れる年
# ただし、100で割り切れて400で割り切れない年はうるう年ではない


def leap_year(start_year, end_year):
    for i in range(start_year, end_year+1):
        if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
            print(i)


leap_year(2100, 2100)
