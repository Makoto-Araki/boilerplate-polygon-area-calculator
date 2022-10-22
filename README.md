# クラス継承

長方形クラスから継承して正方形クラスを作成

## 1. 実行準備

リモートリポジトリから取得後に Python を対話モードで起動

```
$ git clone https://github.com/Makoto-Araki/boilerplate-polygon-area-calculator.git
$ cd boilerplate-polygon-area-calculator
$ python (対話モードで起動)
```

## 2. 長方形クラス

インスタンスを複数作成後にメソッド実行

```
>>> rect1 = shape_calculator.Rectangle(10, 20)  # 長方形1(幅:10 高さ:20)
>>> rect2 = shape_calculator.Rectangle(10, 10)  # 長方形2(幅:10 高さ:10)
>>> print(rect1.get_amount_inside(rect2))       # 長方形1内に包含可能な長方形2の数
2
```

## 3. 正方形クラス

インスタンスを複数作成後にメソッド実行

```
>>> square1 = shape_calculator.Square(20)      # 正方形1(幅:20 高さ:20)
>>> square2 = shape_calculator.Square(10)      # 正方形2(幅:10 高さ:10)
>>> print(square1.get_amount_inside(square2))  # 正方形1内に包含可能な正方形2の数
4
```