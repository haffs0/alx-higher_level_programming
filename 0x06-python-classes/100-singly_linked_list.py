#!/usr/bin/python3
"""A singly linked list in python"""


class Node:
    """creates a node class object."""

    def __init__(self, data, next_node=None):
        """Initialize the data."""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """get the value of private variable data"""
        return self.__data

    @data.setter
    def size(self, value):
        """change the value of size."""
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """point to next node"""
        if not isinstance(value, Node) or value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """create a singlylinkedlist"""

    __head = None

    def __init__(self):
        """initialize the data"""
        pass

    def sorted_insert(self, value):
        """insert data into the to the node."""

        new = Node(value, self.__head)
        self.__head = new

    def __str__(self):
        "print element in the linked lists"""
        values = []
        while(self.__head):
            values.append(self.__head.data)
            self.__head = self.__head.next_node
        return ("\n".join([str(x) for x in sorted(values)]))
