"""
python -m tests.test_don
"""
from src.renumberingist_number.dictionary_order_number import DictionaryOrderNumber as don

test_data = [
    # 正の零
    ['0', don(0), '0'],
    # --                ---
    # 1                 2
    # 1. Actual
    # 2. Expected

    # 正の整数
    ['9', don(9), '9', '9'],
    ['10', don(10), 'A10'],
    ['99', don(99), 'A99'],
    ['100', don(100), 'AA100'],
    ['999', don(999), 'AA999'],
    ['1000', don(1000), 'AAA1000'],

    # 負の零（正の零扱い）
    ['-0', don(-0), '0'],

    # 負の整数
    ['-1', don(-1), '_9'],
    ['-2', don(-2), '_8'],
    ['-9', don(-9), '_1'],
    ['-10', don(-10), '__90'],
    ['-99', don(-99), '__01'],
    ['-100', don(-100), '___900'],
    ['-999', don(-999), '___001'],
    ['-1000', don(-1000), '____9000'],
    ['-9999', don(-9999), '____0001'],

    # 正の整数の文字列
    ['"0"', don('0'), '0'],
    ['"9"', don('9'), '9'],
    ['"10"', don('10'), 'A10'],
    ['"99"', don('99'), 'A99'],
    ['"100"', don('100'), 'AA100'],
    ['"999"', don('999'), 'AA999'],
    ['"1000"', don('1000'), 'AAA1000'],

    # 負の整数の文字列
    ['"-0"', don('-0'), '0'],
    ['"-1"', don('-1'), '_9'],
    ['"-9"', don('-9'), '_1'],
    ['"-10"', don('-10'), '__90'],
    ['"-99"', don('-99'), '__01'],
    ['"-100"', don('-100'), '___900'],
    ['"-999"', don('-999'), '___001'],
    ['"-1000"', don('-1000'), '____9000'],

    # 辞書順記数法 正の整数
    ['"A77"', don('A77'), 'A77'],
    ['"AA777"', don('AA777'), 'AA777'],
    ['"AAA7777"', don('AAA7777'), 'AAA7777'],
    ['"AAAA77777"', don('AAAA77777'), 'AAAA77777'],

    # 辞書順記数法 負の整数
    ['"__88"', don('__88'), '__88'],
    ['"___888"', don('___888'), '___888'],
    ['"____8888"', don('____8888'), '____8888'],
    ['"_____88888"', don('_____88888'), '_____88888'],

    # 小文字, snake_case への寛容
    ['"a77"', don('a77'), 'A77'],
    ['"aa777"', don('aa777'), 'AA777'],
    ['"aaa7777"', don('aaa7777'), 'AAA7777'],
    ['"aaaa77777"', don('aaaa77777'), 'AAAA77777'],
]

for datum in test_data:
    if f'{datum[1]}' == datum[2]:
        print(f'{datum[0]} --> "{datum[1]}" {datum[1].number}')
    else:
        print(
            f'[Error] {datum[0]} --> "{datum[1]}" {datum[1].number} Expected: "{datum[2]}"')

# 間違ったAの個数を例外にできるか確認します
try:
    print(f'[Error] "A1" --> {don("A1")}')
except:
    print(f'"A1" is not don')

try:
    print(f'[Error] "AA10" --> {don("AA10")}')
except:
    print(f'"AA10" is not don')

# 間違った '_' の個数を例外にできるか確認します
try:
    print(f'[Error] "_90" --> {don("_90")}')
except:
    print(f'"_90" is not don')

try:
    print(f'[Error] "__900" --> {don("__900")}')
except:
    print(f'"__900" is not don')

# 'A' と '_' の混合を例外にできるか確認します
try:
    print(f'[Error] "_A90" --> {don("_A90")}')
except:
    print(f'"_A90" is not don')

try:
    print(f'[Error] "A_90" --> {don("A_90")}')
except:
    print(f'"A_90" is not don')
