#!/usr/bin/env python
# coding: utf-8

# **HackerRank---> DataStructure ---> Linked List --->nserting a Node Into a Sorted Doubly Linked List---> Python**
# 
# **Problem:**  Given a reference to the head of a doubly-linked list and an integer, **data**, create a new DoublyLinkedListNode object having data value **data** and insert it at the proper location to maintain the sort.

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    Node = DoublyLinkedListNode(data)
    
    if llist is None:
        llist = Node
        Node.next = None
    if llist.data > data:
        Node.next = llist
        llist.prev = Node
        llist = Node 
    else:
        head = llist
        while head.next is not None and head.data <data:
            head = head.next
        if head.next is None and head.data < data:
            head.next = Node
            Node.prev = head
        else:
            head.prev.next = Node
            Node.prev = head.prev
            Node.next = head
            head.prev = Node


    return llist
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

