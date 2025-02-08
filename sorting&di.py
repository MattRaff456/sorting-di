#Sorting
a = [5, 132, 123213312, 1]
print(sorted(a)) #prints the sorted numbers

#Custom sorting with key=
st = ['casdas', 'asdsa', 'd', 'bb']
print(sorted(st, key=len)) #prints the sorted keys based off a the length of the string

st = ['aNDANSD', 'AKSDNAS', 'N', 'DD']
print(sorted(st, key=str.lower)) #prints the sorted keys but treats them all the same via the .lower

#Dict formatting
h = {}
h['word'] = 'garfield'
h['count'] = 42
s = 'I want %(count)d copies of %(word)s' % h
#s = 'I want {count:d} copies of {word}'.format(h)

#Del
var = 6
del var #deletes var
list = ['a', 'b', 'c']
del list[0]
del list[1] #deletes the element at index 1
print(list)

#Files unicode
#with open('foo.txt', 'rt', encoding='utf-8') as f:
    #for line in f:
    #here line is a unicode string

#with open('write_test', encoding='utf-8', mode='wt') as f:
    #f.write('\u20ACunicode\u20AC\n')