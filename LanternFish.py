import time
start_time = time.time()

class Node:
    def __init__(self, count):
        self.count = count
        self.next = None

def linked_list_create_node(val):
    return Node(val)

def linked_list_head_init(val):
    return linked_list_create_node(val)

def linked_list_push_back(head, val):
    iter = head
    added = linked_list_create_node(val)
    while iter.next is not None:
        iter = iter.next
    iter.next = added

def linked_list_pop_front(head):
    result = head.count
    head = head.next
    return head, result

def linked_list_destroy(head):
    while head is not None:
        head, _ = linked_list_pop_front(head)

def linked_list_increment(head, pos, val):
    iter = head
    for _ in range(pos):
        iter = iter.next
    iter.count += val

def linked_list_print(head):
    iter = head
    while iter is not None:
        print(f"{iter.count} -> ", end="")
        iter = iter.next
    print()

def linked_list_sum(head):
    total = 0
    iter = head
    while iter is not None:
        total += iter.count
        iter = iter.next
    return total

# Example usage
node0 = linked_list_head_init(0)
node1 = linked_list_create_node(1)
node2 = linked_list_create_node(1)
node3 = linked_list_create_node(2)
node4 = linked_list_create_node(1)
node5 = linked_list_create_node(0)
node6 = linked_list_create_node(0)
node7 = linked_list_create_node(0)
node8 = linked_list_create_node(0)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

head = node0
for _ in range(256):
    head, res = linked_list_pop_front(head)
    linked_list_push_back(head, res)
    linked_list_increment(head, 6, res)

print(linked_list_sum(head))


print("Execution time: %s seconds" % (time.time() - start_time))


