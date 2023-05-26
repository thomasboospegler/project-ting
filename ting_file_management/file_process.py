from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
    if len(instance) > 0:
        for file in instance._data:
            if file['nome_do_arquivo'] == path_file:
                return None
    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    file_name = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    return sys.stdout.write(
        f"Arquivo {file_name} removido com sucesso\n"
    )


def file_metadata(instance, position):
    try:
        return sys.stdout.write(str(instance.search(position)))
    except IndexError:
        return sys.stderr.write(
            "Posição inválida"
        )
