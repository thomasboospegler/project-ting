from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        if index not in range(0, len(self._data)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
