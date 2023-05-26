def exists_word(word, instance):
    words = []
    search_word = word.lower()

    for element in instance._data:
        for i in range(len(element["linhas_do_arquivo"])):
            if search_word in element["linhas_do_arquivo"][i].lower():
                words.append({"linha": i + 1})
        if len(words) > 0:
            return [{
                "palavra": word,
                "arquivo": element["nome_do_arquivo"],
                "ocorrencias": words
                }]
        return []


def search_by_word(word, instance):
    result = []
    search_word = word.lower()

    for element in instance._data:
        data = {
            "palavra": word,
            "arquivo": element["nome_do_arquivo"],
            "ocorrencias": [],
        }
        count = 1
        for line in element["linhas_do_arquivo"]:
            if search_word in line.lower():
                data["ocorrencias"].append(
                    {"linha": count, "conteudo": line}
                )
            count += 1
        if len(data["ocorrencias"]) != 0:
            result.append(data)
        data["ocorrencias"] == []
    return result
