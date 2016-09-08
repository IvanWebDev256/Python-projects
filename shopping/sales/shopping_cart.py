class Cart(object):
    def __init__(self):
        self._content = dict()

    def __repr__(self):
        return "{0} {1}".format(Cart, self.__dict__)

    def process(self, order):
        if order.add:
            if order.item not in self._content:
                self._content[order.item] = 0
            self._content[order.item] += 1
        elif order.delete:
            if order.item in self._content:
                self._content[order.item] -= 1
            if self._content[order.item] == 0:
                self._content.pop(order.item)
