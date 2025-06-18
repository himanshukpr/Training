a_age = 25
b_age = a_age # reference Copy operation
c_age = 25 # will make the new storage of the stack but will refere to the same heap HASHCODE 

# if it delete both then it will be dynamic opinter
del a_age # this will just delete the reference of the variable a_age from the stack but not from the  heap

# If it will not delete from the heap then it will be a memory leak

# print(a_age, id(a_age), type(a_age))
print(b_age, id(b_age), type(b_age))
print(c_age, id(c_age), type(c_age))

# hashing function
# Bucket size = 11
# f(x) X % size

# X = 100


 