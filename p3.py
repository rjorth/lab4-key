import sys

class Node(object):
    def __init__(self, v, n):
        self.value = v
        self.next = n
class LinkedList(object):
    def __init__(self):
        self.firstLink = None
    def add (self, newElement):
        self.firstLink = Node(newElement, self.firstLink)
    def test(self, testValue):
        current = self.firstLink
        found = False
        while current and not found:
            if current.testValue == testValue:
                found = True
                return True
            else:
                current = current.next
            if not current:
                return False
    def remove(self, testValue):
        if self.testValue == testValue:
            self.testValue = self.next.testValue
            self.next = self.next.next
            return True
        if self.next == None:
            return False
        if self.next.testValue == testValue:
            self.next = self.next.next
            return True
        return remove(self.next,testValue)
    def len(self):
        temp = self.firstLink
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count
    def reverse(self):
        if self == None: return
        head = self
        tail = self.next
        reverse(tail)
        print head
        reverse(object)
    def Lprint(self):
        node = self.firstLink
        while node:
            print node.data
            node = node.next
