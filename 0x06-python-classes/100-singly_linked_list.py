#!/usr/bin/python3

"""Module defines classes Node and SinglyLinkedList for a singly-linked list"""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Constructor for Node.
        Args:
            data (int): Data for a new Node instance.
            next_node (Node): Next node of the new Node intance.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the data of the Node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the data of the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Constructor for SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node to the SinglyLinkedList in asccending order
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Return string representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
