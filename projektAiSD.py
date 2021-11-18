from typing import Any


class Node:
    value: Any
    next: 'Node'
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    head: Node
    tail: Node


    def __init__(self):
        self.head = None
        self.tail = None


    def __len__(self):
        Node = self.head
        count = 0
        while Node != None:
            count += 1
            Node = Node.next
        return count


    def __str__(self):
        strn = ""
        node = self.head
        for x in range(len(self)):
            if node.next != None:
                strn += str(node.value) + " -> "
            if node.next == None:
                strn += str(node.value)
            node = node.next
        return strn


    def push(self, value:Any) -> None:
        add_node = Node(value)
        add_node.next = self.head
        self.head = add_node


    def append(self, value: Any) -> None:
        add_node = Node(value)
        if self.head is None:
            self.head = add_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = add_node


    def node(self, at: int) -> Node:
        if at == len(self) - 1:
            Node = self.tail
        if len(self) > at:
            Node = self.head
            for x in range(at):
                Node = Node.next
        return Node


    def insert(self, value: Any, after: Node) -> None:
        if after == self.tail:
            self.append(value)
            return
        if after == None:
            return
        add_node = Node(value)
        add_node.next = after.next
        after.next = add_node


    def pop(self) -> Any:
        if self.head != None:
            rem_node = self.head
            self.head = rem_node.next
            return rem_node.value


    def remove_last(self) -> Any:
        add_node = self.head
        if len(self) == 1:
            deleted = self.head
            self.head = None
            return deleted.value

        if len(self) == 2:
            deleted = self.tail
            self.tail = self.head
            self.head.next = None
            return deleted.value

        if len(self) > 2:
            add_node = self.node(len(self)-3)
            self.tail = add_node
            add_node = add_node.next
            deleted = add_node.next
            add_node.next = None
            return deleted.value


    def remove(self, after: Node) -> Any:
        add_node = self.head
        if after.next == self.tail:
            deleted = self.tail
            self.remove_last()
        else:
            while add_node.next != after:
                add_node = add_node.next
            deleted = add_node.next
            add_node.next = after.next
        return deleted



class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()


    def __len__(self):
        return self._storage.__len__()


    def __repr__(self):
        out = []
        node = self._storage.head
        while node != None:
            out.insert(0, node.value)
            node = node.next
        out = map(str, out)
        out_ = "\n".join(out)
        return out_

    def push(self, element: Any) -> None:
        self._storage.push(element)


    def pop(self) -> Any:
        return self._storage.pop()



class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()


    def __len__(self) -> int:
        return len(self._storage)


    def __repr__(self):
        out = []
        node = self._storage.head
        while node != None:
            out.append(node.value)
            node = node.next
        return out


    def __str__(self):
        str_out = map(str, self.__repr__())
        return ", ".join(str_out)


    def peek(self) -> Any:
        return self._storage.node(0)


    def enqueue(self, element:Any) -> None:
        self._storage.append(element)


    def dequeue(self) -> Any:
        return self._storage.pop()


