'''
Cracking the coding interview
Chapter 3 - Stacks and Queues
Page 96
----------------------------------------
Summary: Learning stacks and queues in Python
Constraits or Questions you need to ask:
Solution notes:
'''
from collections import deque

#Stack is a collection of data where you can only add to the top
#and remove from the top
#LIFO: Last In First out 
#Let's implement a stack
data = []
#Add to the top of the stack known as a Push
data.append(5)
data.append(10)
data.append(15)
data.append(20)
#Pop from the top of the stack known as a Pop
elements = data.pop()
print(elements)

#Peek at the top of the stack
print(data[len(data) - 1])







#Queue is a collection of data where you add to the end and remove
#from the front
#FIFO: First In First Out
#Initalizing queue as a list
queue = []

#Appending data to the queue known as a enqueue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

#Pop data from queue with a (0) known as a dequeue
queue.pop(0)
popper = queue.pop(0)

#Peek method for queues that will look at the first in line
print(queue[0]) 



#Deque - a datastructure that be added or removed from the right or left
data_deque = deque()

#Appending to the right by using .append()
data_deque.append("Raj")
data_deque.append("Elmo")
data_deque.append("Chris")
data_deque.append("Tyler")
data_deque.append("Andrew")

#Pop from the left using .popleft()
dequePopleft = data_deque.popleft()

#Pop from the right using .pop()
dequePopright = data_deque.pop()

print(dequePopleft, data_deque)

print(dequePopright, data_deque)
