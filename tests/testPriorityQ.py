import PriorityQ as pq

q = pq.PriorityQ(4)

print(q)
q.insert_with_piority('Item 1', 3)
print(q)
q.insert_with_piority('Item 2', 1)
print(q)
q.insert_with_piority('Item 3', 0)
print(q)
q.insert_with_piority('Item 4', 5)
print(q)
q.insert_with_piority('Item 5', 1)
print(q)
q.insert_with_piority('Item 6', 3)
print(q)
q.insert_with_piority('Item 7', 0) # Item 7 should not be included in the Q (and it is not indeed)
print(q)

a = q.get_front_element()
print(a)
b = q.get_front_element()
print(b)

a = tuple([2,3])
b = tuple([2,3])
print(a == b)