japanese_calendar_list = {
    1868: '明治',
    1912: '大正',
    1926: '昭和',
    1989: '平成',
    2019: '令和'
}


def japanese_calendar_conversion(year):
    low = 0
    high = len(japanese_calendar_list) - 1
    jp_calendar_year_list = list(japanese_calendar_list.keys())

    while low <= high:
        mid = (low + high) // 2
        if jp_calendar_year_list[mid] <= year < jp_calendar_year_list[mid + 1]:
            japanese_calendar = japanese_calendar_list[jp_calendar_year_list[mid]]
            if jp_calendar_year_list[mid] == year:
                return print("%s元年" % japanese_calendar)
            else:
                japanese_calendar_year = year - jp_calendar_year_list[mid] + 1
                return print("%s%s年" % (japanese_calendar, japanese_calendar_year))

        elif jp_calendar_year_list[mid] < year:
            low = mid + 1
        else:
            high = mid - 1


japanese_calendar_conversion(2000)
# 2000 => 平成12年
