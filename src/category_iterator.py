class CategoryIterator:
    def __init__(self, category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._category.get_products_list()):
            product = self._category.get_products_list()[self._index]
            self._index += 1
            return product
        raise StopIteration

    def __repr__(self):
        return f"CategoryIterator({self._category})"
