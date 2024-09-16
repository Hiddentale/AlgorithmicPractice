from queue import Queue, LifoQueue

queue = Queue()
n = 25
elements = [i for i in range(0, n)]

for element in elements:
    queue.put(element)
    
stack = LifoQueue()

while queue.qsize() > 0:
    stack.put(queue.get())

while stack.qsize() > 0:
    queue.put(stack.get())

new_list = []

while queue.qsize() > 0:
    new_list.append(queue.get())

print(elements)
print(new_list)


from queue import Queue, LifoQueue

first_queue = Queue()
second_queue = Queue()

n = 25
elements = [i for i in range(0, n)]

for element in elements:
    first_queue.put(element)
    
while first_queue.qsize() > 1:
    second_queue.put(first_queue.get())

for i in range(1, n):
    for j in range(n - i, 1, -1):
        second_queue.put(second_queue.get())
    first_queue.put(second_queue.get())
    
new_list = []

while first_queue.qsize() > 0:
    new_list.append(first_queue.get())

print(elements)
print(new_list)

