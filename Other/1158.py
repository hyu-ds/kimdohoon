num, ind = map(int, input().split())

class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

head = Node(1)
first_node = head
for i in range(2, num+2):
    if i == num+1:
        head.next = first_node
    else:
        head.next = Node(i)
    head = head.next

output = '<'
while True:
    if head != head.next:
        for _ in range(ind-1):
            head = head.next
        n = head.data
        output += f'{n}, '

        while head.next.data != n:
            head = head.next
        
        head.next = head.next.next
        head = head.next
    else:
        output += f'{head.data}>'
        break
print(output)