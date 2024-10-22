"""
python -m tests.test_rn
"""
# 実際には、
#
#   import renumnum as rn
#
# のように書きたい。
# テストでは以下のように書く
from src.renumnum import renumnum_in_src as rn


# リナンバリンギスト番号の変数名は何でも構いませんがとりあえず oo としてみましょう

# リナンバリンギスト番号の生成
oo1 = rn.vec(1, 2)
oo2 = rn.vec((1, 2))
print(str(oo1))            # O1o2o0
print(str(oo2))            # O1o2o0
print(f"{oo1.elements}")   # (1, 2, 0)
print(f"{oo2.elements}")   # (1, 2, 0)
if f"{oo1.elements}" != f"{oo2.elements}":
    raise ValueError(f"{oo1.elements=} != {oo2.elements=}")

oo1 = rn.vec(3)
oo2 = rn.vec((3))
print(str(oo1))            # O3o0
print(str(oo2))            # O3o0
print(f"{oo1.elements}")   # (3, 0)
print(f"{oo2.elements}")   # (3, 0)
if f"{oo1.elements}" != f"{oo2.elements}":
    raise ValueError(f"{oo1.elements=} != {oo2.elements=}")


# 文字列出力の確認
# ----------------
oo = rn.vec(1)
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')

oo = rn.vec(1, 2)
print(str(oo))     # O1o2o0
if str(oo) != 'O1o2o0':
    raise ValueError(f'{oo=}')

oo = rn.vec('1')
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')

#oo = rn.vec('1, 2')   # error

# 辞書順番号（Dictionary order number）。末尾に o0 が付いていなくても、辞書順番号として有効です
oo = rn.vec('_9')
print(str(oo))     # O_9o0
if str(oo) != 'O_9o0':
    raise ValueError(f'{oo=}')

oo = rn.vec('A10')
print(str(oo))     # OA10o0
if str(oo) != 'OA10o0':
    raise ValueError(f'{oo=}')

# 数珠玉記数法（Beads notation）。末尾に o0 が付いていなくても、数珠玉記数法として有効です
oo = rn.vec('O0')
print(str(oo))     # O0o0
if str(oo) != 'O0o0':
    raise ValueError(f'{oo=}')

oo = rn.vec('O1')
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')

# リナンバリンギスト番号
oo = rn.vec('O0o0')
print(str(oo))     # O0o0
if str(oo) != 'O0o0':
    raise ValueError(f'{oo=}')

oo = rn.vec('O1o0')
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')


# TODO ベクターの出力確認
# ------------------
oo = rn.vec(1)
vect = oo.to_vector()
print(vect)     # [1]
if vect != [1]:
    raise ValueError(f'{oo=}  {vect=}')

oo = rn.vec(1, 2)
vect = oo.to_vector()
print(vect)     # [1, 2]
if vect != [1, 2]:
    raise ValueError(f'{oo=}  {vect=}')

oo = rn.vec('1')
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')

#oo = rn.vec('1, 2')   # error

# 辞書順番号（Dictionary order number）。末尾に o0 が付いていなくても、辞書順番号として有効です
oo = rn.vec('_9')
print(str(oo))     # O_9o0
if str(oo) != 'O_9o0':
    raise ValueError(f'{oo=}')

oo = rn.vec('A10')
print(str(oo))     # OA10o0
if str(oo) != 'OA10o0':
    raise ValueError(f'{oo=}')

# 数珠玉記数法（Beads notation）。末尾に o0 が付いていなくても、数珠玉記数法として有効です
oo = rn.vec('O0')
print(str(oo))     # O0o0
if str(oo) != 'O0o0':
    raise ValueError(f'{oo=}')

oo = rn.vec('O1')
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')

# リナンバリンギスト番号
oo = rn.vec('O0o0')
print(str(oo))     # O0o0
if str(oo) != 'O0o0':
    raise ValueError(f'{oo=}')

oo = rn.vec('O1o0')
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')



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
    ['1', rn.vec(1), 'O1o0', (1, 0)],

    # 正の整数の文字列
    ['"1"', rn.vec('1'), 'O1o0', (1, 0)],

    # 辞書順記数法
    ['"_9"', rn.vec('_9'), 'O_9o0', (-1, 0)],
    ['"A10"', rn.vec('A10'), 'OA10o0', (10, 0)],

    # 数珠玉記数法
    ['"O_9"', rn.vec('O_9'), 'O_9o0', (-1, 0)],
    ['"OA10"', rn.vec('OA10'), 'OA10o0', (10, 0)],
    ['"O_9o1oA10"', rn.vec('O_9o1oA10'), 'O_9o1oA10o0', (-1, 1, 10, 0)],

    # 正の零
    ['0', rn.vec(0), 'O0o0', (0, 0)],
    # -   ---------  ------  ------
    # 1   2          3       4
    # 1. Test case text
    # 2. Actual
    # 3. Expected Label
    # 4. Expected

    # 正の整数
    ['1', rn.vec(1), 'O1o0', (1, 0)],
    ['10', rn.vec(10), 'OA10o0', (10, 0)],

    # 正の整数の文字列
    ['"0"', rn.vec('0'), 'O0o0', (0, 0)],
    ['"1"', rn.vec('1'), 'O1o0', (1, 0)],
    ['"10"', rn.vec('10'), 'OA10o0', (10, 0)],

    # O1o2 の形
    ['"O1o2o_9"', rn.vec('O1o2o_9'), 'O1o2o_9o0', (1, 2, -1, 0)],
    ['"O1o2"', rn.vec('O1o2'), 'O1o2o0', (1, 2, 0)],
    ['"O1o2oA10o4"', rn.vec('O1o2oA10o4'), 'O1o2oA10o4o0', (1, 2, 10, 4, 0)],

    # o1o2 の形, snake_case への寛容
    ['"o1o2o_9"', rn.vec('o1o2o_9'), 'O1o2o_9o0', (1, 2, -1, 0)],
    ['"o1o2"', rn.vec('o1o2'), 'O1o2o0', (1, 2, 0)],
    ['"o1o2oA10o4"', rn.vec('o1o2oA10o4'), 'O1o2oA10o4o0', (1, 2, 10, 4, 0)],

    # O1O2 の形
    ['"O1O2O_9"', rn.vec('O1O2O_9'), 'O1o2o_9o0', (1, 2, -1, 0)],
    ['"O1O2"', rn.vec('O1O2'), 'O1o2o0', (1, 2, 0)],
    ['"O1O2OA10O4"', rn.vec('O1O2OA10O4'), 'O1o2oA10o4o0', (1, 2, 10, 4, 0)],

    # 混在
    ['"o_9O1oA10"', rn.vec('o_9O1oA10'), 'O_9o1oA10o0', (-1, 1, 10, 0)],

    # 拡張: 辞書順記数法への寛容
    ['"A77"', rn.vec('A77'), 'OA77o0', (77, 0)],
    ['"AA777"', rn.vec('AA777'), 'OAA777o0', (777, 0)],
    ['"O7oA77oAA777oAAA7777"', rn.vec(
        'O7oA77oAA777oAAA7777'), 'O7oA77oAA777oAAA7777o0', (7, 77, 777, 7777, 0)],

    ['"a77"', rn.vec('a77'), 'OA77o0', (77, 0)],
    ['"aa777"', rn.vec('aa777'), 'OAA777o0', (777, 0)],
    ['"o7oa77oaa777oaaa7777"', rn.vec(
        'O7oa77oaa777oaaa7777'), 'O7oA77oAA777oAAA7777o0', (7, 77, 777, 7777, 0)],

    # タプル
    ['(1,2)', rn.vec((1, 2)), 'O1o2o0', (1, 2, 0)],
    ['(1,2,-3)', rn.vec((1, 2, -3)), 'O1o2o_7o0', (1, 2, -3, 0)],
    ['(1,2,10,4)', rn.vec((1, 2, 10, 4)), 'O1o2oA10o4o0', (1, 2, 10, 4, 0)],
]

for datum in test_data:
    if f'{datum[1]}' == datum[2] and datum[1].elements == datum[3]:
        print(f'{datum[0]} --> "{datum[1]}" {datum[1].elements}')
    else:
        raise ValueError(
            f'[Error] {datum[0]} --> "{datum[1]}" {datum[1].elements} Expected: "{datum[2]}" {datum[3]}')

# "2oo1" は使えない
try:
    print(f'[Error] "2oo1" --> {rn.vec("2oo1")}')
except:
    print(f'"2oo1" is not rn.vec, ok')
else:
    raise ValueError(f'"2oo1" is not rn.vec')
