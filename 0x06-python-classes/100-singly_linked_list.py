#!/usr/bin/python3

"""define a class for a single linked list"""


class Node:
    """represent a new node"""

    def __init__(self, data, next_node=None):
        """initializing a new node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returning the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retriieving the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("ext_node must be a Node object")
        self.__next_node = value


"""define a singly linked list"""


class SinglyLinkedList:
    """represents a singly linked list"""

    def __init__(self):
        """initializing the head of the list"""
        self.head = None

    def sorted_inserted(self, value):
        """inserts a new node"""
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node

        else:
            current_node = self.head
            while current_node.next_node is not None and current_node.next_node <= value:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        output = ""
        current_node = self.head
        while current_node is not None:
            output += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return output

