'''
Queues (FIFO => First In First Out / LILO => Last In Last Out)
 
=> enqueue (insert)
=> dequeue (remove)
=> front (first element)
=> size (length of queue)
'''

queue = [1, 2, 3, 4, 5]

# insert element to queue
queue.append(6)
print(queue)

# remove element from queue
queue.pop(0)
print(queue)

# get the front of queue
print(queue[0])

# get the size of queue
print(len(queue))