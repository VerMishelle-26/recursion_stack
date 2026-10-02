# === К1: Рекурсивный факториал ===
def factorial(n):
    """Рекурсивный факториал. Базовый случай: n <= 1."""
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# === К2: Рекурсивная сумма списка ===
def recursive_sum(arr):
    """Рекурсивная сумма элементов списка."""
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])


# === К3: Рекурсивный бинарный поиск ===
def binary_search_recursive(arr, target, left=0, right=None):
    """Рекурсивный бинарный поиск. Возвращает индекс или -1."""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# === К4: Класс Stack ===
class Stack:
    """Стек на основе списка."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Добавить элемент на вершину стека."""
        self._items.append(item)

    def pop(self):
        """Удалить и вернуть верхний элемент."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items.pop()

    def peek(self):
        """Посмотреть верхний элемент без удаления."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items[-1]

    def is_empty(self):
        """Проверить, пуст ли стек."""
        return len(self._items) == 0

    def size(self):
        """Количество элементов."""
        return len(self._items)

    def __str__(self):
        return f"Stack({self._items})"


# === Проверка ===
if __name__ == "__main__":
    print("=== К1: Факториал ===")
    for n in [0, 1, 5, 10]:
        print(f"factorial({n}) = {factorial(n)}")

    print("\n=== К2: Сумма списка ===")
    test_lists = [[], [5], [1, 2, 3, 4, 5], [10, 20, 30]]
    for lst in test_lists:
        print(f"recursive_sum({lst}) = {recursive_sum(lst)}")

    print("\n=== К3: Рекурсивный бинарный поиск ===")
    arr = [1, 3, 5, 8, 9, 15, 20]
    for t in [8, 1, 20, 100]:
        print(f"binary_search_recursive({t}) = {binary_search_recursive(arr, t)}")

    print("\n=== К4: Класс Stack ===")
    s = Stack()
    print(f"Пустой: {s.is_empty()}")
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"После push: {s}")
    print(f"peek(): {s.peek()}")
    print(f"pop(): {s.pop()}")
    print(f"После pop: {s}")
    print(f"Размер: {s.size()}")