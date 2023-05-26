from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue({
        "nome_do_arquivo": "teste1.txt",
        "qtd_linhas": 6,
    })
    queue.enqueue({
        "nome_do_arquivo": "teste2.txt",
        "qtd_linhas": 3,
    })
    assert len(queue) == 2
    assert queue.search(1)["nome_do_arquivo"] == "teste1.txt"
    queue.dequeue()
    assert len(queue) == 1
    with pytest.raises(IndexError):
        queue.search(4)
    assert queue.is_priority({
        "nome_do_arquivo": "teste1.txt",
        "qtd_linhas": 6,
    }) is False
