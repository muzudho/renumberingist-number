"""
python -m tests.test_rn
"""
from src.renumberingist_number import RenumberingistNumber as RN

cn = RN.trail_zero((1, 2))
print(f"{cn.elements}")                # (1, 2, 0)

cn = RN.trail_zero(3)
print(f"{cn.elements}")                # (3, 0)

cn = RN((1, 2, 0))
print(f"{cn.elements}")                # (1, 2, 0)

cn = RN((3, 0))
print(f"{cn.elements}")                # (3, 0)

test_data = [
    # 種をまく
    ['RN.trail_zero(1)', RN.trail_zero(1), 'O1o0', (1, 0)],
    # ----------------------   -----------------------  ----   ------
    # 1                        2                        3      3
    # 1. Test case title
    # 2. Actual
    # 3. Expected

    ['RN.trail_zero(2)', RN.trail_zero(2), 'O2o0', (2, 0)],

    # 正の整数
    ['1', RN(1), 'O1', (1,)],

    # 正の整数の文字列
    ['"1"', RN('1'), 'O1', (1,)],

    # 辞書順記数法
    ['"_9"', RN('_9'), 'O_9', (-1,)],
    ['"A10"', RN('A10'), 'OA10', (10,)],

    # 数珠玉記数法
    ['"O_9"', RN('O_9'), 'O_9', (-1,)],
    ['"OA10"', RN('OA10'), 'OA10', (10,)],
    ['"O_9o1oA10"', RN('O_9o1oA10'), 'O_9o1oA10', (-1, 1, 10)],

    # 正の零
    ['0', RN(0), 'O0', (0,)],
    # -   -----------   --   ----
    # 1   2             3    3
    # 1. Test case text
    # 2. Actual
    # 3. Expected

    # 正の整数
    ['1', RN(1), 'O1', (1,)],
    ['10', RN(10), 'OA10', (10,)],

    # 正の整数の文字列
    ['"0"', RN('0'), 'O0', (0,)],
    ['"1"', RN('1'), 'O1', (1,)],
    ['"10"', RN('10'), 'OA10', (10,)],

    # O1o2 の形
    ['"O1o2o_9"', RN('O1o2o_9'), 'O1o2o_9', (1, 2, -1)],
    ['"O1o2"', RN('O1o2'), 'O1o2', (1, 2)],
    ['"O1o2oA10o4"', RN('O1o2oA10o4'), 'O1o2oA10o4', (1, 2, 10, 4)],

    # o1o2 の形, snake_case への寛容
    ['"o1o2o_9"', RN('o1o2o_9'), 'O1o2o_9', (1, 2, -1)],
    ['"o1o2"', RN('o1o2'), 'O1o2', (1, 2)],
    ['"o1o2oA10o4"', RN('o1o2oA10o4'), 'O1o2oA10o4', (1, 2, 10, 4)],

    # O1O2 の形
    ['"O1O2O_9"', RN('O1O2O_9'), 'O1o2o_9', (1, 2, -1)],
    ['"O1O2"', RN('O1O2'), 'O1o2', (1, 2)],
    ['"O1O2OA10O4"', RN('O1O2OA10O4'), 'O1o2oA10o4', (1, 2, 10, 4)],

    # 混在
    ['"o_9O1oA10"', RN('o_9O1oA10'), 'O_9o1oA10', (-1, 1, 10)],

    # 拡張: 辞書順記数法への寛容
    ['"A77"', RN('A77'), 'OA77', (77,)],
    ['"AA777"', RN('AA777'), 'OAA777', (777,)],
    ['"O7oA77oAA777oAAA7777"', RN(
        'O7oA77oAA777oAAA7777'), 'O7oA77oAA777oAAA7777', (7, 77, 777, 7777)],

    ['"a77"', RN('a77'), 'OA77', (77,)],
    ['"aa777"', RN('aa777'), 'OAA777', (777,)],
    ['"o7oa77oaa777oaaa7777"', RN(
        'O7oa77oaa777oaaa7777'), 'O7oA77oAA777oAAA7777', (7, 77, 777, 7777)],

    # タプル
    ['(1,2)', RN((1, 2)), 'O1o2', (1, 2)],
    ['(1,2,-3)', RN((1, 2, -3)), 'O1o2o_7', (1, 2, -3)],
    ['(1,2,10,4)', RN((1, 2, 10, 4)), 'O1o2oA10o4', (1, 2, 10, 4)],
]

for datum in test_data:
    if f'{datum[1]}' == datum[2] and datum[1].elements == datum[3]:
        print(f'{datum[0]} --> "{datum[1]}" {datum[1].elements}')
    else:
        print(
            f'[Error] {datum[0]} --> "{datum[1]}" {datum[1].elements} Expected: "{datum[2]}" {datum[3]}')

# "2oo1" は使えない
try:
    print(f'[Error] "2oo1" --> {RN("2oo1")}')
except:
    print(f'"2oo1" is not RN')
