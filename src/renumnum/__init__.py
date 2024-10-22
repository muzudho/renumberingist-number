import re
from .beads_view import BeadsView
from .dictionary_order_number import DictionaryOrderNumber


class RenumNum:
    """リナンバー主義者の番号"""

    # めんどくさいので .upper() して 'O' と数字で構成されていればOkとする
    # 辞書順記数法に対応するために、めんどくさいので '_', 'A' が含まれていてもOkとする
    __pattern1 = re.compile(r"^([_AO\d]*)$")

    @staticmethod
    def trail_zero(*args):
        """With trailing zero

        Parameters
        ----------
        *args : tuple
            可変長引数
        """

        element_list = None

        # 引数が０個か？
        if len(args) < 1:
            raise ValueError('specify one or more arguments')

        # 引数が１つか？
        elif len(args) == 1:
            try:
                # 整数かどうか判定
                int_value = int(str(args[0]), 10)

            # 整数ではなかったら
            except ValueError:
                # タプル型なら
                if type(args[0]) is tuple:
                    # いったんリストに戻す
                    element_list = list(args[0])

                # TODO 整数ではなかったら
                else:
                    # 文字列と想定して解析を進める
                    element_list = RenumNum.convert_str_to_list(args[0])

            # 整数だったら
            else:
                # リストに変換する
                element_list = []
                element_list.append(int_value)

        # 引数が複数個か？
        else:
            # リストに変換する
            element_list = []
            element_list.extend(list(args))

        # 0 の要素を追加
        element_list.append(0)

        # タプルに変換して使う
        return RenumNum(tuple(element_list))

    @staticmethod
    def convert_str_to_list(text):
        # 大文字に変換
        text = text.upper()

        # '_', 'A', 'O' と数字で構成されている必要がある
        result = RenumNum.__pattern1.match(text)
        if result:
            pass
        else:
            raise ValueError(f"not cyber vector: {text}")

        # 先頭に O が付いているのは構わないものとし、
        # 先頭に付いている O は削除する
        text = text.lstrip('O')

        new_element_list = []

        # 区切り文字 O で分割
        tokens = text.split('O')

        for token in tokens:
            if token[:1] == 'A':
                # A を除去する
                n = int(token.replace('A', ''))
                new_element_list.append(n)

            elif token[:1] == '_':
                # まず '_' を除去する
                token = token.replace('_', '')

                figure = len(token)
                modulo = 1
                for i in range(0, figure):
                    modulo *= 10

                z = -1 * (modulo - int(token))
                new_element_list.append(z)

            else:
                n = int(token)
                new_element_list.append(n)

        return new_element_list

    def __init__(self, *args):
        """初期化

        Parameters
        ----------
        *args : tuple
            可変長引数
        """

        # 引数が０個か？
        if len(args) < 1:
            raise ValueError('specify one or more arguments')

        # 引数が１つか？
        elif len(args) == 1:
            try:
                # 整数かどうか判定
                int_value = int(str(args[0]), 10)

            # 整数ではなかったら
            except ValueError:
                # タプル型なら
                if type(args[0]) is tuple:
                    # そのまま渡す
                    self._beadsv = BeadsView(args[0])

                # 文字列と想定して解析を進める
                else:
                    element_list = RenumNum.convert_str_to_list(args[0])
                    # タプルに変換して渡す
                    self._beadsv = BeadsView(tuple(element_list))

            # 整数だったら
            else:
                # そのまま渡す
                self._beadsv = BeadsView(int_value)
        
        # 引数が複数個か？
        else:
            # そのまま渡す
            self._beadsv = BeadsView(args)


    def __str__(self):
        """辞書順記数法 と 数珠玉記数法 の併用"""
        text = ""
        for token in self.elements:
            text = f"{text}o{DictionaryOrderNumber(token)}"

        # 先頭だけを大文字の 'O' にする
        text = f"O{text[1:]}"
        return text

    @property
    def elements(self):
        return self._beadsv.elements
