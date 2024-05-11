import re

# 1. 関数とオブジェクト
# 1-1. compile
""" re.compile ----------------------------------------------------------- """
# 関数:
# 　　　re.compile(pattern, flags=0)
#
# 説明: 正規表現パターンを 正規表現オブジェクト にコンパイルします。
# 　　　メソッドを使ってマッチングに使えるようにします。

# """
pattern = re.compile(r"d")

# matchを使って正規表現が文字列の先頭にマッチするかを検索します。
match = pattern.search("dog")
if match:
    print("マッチが見つかりました:", match.group())
    print("マッチの開始位置:", match.start())
    print("マッチの終了位置:", match.end())
    print("マッチの位置:", match.span())
else:
    print("マッチが見つかりませんでした")

# 出力：
#    マッチが見つかりました: d
#    マッチの開始位置: 0
#    マッチの終了位置: 1
#    マッチの位置: (0, 1)
# """


# 1-2. search
""" re.search ------------------------------------------------------------ """
# 関数:
# 　　　re.search(pattern, string, flags=0)
# メソッド:
# 　　　Pattern.search(string[, pos[, endpos]])
#
# 説明: string 検索して、正規表現とマッチ(一致)する最初の位置を探して、
# 　　　対応する Match を返します。

# """
pattern = re.compile(r"dog")

# searchを使って正規表現が文字列内に存在するかを検索します。
# ただし、一度マッチすると検索は終了します。
search = pattern.search("I have a dog named Rover.")

if search:
    print("マッチが見つかりました:", search.group())
    print("マッチの開始位置:", search.start())
    print("マッチの終了位置:", search.end())
    print("マッチの位置:", search.span())
else:
    print("マッチが見つかりませんでした。")

# 出力：
#    マッチが見つかりました: dog
#    マッチの開始位置: 9
#    マッチの終了位置: 12
#    マッチの位置: (9, 12)
# """


# 1-3. match
""" re.match ------------------------------------------------------------- """
# 関数:
# 　　　re.match(pattern, string, flags=0)
# メソッド:
# 　　　Pattern.match(string[, pos[, endpos]])
#
# 説明: string の先頭で、正規表現とマッチすれば、対応する Match を返します。

# """
pattern = re.compile(r"dog")

# matchを使って正規表現が文字列の先頭にマッチするかを検索します。
match = pattern.match("I have a dog.")

if match:
    print("マッチが見つかりました。")
else:
    print("マッチが見つかりませんでした。")

# 出力：
#    マッチが見つかりませんでした。

# matchを使って正規表現が文字列の先頭にマッチするかを検索します。
match = pattern.match("dog dot bog dog")

if match:
    print("マッチが見つかりました:", match.group())
    print("マッチの開始位置:", match.start())
    print("マッチの終了位置:", match.end())
    print("マッチの位置:", match.span())
else:
    print("マッチが見つかりませんでした。")

# 出力：
#    マッチが見つかりました: dog
#    マッチの開始位置: 0
#    マッチの終了位置: 3
#    マッチの位置: (0, 3)
# """


# 1-4. fullmatch
""" re.fullmatch --------------------------------------------------------- """
# 関数:
# 　　　re.fullmatch(pattern, string, flags=0)
# メソッド:
# 　　　Pattern.fullmatch(string[, pos[, endpos]])
#
# 説明: string 全体が正規表現にマッチするなら、対応する Match を返します。

# """
# "\d{3}"は、数字の3回繰り返し
pattern = re.compile(r"\d{3}-\d{2}-\d{4}")

# fullmatchを使って正規表現が文字列全体に完全にマッチするかを検索します。
fullmatch = pattern.fullmatch("123-45-6789")
if fullmatch:
    print("マッチが見つかりました:", fullmatch.group())
    print("マッチの開始位置:", fullmatch.start())
    print("マッチの終了位置:", fullmatch.end())
    print("マッチの位置:", fullmatch.span())
else:
    print("マッチが見つかりませんでした")

# 出力：
#    マッチが見つかりました: 123-45-6789
#    マッチの開始位置: 0
#    マッチの終了位置: 11
#    マッチの位置: (0, 11)
# """


# 1-5. split
""" re.split ------------------------------------------------------------- """
# 関数:
# 　　　re.split(pattern, string, maxsplit=0, flags=0)
# メソッド:
# 　　　Pattern.split(string, maxsplit=0)
#
# 説明: string を、正規表現にマッチする箇所で分割して、リストを返します。
# 　　　正規表現に丸括弧が使われていれば、正規表現にマッチする箇所もリストの一部として
# 　　　返します。

# """
# "\s+"は、空白文字の1回以上の回繰り返し
pattern = re.compile(r"\s+")

# splitを使って正規表現にマッチする箇所で文字列を分割します。
split = pattern.split("apple banana  orange   grape")
print("分割された部分文字列:", split)

# 出力：
#    分割された部分文字列: ['apple', 'banana', 'orange', 'grape']

# "\s+"は、空白文字の1回以上の回繰り返し
pattern = re.compile(r"(\s+)")

# splitを使って正規表現にマッチする箇所で文字列を分割します。
split = pattern.split("apple banana  orange   grape")
print("分割された部分文字列:", split)

# 出力：
#  分割された部分文字列: ['apple', ' ', 'banana', '  ', 'orange', '  ', 'grape']
# """


# 1-6. findall
""" re.findall ----------------------------------------------------------- """
# 関数:
# 　　　re.findall(pattern, string, flags=0)
# メソッド:
# 　　　Pattern.findall(string[, pos[, endpos]])
#
# 説明: string で、正規表現にマッチする文字列またはタプルのリストを返します。
# 　　　string の先頭から見つかった順序でリストにします。

# """
# "\d+"は、数字の 1 回以上の繰り返し
pattern = re.compile(r"\d+")

# findallを使って正規表現にマッチする部分文字列を検索します。
findall = pattern.findall("I have 2 apples and 321 bananas.")

# マッチした部分文字列のリストを表示します。
print("マッチした部分文字列:", findall)

# 出力：
#    マッチした部分文字列: ['2', '321']
# """


# 1-7. finditer
""" re.finditer ---------------------------------------------------------- """
# 関数:
# 　　　re.finditer(pattern, string, flags=0)
# メソッド:
# 　　　Pattern.finditer(string[, pos[, endpos]])
#
# 説明: string で、正規表現にマッチする Match オブジェクトを yield する イテレータ
# 　　　を返します。
# 　　　string の先頭から見つかった順序で Match オブジェクトにします。

# """
# "\d+"は、数字の 1 回以上の繰り返し
pattern = re.compile(r"\d+")

# finditerを使って正規表現にマッチする部分文字列を検索します。
finditers = pattern.finditer("I have 2 apples and 321 bananas.")

for iter in finditers:
    if iter:
        print("マッチが見つかりました:", iter.group())
        print("マッチの開始位置:", iter.start())
        print("マッチの終了位置:", iter.end())
        print("マッチの位置:", iter.span())
    else:
        print("マッチが見つかりませんでした")

# 出力：
#    マッチが見つかりました: 2
#    マッチの開始位置: 7
#    マッチの終了位置: 8
#    マッチの位置: (7, 8)
#    マッチが見つかりました: 321
#    マッチの開始位置: 20
#    マッチの終了位置: 23
#    マッチの位置: (20, 23)
# """


# 1-8. sub
""" re.sub --------------------------------------------------------------- """
# 関数:
# 　　　re.sub(pattern, repl, string, count=0, flags=0)
# メソッド:
# 　　　Pattern.sub(repl, string, count=0)
#
# 説明: string で、正規表現にマッチする文字列から repl に置換した文字列を返します。

# """
# "\d+"は、直前の数字の 1 回以上の繰り返し
pattern = re.compile(r"\d+")

# subを使って正規表現にマッチする部分を置換します。
sub_str = pattern.sub("X", "I have 2 apples and 321 bananas.")

print("置換後の文字列:", sub_str)

# 出力：
#    置換後の文字列: I have X apples and X bananas.
# """


# 1-9. subn
""" re.subn -------------------------------------------------------------- """
# 関数:
# 　　　re.subn(pattern, repl, string, count=0, flags=0)
# メソッド:
# 　　　Pattern.subn(repl, string, count=0)
#
# 説明: string で、正規表現にマッチする文字列から repl に置換した文字列と、
# 　　　マッチした回数のタプルを返します。

# """
# "\d+"は、直前の数字の 1 回以上の繰り返し
pattern = re.compile(r"\d+")

# subnを使って正規表現にマッチする部分を置換します。
subn = pattern.subn("X", "I have 2 apples and 321 bananas.")

print("置換後の文字列と置換回数:", subn)
print("置換後の文字列:", subn[0])
print("置換回数:", subn[1])

# 出力：
#    置換後の文字列と置換回数: ('I have X apples and X bananas.', 2)
#    置換後の文字列: I have X apples and X bananas.
#    置換回数: 2
# """


# 1-10. escape
""" re.escape ------------------------------------------------------------ """
# 関数:
# 　　　re.escape(pattern)
#
# 説明: pattern 中の特殊文字をエスケープします。

# """
# 正規表現メタ文字を含む文字列を定義します。
text = "Hello. How are you? [I am fine!]"

# 正規表現パターンとして使用する文字列をエスケープします。
escaped_text = re.escape(text)

# エスケープ後の文字列を表示します。
print("エスケープ後の文字列:", escaped_text)

# 出力：
#    エスケープ後の文字列: Hello\.\ How\ are\ you\?\ \[I\ am\ fine!\]
# """


# 1-11. purge
""" re.purge ------------------------------------------------------------- """
# 関数:
# 　　　re.purge()
#
# 説明: 正規表現キャッシュをクリアします。

# """
# 使用されなくなった正規表現パターンのメモリが解放され、パフォーマンスが向上します。
re.purge()
# """


# 2. 例外
# 2-1. error
""" re.error ------------------------------------------------------------- """
# 関数:
# 　　　re.error(msg, pattern=None, pos=None)
#
# 説明: 文字列が有効な正規表現ではないとき、またはコンパイルやマッチングでなんらかの
# 　　　エラーが発生した場合に例外が送出されます。

# """
try:
    # 正規表現パターンが不正なため、エラーが発生します。
    re.compile(r"[")  # '['は正規表現パターンとして不正です
except re.error as e:
    # re.errorが発生した場合、エラーメッセージを表示します。
    # e = unterminated character set at position 0
    print("正規表現エラーが発生しました:", e)
finally:
    print("終了しました。")

# 出力：
#    正規表現エラーが発生しました: unterminated character set at position 0
#    終了しました。
# """


# 3. フラグとオブジェクトメソッド
# 3-1. flags
""" flags ---------------------------------------------------------------- """
# 関数:
# 　　　Pattern.flags
#
# 説明: 正規表現のマッチングフラグです。
#
# フラグの一覧と値。
# re.NOFLAG:     0x0: フラグが適用されていないことを示す。
# re.IGNORECASE: 0x2: 大文字と小文字を区別しないマッチができます。
# re.LOCALE:     0x4: 現在のロケールに依存させます。
# re.MULTILINE:  0x8: 複数行モードになります。複数行モードでは、
# 　　　　　　　　　　　'^'は各行の先頭に、'$は各行の末尾にマッチできます。
# re.DOTALL:    0x10: '.' が改行文字 '\n' にもマッチできる。
# re.UNICODE:   0x20: Python 3 では、デフォルトで Unicode文字にマッチ
# 　　　　　　　　　　　するのでフラグ設定は不要です。
# re.VERBOSE:   0x40: 空白文字、エスケープされていない'#'、'#'から行末まで
# 　　　　　　　　　　　の文字列(コメント)が無視されます。
# re.DEBUG:     0x80: 正規表現のデバッグ情報が表示できます。
# re.ASCII:    0x100: ASCII文字だけにマッチできます。


# re.IGNORECASE
# 説明: 大文字と小文字を区別しないマッチができます。
# """
regex = re.compile(r"a")
sub_str = regex.sub("b", "A a")
print("置換後の文字列:", sub_str)
# 出力：
#       置換後の文字列: A b

regex = re.compile(r"a", re.IGNORECASE)
sub_str = regex.sub("b", "A a")
print("置換後の文字列:", sub_str)
# 出力：
#       置換後の文字列: b b
# """


# re.LOCALE
# 説明: 現在のロケールに依存させます。
# """
# 省略
# """


# re.MULTILINE
# 説明: 複数行モードになります。複数行モードでは、
# 　　　'^'は各行の先頭に、'$は各行の末尾にマッチできます。
# """
regex = re.compile(r"^\w+")
matches = regex.findall("apple\nbanana\ncherry")
print("マッチした部分文字列:", matches)
# 出力：
#       マッチした部分文字列: ['apple']

regex = re.compile(r"^\w+", re.MULTILINE)
matches = regex.findall("apple\nbanana\ncherry")
print("マッチした部分文字列:", matches)
# 出力：
#       マッチした部分文字列: ['apple', 'banana', 'cherry']
# """


# re.DOTALL
# 説明: '.' が改行文字 '\n' にもマッチできます。
# """
regex = re.compile(r"a.*c")
sub_str = regex.sub("d", "ab\nc")
print("置換後の文字列:", sub_str)
# 出力：
#       置換後の文字列: ab
#       c

regex = re.compile(r"a.*c", re.DOTALL)
sub_str = regex.sub("d", "ab\nc")
print("置換後の文字列:", sub_str)
# 出力：
#       置換後の文字列: d
# """


# re.VERBOSE
# 説明: 空白文字、エスケープされていない'#'、'#'から行末まで
# 　　　の文字列(コメント)が無視されます。
# '''
# regex = re.compile(r"""\d+.+\d*""")
regex = re.compile(r"""\d + # 1文字以上の数字
                       .  + # 1文字以上の文字列
                       \d * # 0文字以上の数字
                       """)
sub_str = regex.sub("d", "12abc678")
print("置換後の文字列:", sub_str)
# 出力：
#       置換後の文字列: 12abc678

# regex = re.compile(r"""\d+.+\d*""", re.VERBOSE)
regex = re.compile(r"""\d + # 1文字以上の数字
                       .  + # 1文字以上の文字列
                       \d * # 0文字以上の数字
                       """, re.VERBOSE)
sub_str = regex.sub("d", "12abc678")
print("置換後の文字列:", sub_str)
# 出力：
#       置換後の文字列: d
# '''


# re.DEBUG
# 説明: 正規表現のデバッグ情報が表示できます。
# """
regex = re.compile(r"a")
match = regex.match("a")
if match:
    print("マッチが見つかりました。")
# 出力：
#       マッチが見つかりました。

regex = re.compile(r"a", re.DEBUG)
match = regex.match("a")
if match:
    print("マッチが見つかりました。")
# 出力：
#       LITERAL 97
#        0. INFO 8 0b11 1 1 (to 9)
#             prefix_skip 1
#             prefix [0x61] ('a')
#             overlap [0]
#        9: LITERAL 0x61 ('a')
#       11. SUCCESS
#       マッチが見つかりました。
# """


# re.ASCII
# 説明: ASCII文字だけにマッチできます。
# """
regex = re.compile(r"\w+")
matches = regex.findall("Hello, world! こんにちは、世界！")
print("マッチした部分文字列:", matches)
# 出力：
#       マッチした部分文字列: ['Hello', 'world', 'こんにちは', '世界']

regex = re.compile(r"\w+", re.ASCII)
matches = regex.findall("Hello, world! こんにちは、世界！")
print("マッチした部分文字列:", matches)
# 出力：
#       マッチした部分文字列: ['Hello', 'world']
# """


# 3-2. groups
""" groups --------------------------------------------------------------- """
# 説明: パターン中のキャプチャグループの数です。

# """
pattern = r"(\d{4})-(\d{2})-(\d{2})"
regex = re.compile(pattern)
print("グループの数:", regex.groups)

# 出力：
#       グループの数: 3
# """


# 3-3. groupindex
""" groupindex ----------------------------------------------------------- """
# 説明: シンボリックグループ名とグループ番号の辞書です。

# """
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
regex = re.compile(pattern)
print("グループの数:", regex.groups)
print("グループ名とインデックス番号:", regex.groupindex)

# 出力：
#       グループの数: 3
#       グループ名とインデックス番号: {'year': 1, 'month': 2, 'day': 3}
# """


# 3-4. pattern
""" pattern -------------------------------------------------------------- """
# 説明: パターンオブジェクトがコンパイルされた元のパターン文字列です。

# """
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
regex = re.compile(pattern)
print("グループの数:", regex.groups)
print("グループ名とインデックス番号:", regex.groupindex)
print("パターン:", regex.pattern)

# 出力：
#       グループの数: 3
#       グループ名とインデックス番号: {'year': 1, 'month': 2, 'day': 3}
#       パターン: (?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})
# """


# 4. マッチオブジェクト
# 4-1. Match.expand(template)
""" Match.expand --------------------------------------------------------- """
# 説明: テンプレート文字列 template でバックスラッシュ置換を実行して取得
#      された文字列を返します。

# """
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, "Today is 2024-04-30.")
expanded_text = match.expand(r"\g<day>.\g<2>.\1")
print("置換されたパターン:", expanded_text)

# 出力：
#       置換されたパターン: 30.04.2024
# """


# 4-2. Match.group([group1, ...])
""" Match.group ---------------------------------------------------------- """
# 説明: マッチしたグループの文字列を返します。
#      複数の引数があれば、タプルで返します。

# """
pattern = r"(\w+) (\w+)"
match = re.match(pattern, "Isaac Newton, physicist")
print("グループ全体:", match.group(0))
print("グループ1:", match.group(1))
print("グループ2:", match.group(2))
print("グループ(1, 2):", match.group(1, 2))

# 出力：
#       グループ全体: Isaac Newton
#       グループ1: Isaac
#       グループ2: Newton
#       グループ(1, 2): ('Isaac', 'Newton')
# """


# 4-3. Match.__getitem__(g)
""" Match.__getitem__ ---------------------------------------------------- """
# 説明: groupと同じで、マッチしたグループの文字列を返します。

# """
pattern = r"(\w+) (\w+)"
match = re.match(pattern, "Isaac Newton, physicist")
print("グループ全体:", match.__getitem__(0))
print("グループ1:", match.__getitem__(1))
print("グループ2:", match.__getitem__(2))

# 出力：
#       グループ全体: Isaac Newton
#       グループ1: Isaac
#       グループ2: Newton
# """


# 4-4. Match.groups(default=None)
""" Match.groups --------------------------------------------------------- """
# 説明: 全てのサブグループを含むタプルを返します。

# """
match = re.match(r"(\d+)\.(\d+)", "24.1632")
print("グループ全体:", match.groups())

# 出力：
#       グループ全体: ('24', '1632')
# """


# 4-5. Match.groupdict(default=None)
""" Match.groupdict ------------------------------------------------------ """
# 説明: 全ての 名前付き サブグループを含む、サブグループ名がキーの辞書を返します。

# """
pattern = r"(?P<first_name>\w+) (?P<last_name>\w+)"
regex = re.compile(pattern)
match = re.match(regex, "Malcolm Reynolds")
print("グループの辞書:", match.groupdict())

# 出力：
#       グループの辞書: {'first_name': 'Malcolm', 'last_name': 'Reynolds'}
# """


# 4-6. Match.start([group])
#      Match.end([group])
#      Match.span([group])
""" Match.start ---------------------------------------------------------- """
""" Match.end ------------------------------------------------------------ """
""" Match.span ----------------------------------------------------------- """
# Match.start([group])
#  　説明: マッチした部分文字列の先頭のインデックスを返します。
# Match.end([group])
#  　説明: マッチした部分文字列の末尾のインデックスを返します。
# Match.span([group])
#  　説明: マッチした部分文字列の先頭と末尾のインデックスをタプルで返します。

# """
pattern = re.compile(r"dog")
search = pattern.search("I have a dog named Rover.")

if search:
    print("マッチの開始位置:", search.start())
    print("マッチの終了位置:", search.end())
    print("マッチの位置:", search.span())

# 出力：
#    マッチの開始位置: 9
#    マッチの終了位置: 12
#    マッチの位置: (9, 12)
# """


# 4-7. Match.pos
#      Match.endpos
#      Match.lastindex
#      Match.lastgroup
""" Match.pos ------------------------------------------------------------ """
""" Match.endpos --------------------------------------------------------- """
""" Match.lastindex ------------------------------------------------------ """
""" Match.lastgroup ------------------------------------------------------ """
# Match.pos
#  　説明: 探索が始まる位置の文字列のインデックスです。
# Match.endpos
#  　説明: 探索が終わる位置の文字列のインデックスです。
# Match.lastindex
#  　説明: 最後にマッチしたキャプチャグループのインデックスです。
# Match.lastgroup
#  　説明: 最後にマッチしたキャプチャグループ名です。

# """
pattern = r"(?P<first_name>\w+) (?P<last_name>\w+)"
regex = re.compile(pattern)
match = re.match(regex, "Malcolm Reynolds")

if match:
    print("検索開始位置:", match.pos)
    print("検索終了位置:", match.endpos)
    print("マッチの位置:", match.lastindex)
    print("マッチの位置:", match.lastgroup)

# 出力：
#    検索開始位置: 0
#    検索終了位置: 16
#    最後のインデックス番号: 2
#    最後のグループ名: last_name
# """

# 4-8. Match.re
#      Match.string
""" Match.re ------------------------------------------------------------- """
""" Match.string --------------------------------------------------------- """
# Match.re
#  　説明: 正規表現オブジェクト
# Match.string
#  　説明: マッチオブジェクトに入力した文字列です。

# """
pattern = re.compile(r"dog")
search = pattern.search("I have a dog named Rover.")

if search:
    print("正規表現オブジェクト:", search.re)
    print("入力文字列:", search.string)

# 出力：
#    正規表現オブジェクト: re.compile('dog')
#    入力文字列: I have a dog named Rover.
# """


# 5. 正規表現
# 5-1. '.' (ドット)
""" '.' (dot) ------------------------------------------------------------ """
# 改行以外の任意の文字にマッチします。
# re.DOTALLフラグ使用時は、改行も含みます。

# """
pattern = re.compile(r"...")
search = pattern.search("dog")
if search:
    print("マッチが見つかりました:", search.group())
else:
    print("マッチが見つかりませんでした")

pattern = re.compile(r"...")
search = pattern.search("d\ng")
if search:
    print("マッチが見つかりました:", search.group())
else:
    print("マッチが見つかりませんでした")

pattern = re.compile(r"...", re.DOTALL)
search = pattern.search("d\ng")
if search:
    print("マッチが見つかりました:", search.group())
else:
    print("マッチが見つかりませんでした")

# 出力：
#       マッチが見つかりました: dog
#       マッチが見つかりませんでした
#       マッチが見つかりました: d
#       g
# """

# 5-2. '^' (キャレット)
""" '^' (caret) ---------------------------------------------------------- """
# 文字列の先頭にマッチします。
# re.MULTILINEフラグ使用時は、改行も含みます。

# """
pattern = re.compile(r"^A")
matches = pattern.findall("A\nA")
for match in matches:
    print("マッチA:", match)

pattern = re.compile(r"^b", re.MULTILINE)
matches = pattern.findall("b\nb")
for match in matches:
    print("マッチb:", match)

# 出力：
#       マッチA: A
#       マッチb: b
#       マッチb: b
# """

# 5-3. '$' (ドル記号)
""" '$' (dollar sign) ---------------------------------------------------- """
# 文字列の先頭にマッチします。
# re.MULTILINEフラグ使用時は、改行も含みます。

# """
pattern = re.compile(r"A$")
matches = pattern.findall("A\nA")
for match in matches:
    print("マッチA:", match)

pattern = re.compile(r"b$", re.MULTILINE)
matches = pattern.findall("b\nb")
for match in matches:
    print("マッチb:", match)

# 出力：
#       マッチA: A
#       マッチb: b
#       マッチb: b
# """


# 5-4. '*' (アスタリスク)
""" '*' (asterisk) ------------------------------------------------------- """
# 直前の文字の 0 回以上の繰り返しにマッチします。

# """
pattern = re.compile(r"b*")
matches = pattern.findall("aaabbbbcccc")
print("マッチ:", matches)

# 出力：
#       マッチ: ['', '', '', 'bbbb', '', '', '', '', '']
# """


# 5-5. '+' (プラス)
""" '+' (plus) ----------------------------------------------------------- """
# 直前の文字の 1 回以上の繰り返しにマッチします。

# """
pattern = re.compile(r"b+")
matches = pattern.findall("aaabbbbcccc")
print("マッチ:", matches)

# 出力：
#       マッチ: ['bbbb']
# """


# 5-6. '?' (クエスチョンマーク)
""" '?' (question mark) -------------------------------------------------- """
# 直前の文字の 0回 または 1 回の繰り返しにマッチします。

# """
pattern = re.compile(r"c?")
matches = pattern.findall("aaabbbbcccc")
print("マッチ:", matches)

# 出力：
#       マッチ: ['', '', '', '', '', '', '', 'c', 'c', 'c', 'c', '']
# """


# 5-7. '*?', '+?', '??' (非貪欲 (non-greedy) または 最小 (minimal))
""" '*?', '+?', '??' (non-greedy or minimal) ----------------------------- """
# できるだけ 少ない 文字にマッチします。

# """
# '*?' による貪欲マッチング
matches_non_greedy = re.findall(r"a*?", "aaaaab")
print("非貪欲マッチング:", matches_non_greedy)

# 出力：
#   非貪欲マッチング: ['', 'a', '', 'a', '', 'a', '', 'a', '', 'a', '', '', '']

# '+?' による非貪欲マッチング
matches_non_greedy = re.findall(r"b+?", "abbbb")
print("非貪欲マッチング:", matches_non_greedy)

# 出力：
#   非貪欲マッチング: ['b', 'b', 'b', 'b']

# '??' による非貪欲マッチング
matches_non_greedy = re.findall(r"ab??", "ababab")
print("非貪欲マッチング:", matches_non_greedy)

# 出力：
#   非貪欲マッチング: ['a', 'a', 'a']
# """


# 5-8. '*+', '++', '?+'
""" '*+', '++', '??' ----------------------------------------------------- """
# できるだけ 多くの文字にマッチします。

# """
# '*+' による貪欲マッチング
matches_non_greedy = re.findall(r"a*+", "aaaaaab")
print("'*+'マッチング:", matches_non_greedy)

# 出力：
#     '*+'マッチング: ['aaaaaa', '', '']

# '++' のマッチング
matches_non_greedy = re.findall(r"b++", "abbbb")
print("'++'マッチング:", matches_non_greedy)

# 出力：
#     '++'マッチング: ['bbbb']

# '?+' のマッチング
matches_non_greedy = re.findall(r"ab?+", "ababab")
print("'?+'マッチング:", matches_non_greedy)

# 出力：
#     '?+'マッチング: ['ab', 'ab', 'ab']
# """


# 5-9. '{m}'
""" '{m}' ---------------------------------------------------------------- """
# 直前の正規表現を m 回繰り返したものにマッチします。

# """
matches = re.findall(r"a{3}", "aaa aaaa aaaaa")
print("'{m}'マッチした部分:", matches)

# 出力：
#     '{m}'マッチした部分: ['aaa', 'aaa', 'aaa']
# """


# 5-10. '{m,n}'
""" '{m,n}' -------------------------------------------------------------- """
# 直前の正規表現を m 回から n 回 できるだけ多く繰り返したものにマッチします。

# """
matches = re.findall(r"a{3,5}", "aaa aaaa aaaaa")
print("'{m,n}'マッチした部分:", matches)

# 出力：
#     '{m,n}'マッチした部分: ['aaa', 'aaaa', 'aaaaa']
# """


# 5-11. '{m,n}?'
""" '{m,n}?' ------------------------------------------------------------- """
# 前にある正規表現を、m 回から n 回まで繰り返したものにマッチし、
# できるだけ 少なく 繰り返したものにマッチします。

# """
matches = re.findall(r"a{3,5}?", "aaa aaaa aaaaa")
print("'{m,n}?'マッチした部分:", matches)

# 出力：
#     '{m,n}?'マッチした部分: ['aaa', 'aaa', 'aaa']
# """


# 5-12. '{m,n}+'
""" '{m,n}+' ------------------------------------------------------------- """
# 前にある正規表現を、m 回から n 回まで繰り返したものにマッチし、
# できるだけ 多く 繰り返したものにマッチします。

# """
matches = re.findall(r"a{3,5}+", "aaa aaaa aaaaa")
print("'{m,n}+'マッチした部分:", matches)

# 出力：
#     '{m,n}+'マッチした部分: ['aaa', 'aaaa', 'aaaaa']
# """


# 5-13. '\'
""" '\' ------------------------------------------------------------------ """
# 特殊文字をエスケープ ( '*' や '?' などの文字にマッチできるようにする) します。

# """
matches = re.findall(r"\*+", "aaa **** aaaaa")
print("'\*+'マッチした部分:", matches)

# 出力：
#     '\*+'マッチした部分: ['****']
# """


# 5-14. '[]'
""" '[]' ----------------------------------------------------------------- """
# 文字の集合を指定するのに使います。

# ""
# (1) 文字を個別に指定できます。
#      例： [amk] は 'a' 、 'm' または 'k' にマッチします。
matches = re.findall(r"[amk]", "abcdefghijklmnopqrstuvwxyz")
print("'[amk]'マッチ:", matches)

# 出力：
#     '[amk]'マッチ: ['a', 'k', 'm']


# (2) 連続した文字の範囲を、 '-' を2 つの文字で挟んで指定できます。
#      例： [a-z] はあらゆる小文字の ASCII 文字にマッチします。
#      例： [0-5][0-9] は 00 から 59 まで全ての 2 桁の数字にマッチします。
#      例： [0-9A-Fa-f] は任意の 16 進数字にマッチします。
matches = re.findall(r"[a-z]", "abcdwxyz")
print("'[a-z]'マッチ:", matches)

matches = re.findall(r"[0-5][0-9]", "00 01 58 59 60")
print("'[0-5][0-9]'マッチ:", matches)

matches = re.findall(r"[0-9A-Fa-f]", "0 1 9 a f g A F G")
print("'[0-9A-Fa-f]'マッチ:", matches)

# 出力：
#     '[a-z]'マッチ: ['a', 'b', 'c', 'd', 'w', 'x', 'y', 'z']
#     '[0-5][0-9]'マッチ: ['00', '01', '58', '59']
#     '[0-9A-Fa-f]'マッチ: ['0', '1', '9', 'a', 'f', 'A', 'F']


# (3) '-' はエスケープされるか、先頭や末尾にされると リテラル '-' にマッチします。
#      例： [a\-z]
#      例： [-a] や [a-]
matches = re.findall(r"[a\-z]", "abc-xyz")
print("'[a\-z]'マッチ:", matches)

matches = re.findall(r"[-a]", "abc-xyz")
print("'[-a]'マッチ:", matches)

matches = re.findall(r"[a-]", "abc-xyz")
print("'[a-]'マッチ:", matches)

# 出力：
#     '[a\-z]'マッチ: ['a', '-', 'z']
#     '[-a]'マッチ: ['a', '-']
#     '[a-]'マッチ: ['a', '-']


# (4) 集合の中では、特殊文字はその特殊な意味を失います。
#      例： [(+*)] はリテラル '('、'+'、'*'、または ')' のどれでもマッチします。
matches = re.findall(r"[(+*)]", "[(+*)]")
print("'[(+*)]'マッチ:", matches)

# 出力：
#     '[(+*)]'マッチ: ['(', '+', '*', ')']


# (5) \w や \S などセット内で受け入れられます。
#     一致する文字は使用されるフラグによって異なります。
matches = re.findall(r"[\w\s]", "abcxyz-[(+*)]")
print("'[\w\S]'マッチ:", matches)

# 出力：
#     '[\w\S]'マッチ: ['a', 'b', 'c', 'x', 'y', 'z']


# (6) 補集合 をとって範囲内にない文字にマッチできます。
#     集合の最初の文字が '^' なら、集合に 含まれないマッチします。
#     '^' は集合の最初の文字でなければ特別の意味を持ちません。
#      例： [^5] は '5' を除くあらゆる文字にマッチします。
#      例： [^^] は '^' を除くあらゆる文字にマッチします。
matches = re.findall(r"[^5]", "1234567890")
print("'[^5]'マッチ:", matches)

matches = re.findall(r"[^^]", "!#$%&^*")
print("'[^^]'マッチ:", matches)

# 出力：
#     '[^5]'マッチ: ['1', '2', '3', '4', '6', '7', '8', '9', '0']
#     '[^^]'マッチ: ['!', '#', '$', '%', '&', '*']


# (7) リテラル ']' にマッチさせるには、前にバックスラッシュをつけるか、
#     集合の先頭に置きます。
#      例：  [()[\]{}] と []()[{}] はどちらも閉じ角括弧、開き角括弧、波括弧、
#            丸括弧にマッチします。
matches = re.findall(r"[()[\]{}]", "[](){}")
print("'[()[\]{}]'マッチ:", matches)

matches = re.findall(r"[]()[{}]", "[](){}")
print("'[]()[{}]'マッチ:", matches)

# 出力：
#     '[()[\]{}]'マッチ: ['[', ']', '(', ')', '{', '}']
#     '[]()[{}]'マッチ: ['[', ']', '(', ')', '{', '}']
# """


# 5-15. '|'
""" '|' ------------------------------------------------------------------ """
# A|B は A と B のいずれかにマッチします。
# 正規表現を '|' で分離できます。

# """
matches = re.findall(r"dog|cat", "I have a dog and a cat.")
print("'dog|cat'マッチ:", matches)

# 出力：
#     'dog|cat'マッチ: ['dog', 'cat']
# """


# 5-16. '(...)'
""" '(...)' -------------------------------------------------------------- """
# 丸括弧で囲まれた正規表現にマッチするとともに、グループの開始と終了を表します。

# """
pattern = r"(\w+) is \1"
text = "apple is apple, banana is banana, orange is orange."
matches = re.findall(pattern, text)
print("'(\w+) is \1'マッチ:", matches)

# 出力：
#     '(\w+) is 'マッチ: ['apple', 'banana', 'orange']
# """


# 5-17. '(?aiLmsux)'
""" '(?aiLmsux)' --------------------------------------------------------- """
# '?' に続く最初の文字がこの構造の意味と特有の構文を決定します。
# 拡張は一般に新しいグループを作成しません。ただし (?P<name>...) は例外です。

# '''
# (1) '(?a)' = re.ASCII、re.A
#     説明: ASCII文字だけにマッチできます。
regex = re.compile(r"(?a)\w+")
matches = regex.findall("Hello, world! こんにちは、世界！")
print("'(?a)'マッチ:", matches)

# 出力：
#     '(?a)'マッチ: ['Hello', 'world']


# (2) '(?i)' = re.IGNORECASE、re.I
#     説明: 大文字と小文字を区別しないマッチができます。
regex = re.compile(r"(?i)a")
matches = regex.findall("A a")
print("'(?i)'マッチ:", matches)

# 出力：
#     '(?i)'マッチ: ['A', 'a']


# (3) '(?L)' = re.LOCALE、re.L
#     説明: 現在のロケールに依存させます。
# 省略


# (4) '(?m)' = re.MULTILINE、re.M
#     説明: 複数行モードになります。複数行モードでは、
#          '^' や '$' を使用して、各行でマッチできる。
regex = re.compile(r"(?m)^\w+")
matches = regex.findall("apple\nbanana\ncherry")
print("'(?m)'マッチ:", matches)

# 出力：
#     '(?m)'マッチ: ['apple', 'banana', 'cherry']


# (5) '(?s)' = re.DOTALL、re.S
#     説明: 特殊文字 '.' を、改行を含む任意の文字とマッチ
regex = re.compile(r"(?s)a.*c")
matches = regex.findall("ab\nc")
print("'(?s)'マッチ:", matches)

# 出力：
#     '(?s)'マッチ: ['ab\nc']


# (6) '(?u)' = re.UNICODE、re.U
#     説明: Unicode文字にマッチします。
# 省略


# (7) '(?x)' = re.VERBOSE、re.X
#     説明: 空白文字、エスケープされていない'#'、'#'から行末まで
#           の文字列(コメント)が無視されます。
regex = re.compile(r"""(?x)
                       \d + # 1文字以上の数字
                       .  + # 1文字以上の文字列
                       \d * # 0文字以上の数字
                       """)
matches = regex.findall("12abc678")
print("'(?x)'マッチ:", matches)

# 出力：
#     '(?x)'マッチ: ['12abc678']
# '''


# 5-18. '(?>...)'
""" '(?>...)' ------------------------------------------------------------ """
# ... の照合を試行し、成功すると、その後に続くパターンの残りの部分と照合し続けます。
#  x*+、x++、および x?+ は、それぞれ (?>x*)、(?>x+)、および (?>x?) と同等です。

# """
matches_non_greedy = re.findall(r"(?>a*)", "aaaaaab")
print("'(?>...)'マッチ:", matches_non_greedy)

# 出力：
#     '(?>...)'マッチ: ['aaaaaa', '', '']
# """


# 5-19. '(?P<name>...)'
""" '(?P<name>...)' ------------------------------------------------------ """
# グループに一致する部分文字列には、シンボリック グループ名 name を介してアクセス
# できます。

# """
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"  # 年月日のパターン
text = "Today is 2024-04-30."
matches = re.search(pattern, text)
if matches:
    print("'(?P<year>)' 年:", matches.group('year'))
    print("'(?P<month>)' 月:", matches.group('month'))
    print("'(?P<day>)' 日:", matches.group('day'))

# 出力：
#     '(?P<year>)' 年: 2024
#     '(?P<month>)' 月: 04
#     '(?P<day>)' 日: 30
# """


# 5-20. '(?P=name)'
""" '(?P=name)' ---------------------------------------------------------- """
# name という名前の既出のグループがマッチした文字列にマッチします。

# """
pattern = r"(?P<word>\w+) is (?P=word)"  # 同じ単語が2回続くパターン
text = "apple is apple, banana is banana, orange is orange."
matches = re.findall(pattern, text)
print("'(?P=name)'マッチ:", matches)

# 出力：
#     '(?P=name)'マッチ: ['apple', 'banana', 'orange']
# """


# 5-21. '(?#...)'
""" '(?#...)' ------------------------------------------------------------ """
# コメントは無視されます。

# """
matches = re.findall(r"(?#コメントです)a", "a a a")
print("'(?#コメントです)a':", matches)

# 出力：
#     '(?#コメントです)a': ['a', 'a', 'a']
# """


# 5-22. '(?=...)'
""" '(?=...)' ------------------------------------------------------------ """
# ... が次に続くものにマッチすればマッチします。
# 先読みアサーション (lookahead assertion) と呼ばれます。

# """
pattern = r"Isaac (?=Asimov)"
text = "Isaac Asimov is a great author."
matches = re.findall(pattern, text)
print("'Isaac (?=Asimov)'マッチ:", matches)

# 出力：
#     'Isaac (?=Asimov)'マッチ: ['Isaac ']
# """


# 5-23. '(?!...)'
""" '(?!...)' ------------------------------------------------------------ """
# ... が次に続くものにマッチしなければマッチします。
# 否定先読みアサーション (negative lookahead assertion) と呼ばれます。

# """
pattern = r"Isaac (?!Asimov)"
text = "Isaac Newton is a great scientist."
matches = re.findall(pattern, text)
print("'Isaac (?!Asimov)'マッチ:", matches)

# 出力：
#     'Isaac (?!Asimov)'マッチ: ['Isaac ']
# """


# 5-24. '(?<=...)'
""" '(?<=...)' ----------------------------------------------------------- """
# 現在位置で終わる ... とマッチします。後読みアサーション と呼ばれます。
# 含まれるパターンは固定長の文字列にのみマッチしなければなりません。
# 肯定後読みアサーションで始まるパターンは、検索される文字列の先頭とは決して
# マッチしないことに注意して下さい。match() 関数ではなく search() 関数を使う方が
# 望ましいでしょう。

# """
matches = re.findall(r"(?<=abc)def", "abcdef")
print("'(?<=abc)def'マッチ:", matches)

# 出力：
#     '(?<=abc)def'マッチ: ['def']
# """


# 5-25. '(?<!...)'
""" '(?<!...)' ----------------------------------------------------------- """
# 現在位置の前に ... とのマッチがなければ、マッチします。
# 否定後読みアサーション(negative lookbehind assertion) と呼ばれます。
# 含まれるパターンは固定長の文字列にのみマッチしなければなりません。

# """
matches = re.findall(r"(?<!abc)def", "abbdef")
print("'(?<!abc)def'マッチ:", matches)

# 出力：
#     '(?<!abc)def'マッチ: ['def']
# """


# 5-26. '(?(id/name)yes-pattern|no-pattern)'
""" '(?(id/name)yes-pattern|no-pattern)' --------------------------------- """
# 与えられた id や name のグループが存在すれば yes-pattern とマッチを試みます。
# 与えられた id や name のグループが存在しなければ no-pattern とのマッチを試みます。
# no-pattern はオプションであり省略できます。

# """
pattern = r"(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)"
text = "<user@host.com> user@host.com"
matches = re.findall(pattern, text)
print("'(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)'マッチ:", matches)

# 出力：
#     '(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)'マッチ: ['def']
# """


# 5-27. '\number'
""" '\number' ------------------------------------------------------------ """
# 同じ番号のグループの中身にマッチします。グループは 1 から始まる番号をつけられます。
# 最初の 99 グループのうちの 1 グループとのマッチにのみ使えます。

# """
matches = re.findall(r"(.+) \1", "the the 55 55")
print("'(.+) \1'マッチ:", matches)

# 出力：
#     '(.+) 'マッチ: ['the', '55']
# """


# 5-28. '\A'
""" '\A' ----------------------------------------------------------------- """
# 文字列の先頭でのみマッチします。

# """
matches = re.findall(r"\Aa", "b a a")
print("'\Aa'マッチ:", matches)

# 出力：
#     '\Aa'マッチ: []

matches = re.findall(r"\Aa", "a b b")
print("'\Aa'マッチ:", matches)

# 出力：
#     '\Aa'マッチ: ['a']
# """


# 5-29. '\b'
""" '\b' ----------------------------------------------------------------- """
# 空文字列にマッチしますが、単語の先頭か末尾でのみです。
# 形式的には、 \b は \w と \W 文字 (またはその逆) との、あるいは
# \w と文字列の先頭・末尾との境界として定義されます。

# """
matches = re.findall(r"\bat\b", "attempt")
print("'\\bat\\b'マッチ:", matches)

# 出力：
#     '\bat\b'マッチ: []

matches = re.findall(r"\bat\b", "as at ay")
print("'\\bat\\b'マッチ:", matches)

# 出力：
#     '\bat\b'マッチ: ['at']
# """


# 5-30. '\B'
""" '\B' ----------------------------------------------------------------- """
# 空文字列にマッチしますが、それが単語の先頭か末尾 でない ときのみです。
# 形式的には、 \b は \w と \W 文字 (またはその逆) との、あるいは
# \w と文字列の先頭・末尾との境界として定義されます。

# """
matches = re.findall(r"\Bat\B", "battery")
print("'\Bat\B'マッチ:", matches)

# 出力：
#     '\Bat\B'マッチ: ['at']

matches = re.findall(r"\Bat\B", "at")
print("'\Bat\B'マッチ:", matches)

# 出力：
#     '\Bat\B'マッチ: []
# """


# 5-31. '\d'
""" '\d' ----------------------------------------------------------------- """
# Unicode (str) パターンでは:
#      任意の Unicode 10 進数字 にマッチします。[0-9] と他多数の数字を含みます。
#      ASCII フラグを使用すると [0-9] にマッチします。
# 8 ビット (bytes) パターンでは:
#      任意のASCII文字の 10 進数字にマッチします。これは [0-9] と等価です。

# """
matches = re.findall(r"\d\d\d", "abc ef 123 456")
print("'\d\d\d'マッチ:", matches)

# 出力：
#     '\d\d\d'マッチ: ['123', '456']
# """


# 5-32. '\D'
""" '\D' ----------------------------------------------------------------- """
# 10 進数ではない任意の文字と一致します。 \d の逆です。
# ASCII フラグを使用すると [^0-9] にマッチします。

# """
matches = re.findall(r"\D\D\D", "abc ef 123 456")
print("'\D\D\D'マッチ:", matches)

# 出力：
#     '\D\D\D'マッチ: ['abc', ' ef']
# """


# 5-33. '\s'
""" '\s' ----------------------------------------------------------------- """
# Unicode (str) パターンでは:
#      Unicode 空白文字 (これは [ \t\n\r\f\v] その他多くの文字にマッチします。
#      ASCII フラグを使用すると [ \t\n\r\f\v] にマッチします。
# 8 ビット (bytes) パターンでは:
#      空白文字と見なされる文字にマッチします。[ \t\n\r\f\v] と等価です。

# """
matches = re.findall(r"\s", "ab   cd\tef\n")
print("'\s'マッチ:", matches)

# 出力：
#     '\s'マッチ: [' ', ' ', ' ', '\t', '\n']
# """


# 5-34. '\S'
""" '\S' ----------------------------------------------------------------- """
# 空白文字ではない任意の文字と一致します。 これは \s の逆です。
# ASCII フラグを使用すると [^ \t\n\r\f\v] にマッチします。

# """
matches = re.findall(r"\S", "ab   cd\tef\n")
print("'\S'マッチ:", matches)

# 出力：
#     '\S'マッチ: ['a', 'b', 'c', 'd', 'e', 'f']
# """


# 5-35. '\w'
""" '\w' ----------------------------------------------------------------- """
# Unicode (str) パターンでは:
#      単語文字にマッチします。英数字とアンダースコア (_) を含みます。
#      ASCII フラグを使用すると [a-zA-Z0-9_] にマッチします。
# 8 ビット (bytes) パターンでは:
#      英数字とアンダースコア (_) にマッチします。[a-zA-Z0-9_] と等価です。

# """
matches = re.findall(r"\w", "azAz09_")
print("'\w'マッチ:", matches)

# 出力：
#     '\w'マッチ: [' ', ' ', ' ', '\t', '\n']
# """


# 5-36. '\W'
""" '\W' ----------------------------------------------------------------- """
# 単語文字ではない任意の文字とマッチします。 \w の逆です。
# アンダースコア (_) 以外の文字と一致します。
# ASCII フラグを使用すると [^a-zA-Z0-9_] にマッチします。

# """
matches = re.findall(r"\W", "azAz09_!-^()&%$#")
print("'\W'マッチ:", matches)

# 出力：
#     '\W'マッチ: ['!', '-', '^', '(', ')', '&', '%', '$', '#']
# """


# 5-37. '\Z'
""" '\Z' ----------------------------------------------------------------- """
# 文字列の末尾でのみマッチします。

# """
matches = re.findall(r"\d\Z", "1234")  # 数字の後に末尾が続く場合
print("'\d\Z'マッチ", matches)

# 出力：
#     '\d\Z'マッチ ['4']
# """
