"""
python -m tests.test_rn
"""
from src.renumnum import renumnum as rn


# リナンバリンギスト番号の生成
vec1 = rn.vec(1, 2)
vec2 = rn.vec((1, 2))
print(f"{vec1.elements}")                # (1, 2, 0)
print(f"{vec2.elements}")                # (1, 2, 0)
if f"{vec1.elements}" != f"{vec2.elements}":
    raise ValueError(f"{vec1.elements=} != {vec2.elements=}")

vec1 = rn.vec(3)
vec2 = rn.vec((3))
print(f"{vec1.elements}")                # (3, 0)
print(f"{vec2.elements}")                # (3, 0)
if f"{vec1.elements}" != f"{vec2.elements}":
    raise ValueError(f"{vec1.elements=} != {vec2.elements=}")


test_data = [
    # 種をまく
    ['rn.vec(1)', rn.vec(1), 'O1o0', (1, 0)],
    # ----------  ---------  ------  ------
    # 1           2          3       4
    # 1. Test case title
    # 2. Actual
    # 3. Expected Label
    # 4. Expected

    ['rn.vec(2)', rn.vec(2), 'O2o0', (2, 0)],

    # 正の整数
    ['1', rn.vec(1), 'O1', (1,)],

    # 正の整数の文字列
    ['"1"', rn.vec('1'), 'O1', (1,)],

    # 辞書順記数法
    ['"_9"', rn.vec('_9'), 'O_9', (-1,)],
    ['"A10"', rn.vec('A10'), 'OA10', (10,)],

    # 数珠玉記数法
    ['"O_9"', rn.vec('O_9'), 'O_9', (-1,)],
    ['"OA10"', rn.vec('OA10'), 'OA10', (10,)],
    ['"O_9o1oA10"', rn.vec('O_9o1oA10'), 'O_9o1oA10', (-1, 1, 10)],

    # 正の零
    ['0', rn.vec(0), 'O0', (0,)],
    # -   ---------   --   ----
    # 1   2           3    4
    # 1. Test case text
    # 2. Actual
    # 3. Expected Label
    # 4. Expected

    # 正の整数
    ['1', rn.vec(1), 'O1', (1,)],
    ['10', rn.vec(10), 'OA10', (10,)],

    # 正の整数の文字列
    ['"0"', rn.vec('0'), 'O0', (0,)],
    ['"1"', rn.vec('1'), 'O1', (1,)],
    ['"10"', rn.vec('10'), 'OA10', (10,)],

    # O1o2 の形
    ['"O1o2o_9"', rn.vec('O1o2o_9'), 'O1o2o_9', (1, 2, -1)],
    ['"O1o2"', rn.vec('O1o2'), 'O1o2', (1, 2)],
    ['"O1o2oA10o4"', rn.vec('O1o2oA10o4'), 'O1o2oA10o4', (1, 2, 10, 4)],

    # o1o2 の形, snake_case への寛容
    ['"o1o2o_9"', rn.vec('o1o2o_9'), 'O1o2o_9', (1, 2, -1)],
    ['"o1o2"', rn.vec('o1o2'), 'O1o2', (1, 2)],
    ['"o1o2oA10o4"', rn.vec('o1o2oA10o4'), 'O1o2oA10o4', (1, 2, 10, 4)],

    # O1O2 の形
    ['"O1O2O_9"', rn.vec('O1O2O_9'), 'O1o2o_9', (1, 2, -1)],
    ['"O1O2"', rn.vec('O1O2'), 'O1o2', (1, 2)],
    ['"O1O2OA10O4"', rn.vec('O1O2OA10O4'), 'O1o2oA10o4', (1, 2, 10, 4)],

    # 混在
    ['"o_9O1oA10"', rn.vec('o_9O1oA10'), 'O_9o1oA10', (-1, 1, 10)],

    # 拡張: 辞書順記数法への寛容
    ['"A77"', rn.vec('A77'), 'OA77', (77,)],
    ['"AA777"', rn.vec('AA777'), 'OAA777', (777,)],
    ['"O7oA77oAA777oAAA7777"', rn.vec(
        'O7oA77oAA777oAAA7777'), 'O7oA77oAA777oAAA7777', (7, 77, 777, 7777)],

    ['"a77"', rn.vec('a77'), 'OA77', (77,)],
    ['"aa777"', rn.vec('aa777'), 'OAA777', (777,)],
    ['"o7oa77oaa777oaaa7777"', rn.vec(
        'O7oa77oaa777oaaa7777'), 'O7oA77oAA777oAAA7777', (7, 77, 777, 7777)],

    # タプル
    ['(1,2)', rn.vec((1, 2)), 'O1o2', (1, 2)],
    ['(1,2,-3)', rn.vec((1, 2, -3)), 'O1o2o_7', (1, 2, -3)],
    ['(1,2,10,4)', rn.vec((1, 2, 10, 4)), 'O1o2oA10o4', (1, 2, 10, 4)],
]

for datum in test_data:
    if f'{datum[1]}' == datum[2] and datum[1].elements == datum[3]:
        print(f'{datum[0]} --> "{datum[1]}" {datum[1].elements}')
    else:
        print(
            f'[Error] {datum[0]} --> "{datum[1]}" {datum[1].elements} Expected: "{datum[2]}" {datum[3]}')

# "2oo1" は使えない
try:
    print(f'[Error] "2oo1" --> {rn.vec("2oo1")}')
except:
    print(f'"2oo1" is not rn.vec')
