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
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode


    def append(self, value: Any) -> None:
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode


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
        newnode = Node(value)
        newnode.next = after.next
        after.next = newnode


    def pop(self) -> Any:
        if self.head != None:
            currnode = self.head
            self.head = currnode.next
            return currnode.value


    def remove_last(self) -> Any:
        newnode = self.head
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
            newnode = self.node(len(self)-3)
            self.tail = newnode
            newnode = newnode.next
            deleted = newnode.next
            newnode.next = None
            return deleted.value


    def remove(self, after: Node) -> Any:
        newnode = self.head
        if after.next == self.tail:
            deleted = self.tail
            self.remove_last()
        else:
            while newnode.next != after:
                newnode = newnode.next
            deleted = newnode.next
            newnode.next = after.next
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


