class Point(object):
    def __init__(self, x = 0, y = 0, z = 0):
        self._x = x
        self._y = y
        self._z = z

    def toString(self):
        x = '{:.2f}'.format(self._x)
        y = '{:.2f}'.format(self._y)
        z = '{:.2f}'.format(self._z)
        if z > 0:
            print("P(" + str(x) + ", " + str(y) +")")
        else:
            print("P(" + str(x) + ", " + str(y) + ", " + str(z) + ")")
