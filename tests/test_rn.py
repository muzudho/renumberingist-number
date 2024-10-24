"""
python -m tests.test_rn
"""

import sys  # テスト用

# 実際には、
#
#   import renumnum as rn
#
# のように書きたい。
# テストでは以下のように書く
from src.renumnum import renumnum_in_src as rn


# リナンバリンギスト番号の変数名は何でも構いませんがとりあえず oo としてみましょう
try:
    oo = rn.num()

    # 例外が投げられてこなかったらエラー
    raise ValueError('no parameter most be error')

except ValueError as e:
    if str(e) != 'specify one or more arguments':
        raise ValueError('no parameter most be error') from e

    # 例外が投げられてくるのが正しい。ここを抜ける

except:
    raise ValueError('no parameter most be error') from e


# リナンバリンギスト番号の生成
oo1 = rn.num(1, 2)
oo2 = rn.num((1, 2))
print(str(oo1))            # O1o2o0
print(str(oo2))            # O1o2o0
print(f"{oo1.totuple()}")   # (1, 2)
print(f"{oo2.totuple()}")   # (1, 2)
if oo1.totuple() != (1, 2) or f"{oo1.totuple()}" != f"{oo2.totuple()}":
    raise ValueError(f"{oo1.totuple()=}  {oo1.totuple()=} != {oo2.totuple()=}")

oo1 = rn.num(3)
oo2 = rn.num((3))
print(str(oo1))            # O3o0
print(str(oo2))            # O3o0
print(f"{oo1.totuple()}")   # (3, 0)
print(f"{oo2.totuple()}")   # (3, 0)
if f"{oo1.totuple()}" != f"{oo2.totuple()}":
    raise ValueError(f"{oo1.totuple()=} != {oo2.totuple()=}")


# 文字列出力の確認
# ----------------
oo = rn.num(1)
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')

oo = rn.num(1, 2)
print(str(oo))     # O1o2o0
if str(oo) != 'O1o2o0':
    raise ValueError(f'{oo=}')

oo = rn.num('1')
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')

#oo = rn.num('1, 2')   # error

# 辞書順番号（Dictionary order number）。末尾に o0 が付いていなくても、辞書順番号として有効です
oo = rn.num('_9')
print(str(oo))     # O_9o0
if str(oo) != 'O_9o0':
    raise ValueError(f'{oo=}')

oo = rn.num('A10')
print(str(oo))     # OA10o0
if str(oo) != 'OA10o0':
    raise ValueError(f'{oo=}')

# 数珠玉記数法（Beads notation）。末尾に o0 が付いていなくても、数珠玉記数法として有効です
oo = rn.num('O0')
print(str(oo))     # O0o0
if str(oo) != 'O0o0':
    raise ValueError(f'{oo=}')

oo = rn.num('O1')
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')

# リナンバリンギスト番号
oo = rn.num('O0o0')
print(str(oo))     # O0o0
if str(oo) != 'O0o0':
    raise ValueError(f'{oo=}')

oo = rn.num('O1o0')
print(str(oo))     # O1o0
if str(oo) != 'O1o0':
    raise ValueError(f'{oo=}')


# タプル、リストへの出力確認
# --------------------------
oo = rn.num(1)
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (1,)  [1]
if tpl != (1,) or vec != [1]:
    raise ValueError(f'{oo=}  {vec=}')

oo = rn.num(1, 2)
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (1, 2)  [1, 2]
if tpl != (1, 2) or vec != [1, 2]:
    raise ValueError(f'{oo=}  {vec=}')

oo = rn.num('1')
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (1,)  [1]
if tpl != (1,) or vec != [1]:
    raise ValueError(f'{oo=}  {vec=}')

# 辞書順番号（Dictionary order number）。末尾に o0 が付いていなくても、辞書順番号として有効です
oo = rn.num('_9')
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (-1,)  [-1]
if tpl != (-1,) or vec != [-1]:
    raise ValueError(f'{oo=}  {vec=}')

oo = rn.num('A10')
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (10,)  [10]
if tpl != (10,) or vec != [10]:
    raise ValueError(f'{oo=}  {vec=}')

# 数珠玉記数法（Beads notation）。末尾に o0 が付いていなくても、数珠玉記数法として有効です
oo = rn.num('O0')
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (0,)  [0]
if tpl != (0,) or vec != [0]:
    raise ValueError(f'{oo=}  {vec=}')

oo = rn.num('O1')
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (1,)  [1]
if tpl != (1,) or vec != [1]:
    raise ValueError(f'{oo=}  {vec=}')

# リナンバリンギスト番号
oo = rn.num('O0o0')
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (0,)  [0]
if tpl != (0,) or vec != [0]:
    raise ValueError(f'{oo=}  {vec=}')

oo = rn.num('O1o0')
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (1,)  [1]
if tpl != (1,) or vec != [1]:
    raise ValueError(f'{oo=}  {vec=}')

# タプル
oo = rn.num((1, 2))
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (1, 2)  [1, 2]
if tpl != (1, 2) or vec != [1, 2]:
    raise ValueError(f'{oo=}  {vec=}')

# リスト
oo = rn.num([1, 2])
tpl = oo.totuple()
vec = oo.tolist()
print(f"{tpl=}  {vec=}")     # (1, 2)  [1, 2]
if tpl != (1, 2) or vec != [1, 2]:
    raise ValueError(f'{oo=}  {vec=}')



# 比較
print("O1o0 < O2o0")
oo1 = rn.num('O1o0')
oo2 = rn.num('O2o0')
print(oo1 < oo2)        # True

print("O1o0 < O1o0o0")
oo1 = rn.num('O1o0')
oo2 = rn.num('O1o0o0')
print(oo1 < oo2)        # True


# 比較演算子の確認 '<'
# --------------------
test_data = [
    (rn.num([-2]), rn.num([-1])),
    (rn.num([-1]), rn.num([0])),
    (rn.num([0]), rn.num([1])),
    (rn.num([1]), rn.num([2])),
    (rn.num([-2]), rn.num([2])),

    (rn.num([0, -2]), rn.num([0, -1])),
    (rn.num([0, -1]), rn.num([0, 0])),
    (rn.num([0, 0]), rn.num([0, 1])),
    (rn.num([0, 1]), rn.num([0, 2])),
    (rn.num([0, -2]), rn.num([0, 2])),

    (rn.num([0, 0, 0]), rn.num([0, 0, 1])),
    (rn.num([0, 0, 0, 1]), rn.num([0, 0, 1, 0])),
    (rn.num([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1]),
     rn.num([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 2])),

    (rn.num([0, -1]), rn.num([0])),
    (rn.num([0]), rn.num([0, 1])),

    # 特殊系
    (rn.num([0]), rn.num([0, 0])),
    (rn.num([0, 0]), rn.num([0, 0, 0])),
    (rn.num([0]), rn.num([0, 0, 0])),
]

# ホワイトボックステスト
# for datum in test_data:
#     print(f"{datum[0].tolist()} compare {datum[1].tolist()}. compare is {datum[0]._kind_of_compare(datum[1])}")

for datum in test_data:
    if not datum[0] < datum[1]:
        raise ValueError(f'{str(datum[0])} < {str(datum[1])} is False. {datum[0].tolist()}, {datum[1].tolist()}')


    if datum[0] > datum[1]:
        raise ValueError(f'{str(datum[0])} > {str(datum[1])} is True. {datum[0].tolist()}, {datum[1].tolist()}')


    if not datum[0] <= datum[1]:
        raise ValueError(f'{str(datum[0])} <= {str(datum[1])} is False. {datum[0].tolist()}, {datum[1].tolist()}')


    if datum[0] >= datum[1]:
        raise ValueError(f'{str(datum[0])} >= {str(datum[1])} is True. {datum[0].tolist()}, {datum[1].tolist()}')


    if datum[0] == datum[1]:
        raise ValueError(f'{str(datum[0])} == {str(datum[1])} is True. {datum[0].tolist()}, {datum[1].tolist()}')


    if not datum[0] != datum[1]:
        raise ValueError(f'{str(datum[0])} != {str(datum[1])} is False. {datum[0].tolist()}, {datum[1].tolist()}')


# 比較演算子の確認 '=='
# ---------------------
test_data = [
    (rn.num([-1]), rn.num([-1])),
    (rn.num([0]), rn.num([0])),
    (rn.num([1]), rn.num([1])),

    (rn.num([0, -1]), rn.num([0, -1])),
    (rn.num([0, 0]), rn.num([0, 0])),
    (rn.num([0, 1]), rn.num([0, 1])),

    (rn.num([-1, 0, 1]), rn.num([-1, 0, 1])),
    (rn.num([-1, 0, 1, 10]), rn.num([-1, 0, 1, 10])),
]

for datum in test_data:
    if datum[0] < datum[1]:
        raise ValueError(f'{str(datum[0])} < {str(datum[1])} is True. {datum[0].tolist()}, {datum[1].tolist()}')


    if datum[0] > datum[1]:
        raise ValueError(f'{str(datum[0])} > {str(datum[1])} is True. {datum[0].tolist()}, {datum[1].tolist()}')


    if not datum[0] <= datum[1]:
        raise ValueError(f'{str(datum[0])} <= {str(datum[1])} is False. {datum[0].tolist()}, {datum[1].tolist()}')


    if not datum[0] >= datum[1]:
        raise ValueError(f'{str(datum[0])} >= {str(datum[1])} is False. {datum[0].tolist()}, {datum[1].tolist()}')


    if not datum[0] == datum[1]:
        raise ValueError(f'{str(datum[0])} == {str(datum[1])} is False. {datum[0].tolist()}, {datum[1].tolist()}')


    if datum[0] != datum[1]:
        raise ValueError(f'{str(datum[0])} != {str(datum[1])} is True. {datum[0].tolist()}, {datum[1].tolist()}')


test_data = [
    # 種をまく
    ['rn.num(1)', rn.num(1), 'O1o0', (1,), [1]],
    # ----------  ---------  ------  ----  ---
    # 1           2          3       4     5
    # 1. Test case title
    # 2. Actual
    # 3. Expected Label
    # 4. Expected tuple
    # 5. Expected list

    ['rn.num(2)', rn.num(2), 'O2o0', (2,), [2]],

    # 正の整数
    ['1', rn.num(1), 'O1o0', (1,), [1]],

    # 正の整数の文字列
    ['"1"', rn.num('1'), 'O1o0', (1,), [1]],

    # 辞書順記数法
    ['"_9"', rn.num('_9'), 'O_9o0', (-1,), [-1]],
    ['"A10"', rn.num('A10'), 'OA10o0', (10,), [10]],

    # 数珠玉記数法
    ['"O_9"', rn.num('O_9'), 'O_9o0', (-1,), [-1]],
    ['"OA10"', rn.num('OA10'), 'OA10o0', (10,), [10]],
    ['"O_9o1oA10"', rn.num('O_9o1oA10'), 'O_9o1oA10o0', (-1, 1, 10), [-1, 1, 10]],

    # 正の零
    ['0', rn.num(0), 'O0o0', (0,), [0]],
    # -   ---------  ------  ----  ---
    # 1   2          3       4     5
    # 1. Test case text
    # 2. Actual
    # 3. Expected Label
    # 4. Expected tuple
    # 5. Expected list

    # 正の整数
    ['1', rn.num(1), 'O1o0', (1,), [1]],
    ['10', rn.num(10), 'OA10o0', (10,), [10]],

    # 正の整数の文字列
    ['"0"', rn.num('0'), 'O0o0', (0,), [0]],
    ['"1"', rn.num('1'), 'O1o0', (1,), [1]],
    ['"10"', rn.num('10'), 'OA10o0', (10,), [10]],

    # O1o2 の形
    ['"O1o2o_9"', rn.num('O1o2o_9'), 'O1o2o_9o0', (1, 2, -1), [1, 2, -1]],
    ['"O1o2"', rn.num('O1o2'), 'O1o2o0', (1, 2), [1, 2]],
    ['"O1o2oA10o4"', rn.num('O1o2oA10o4'), 'O1o2oA10o4o0', (1, 2, 10, 4), [1, 2, 10, 4]],

    # o1o2 の形, snake_case への寛容
    ['"o1o2o_9"', rn.num('o1o2o_9'), 'O1o2o_9o0', (1, 2, -1), [1, 2, -1]],
    ['"o1o2"', rn.num('o1o2'), 'O1o2o0', (1, 2), [1, 2]],
    ['"o1o2oA10o4"', rn.num('o1o2oA10o4'), 'O1o2oA10o4o0', (1, 2, 10, 4), [1, 2, 10, 4]],

    # O1O2 の形
    ['"O1O2O_9"', rn.num('O1O2O_9'), 'O1o2o_9o0', (1, 2, -1), [1, 2, -1]],
    ['"O1O2"', rn.num('O1O2'), 'O1o2o0', (1, 2), [1, 2]],
    ['"O1O2OA10O4"', rn.num('O1O2OA10O4'), 'O1o2oA10o4o0', (1, 2, 10, 4), [1, 2, 10, 4]],

    # 混在
    ['"o_9O1oA10"', rn.num('o_9O1oA10'), 'O_9o1oA10o0', (-1, 1, 10), [-1, 1, 10]],

    # 拡張: 辞書順記数法への寛容
    ['"A77"', rn.num('A77'), 'OA77o0', (77,), [77]],
    ['"AA777"', rn.num('AA777'), 'OAA777o0', (777,), [777]],
    ['"O7oA77oAA777oAAA7777"', rn.num(
        'O7oA77oAA777oAAA7777'), 'O7oA77oAA777oAAA7777o0', (7, 77, 777, 7777), [7, 77, 777, 7777]],

    ['"a77"', rn.num('a77'), 'OA77o0', (77,), [77]],
    ['"aa777"', rn.num('aa777'), 'OAA777o0', (777,), [777]],
    ['"o7oa77oaa777oaaa7777"', rn.num(
        'O7oa77oaa777oaaa7777'), 'O7oA77oAA777oAAA7777o0', (7, 77, 777, 7777), [7, 77, 777, 7777]],

    # タプル
    ['(1,2)', rn.num((1, 2)), 'O1o2o0', (1, 2), [1, 2]],
    ['(1,2,-3)', rn.num((1, 2, -3)), 'O1o2o_7o0', (1, 2, -3), [1, 2, -3]],
    ['(1,2,10,4)', rn.num((1, 2, 10, 4)), 'O1o2oA10o4o0', (1, 2, 10, 4), [1, 2, 10, 4]],

    # リスト
    ['[1,2]', rn.num([1, 2]), 'O1o2o0', (1, 2), [1, 2]],
    ['[1,2,-3]', rn.num([1, 2, -3]), 'O1o2o_7o0', (1, 2, -3), [1, 2, -3]],
    ['[1,2,10,4]', rn.num([1, 2, 10, 4]), 'O1o2oA10o4o0', (1, 2, 10, 4), [1, 2, 10, 4]],
]

for datum in test_data:
    if f'{datum[1]}' == datum[2] and datum[1].totuple() == datum[3] and datum[1].tolist() == datum[4]:
        print(f'{datum[0]} --> "{datum[1]}" {datum[1].totuple()} {datum[1].tolist()}')
    else:
        raise ValueError(
            f'[Error] {datum[0]} --> "{datum[1]}" {datum[1].totuple()} Expected: "{datum[2]}" {datum[3]} {datum[4]}')

# "2oo1" は使えない
try:
    print(f'[Error] "2oo1" --> {rn.num("2oo1")}')
except:
    print(f'"2oo1" is not rn.num, ok')
else:
    raise ValueError(f'"2oo1" is not rn.num')
