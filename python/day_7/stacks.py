'''
Stacks (FILO => First In Last Out / LIFO => Last In First Out)

=> push (insert)
=> pop (remove)
=> peep / top (get top element)
=> size (get the length of stack)
'''

stack = [1, 2, 3, 4, 5]

# insert element into stack
stack.append(6)
print(stack)

# remove element from stack
stack.pop()
print(stack)

# get the top element in stack
print(stack[len(stack) - 1])

# get the size pf stack
print(len(stack))