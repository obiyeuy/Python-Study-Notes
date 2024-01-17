'''
fruit=['apple','pear']
fruit.insert(1,'grape')  #插入元素，在指定位置后
print(fruit)
fruit[0:0]=['orange']
print(fruit)
'''

'''
import string

path = 'C:\YYB\Desktop\Walden.txt'

with open(path,'r') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index for index in words_index)}

for word in sorted(counts_dict,key = lambda x:counts_dict[x],reverse = True):
    print('{}--{} times'.format(word,counts_dict[word]))
    '''