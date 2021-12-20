class SpecialStack:

    _arr = None
    _min = None

    def __init__(self):
        self._arr = []

    def __repr__(self):
        return "<SpecialStack Min:{0}: {1}>".format(self._min, self._arr)

    def push(self, data):
        if not self._min:
            self._min = data
        elif data < self._min:
            self._min = data
        self._arr.append(data)
        return self._arr

    def pop(self):
        i = self._arr[-1]
        del self._arr[-1]
        return i

    def is_empty(self):
        return True if self._min is not None else False

    def get_min(self):
        return self._min

ee = SpecialStack()

ee.push(9)
ee.push(2)
ee.push(5)
ee.push(1)
ee.push(4)
ee.push(6)

print(ee)

ee.pop()
