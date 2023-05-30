#!/usr/bin/python3
""""This module defines a singly linked list and its nodes"""


class Node:
    """This class represents a node in a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initialises a new Node instance
        Args:
            param1: node data
            param2: pointer to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the Node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the Node data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the pointer to the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class defines a Singly Linked List"""
    def __init__(self):
        """initialise the object"""
        self.__head = None

    def __str__(self):
        """customize printable message"""
        msg = ""
        ptr = self.__head

        while ptr is not None:
            msg += str(ptr.data)
            if ptr.next_node is not None:
                msg += "\n"
            ptr = ptr.next_node

        return msg

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
        in the list (increasing order)

        Args:
            param1: the value to be inserted
        """

        ptr = self.__head
        while ptr is not None:
            if value < ptr.data:
                break
            pre_ptr = ptr
            ptr = ptr.next_node

        new_node = Node(value, ptr)

        if ptr == self.__head:
            self.__head = new_node
        else:
            pre_ptr.next_node = new_node
