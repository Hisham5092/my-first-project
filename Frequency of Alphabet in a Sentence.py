from pprint import pprint

Sentence = "Hello world this is python programming"

Frequency = {}

for i in Sentence:
    if i in Frequency:
        Frequency[i] = Frequency[i]+1
    else:
        Frequency[i] = 1
# pprint(Frequency, width=1)
sorted_frequency = sorted(Frequency.items(), key= lambda kv:kv[1], reverse=True)
print(sorted_frequency[1])


