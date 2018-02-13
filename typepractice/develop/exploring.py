import os
from utilities import directories, file_of_path, non_relavant_words
from collections import Counter
import numpy as np


command = 'find {dir} -name "*.py" {func} ' + file_of_path
os.system(command.format(dir=directories[0], func='>'))

for dir in directories[1:]:
    os.system(command.format(dir=dir, func='>>'))

n_grams = int(raw_input('the n of the n-grams is: '))
unique_grams = int(raw_input('number of unique {n}-grams: '.format(n=str(n_grams))))
n_grams_in_text = int(raw_input('how many n-grams: '))

n_grams_list = []

for file in open('../files/file_paths.txt', "r"):
    file = file.replace('\n', '')
    try:
        file_content = open(file, "r")
    except IOError:
        continue
    words = file_content.read().split()
    for word in set(words) & set(non_relavant_words):
        # import pudb
        # pudb.set_trace()
        while word in words:
            words.remove(word)
    n_grams_list.extend([' '.join(words[i:i+n_grams]) for i in range(len(words) - 2)])

wordcount = Counter(n_grams_list)
n_grams_count = wordcount.most_common(unique_grams)
print(n_grams_count)
n_grams_list = [x[0] for x in n_grams_count]
counts = [x[1] for x in n_grams_count]
total = sum(counts)
probabilities = [x[1]/float(total) for x in n_grams_count]
text = list(np.random.choice(n_grams_list, n_grams_in_text, p=probabilities))
print(' '.join(text))