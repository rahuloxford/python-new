
name = '"tim" olsen'
print(name)
place = "india 'gate'"
print(place)

phrase = r"the \king\ in \tthe \north\\"
print(phrase)

# multiline string
global_warning = '''the increase in the temperature
of the earth’s atmosphere,
caused by the increase
of certain gases'''

print(global_warning)


#indexing

# index: 01234567
show = "ramayana"

print(show)
# print a peice of the using their index numbers 
print(show[4])
#print(show[8]) # error: index out of bound
#print(show[-4])
print(show[len(show) - 1])
print(show[0:5])
print(show[2:6])
print(show[0:20])

print(show[:5])
print(show[2:])
print(show[:])


