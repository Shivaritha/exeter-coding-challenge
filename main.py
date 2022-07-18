import csv
import tracemalloc
import time
from collections import Counter
import pandas as pd
#from memory_profiler import memory_usage
#from time import sleep


def ReplaceDict():
    with open('french_dictionary.csv', mode='r') as inp:
        reader = csv.reader(inp)
        dicty = {rows[0]: rows[1] for rows in reader}

    file1 = open('find_words.txt', 'r')
    Lines = file1.readlines()
    replaced_texts = []

    with open('t8.shakespeare.txt', 'r') as file:
        data = file.read()

    for line in Lines:
        search_text = line.strip()
        replace_text = dicty[search_text]

        data = data.replace(search_text, dicty[search_text])
        if replace_text in data:
            replaced_texts.append(replace_text)

    with open('t8.shakespeare.translated.txt', 'w') as file:
        file.write(data)  # writing on file

    print("Replaced Words are: ")
    print(replaced_texts)
    print("Number of words that are replaced are: " + str(len(replaced_texts)))
    unique = set(replaced_texts)
    print("Number of Unique words that are replaced are: " + str(len(unique)))
    print("Count of Replaced words are: ")
    print(Counter(replaced_texts))

    frequency = {}
    # iterating over the list
    for item in replaced_texts:
        # checking the element in dictionary
        if item in frequency:
            # incrementing the counr
            frequency[item] += 1
        else:
            # initializing the count
            frequency[item] = 1

    # printing the frequency
    print(frequency)



    items = pd.Series(replaced_texts).value_counts().sort_values(ascending=False)
    items.columns = ['items', '#counts']

    items.to_csv('D:/college/internshipExter/internship/frequency.csv' , header=True)



tracemalloc.start()

st = time.time()
ReplaceDict()

#(curreny memory, peak memory)
print("Memory used in processing the code:(current memory, peak memory)")
print(tracemalloc.get_traced_memory())

#mem_usage = memory_usage(ReplaceDict)
#print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
#print('Maximum memory usage: %s' % max(mem_usage))
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
with open('performance.txt', 'w') as file:
    file.write(str(elapsed_time))

tracemalloc.stop()
