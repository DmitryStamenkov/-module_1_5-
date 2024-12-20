#immutable_var = ('D',2,True,5)
#print(immutable_var)
#immutable_var[1] = 4
#print(immutable_var)
#TypeError: 'tuple' object does not support item assignment
mutable_list = ['D',2,True,5]
mutable_list[1] = 4
mutable_list[2] = False
mutable_list.append(11)
mutable_list.remove(5)
print(mutable_list)
