from typing import TypeVar, Tuple, Dict

japanese_calendar_list: Dict[int, str] = {
    1868: '明治',
    1912: '大正',
    1926: '昭和',
    1989: '平成',
    2019: '令和'
}

Wareki = Tuple[str, int]


def bs(year: int) -> Tuple[str, int]:
    low = 0
    high = len(japanese_calendar_list) - 1
    jp_calendar_year_list = list(japanese_calendar_list.keys())

    while low <= high:
        mid = (low + high) // 2
        if jp_calendar_year_list[mid] <= year < jp_calendar_year_list[mid + 1]:
            wareki = japanese_calendar_list[jp_calendar_year_list[mid]]
            wareki_year = year - jp_calendar_year_list[mid] + 1
            return wareki, wareki_year
        elif jp_calendar_year_list[mid] < year:
            low = mid + 1
        else:
            high = mid - 1
    return 'notthing', 0


def japanese_calendar_conversion(year: int) -> str:
    wareki, wareki_year = bs(year)
    if wareki == 'notthing':
        return ('見つかりませんでした')
    elif wareki_year == 1:
        return ("%s元年" % wareki)
    else:
        return ("%s%s年" % (wareki, wareki_year))


print(japanese_calendar_conversion(2000))
# 2000 => 平成12年
