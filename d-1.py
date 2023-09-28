import math  # mathモジュールをインポートして、円周率や数学的計算を利用できるようにします。


class Circle:  # Circleという名前のクラスを定義します。
    def __init__(self, radius):  # インスタンスが生成される際に初期化を行う特殊メソッドです。
        self.radius = radius  # 引数として受け取ったradiusをインスタンスの属性として保存します。

    def area(self):  # areaというメソッドを定義します。これが円の面積を計算するメソッドです。
        # math.piで円周率πを取得し、半径の二乗に掛けて面積を計算します。その後、roundで小数点以下2位を四捨五入します。
        return round(math.pi * self.radius**2, 2)

    def perimeter(self):  # perimeterというメソッドを定義します。これが円の周囲長（円周）を計算するメソッドです。
        # 2 * math.piで円周率πを2倍し、半径に掛けて周囲長を計算します。その後、roundで小数点以下2位を四捨五入します。
        return round(2 * math.pi * self.radius, 2)


# 以下は上で定義したCircleクラスの使用例です。

# 半径1の円のインスタンスを生成します。
circle1 = Circle(radius=1)
# circle1の面積を計算して出力します。
print(circle1.area())  # 出力: 3.14
# circle1の周囲長を計算して出力します。
print(circle1.perimeter())  # 出力: 6.28

# 半径3の円のインスタンスを生成します。
circle3 = Circle(radius=3)
# circle3の面積を計算して出力します。
print(circle3.area())  # 出力: 28.27
# circle3の周囲長を計算して出力します。
print(circle3.perimeter())  # 出力: 18.85
