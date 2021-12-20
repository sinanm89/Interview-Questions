
sentences = [
    'the quick brown fox',
    'the slow brown cow',
    'to be or not to be that is the question',
]

queries = [
    'the',
    'cow',
    'to',
]


def set_indexes(sentences):
    output_dict = {}
    for sentence_index, sentence in enumerate(sentences):
        words = sentence.split(' ')
        print(output_dict)
        for word_index, word in enumerate(words):
            if output_dict.get(word):
                output_dict[word] = output_dict.get(word, []).append([sentence_index, word_index])
            else:
                output_dict[word] = [[sentence_index, word_index]]
    return output_dict


def find_indexes(index_dict, queries):
    query_output_indexes = {}
    for query in queries:
        query_output_indexes[query] = index_dict.get(query)
    return query_output_indexes


index_dict = set_indexes(sentences)
found_indexes = find_indexes(index_dict, queries)

print(found_indexes)
