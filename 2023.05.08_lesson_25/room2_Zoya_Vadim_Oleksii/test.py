# class Node:
#
#     def __init__(self, data, next_node = None):
#         self.data = data
#         self.next_node = next_node
#
# class LinkedList:
#
#     def __init__(self, root = None):
#         self.root = root
#         self.size = 0
#
#     def add(self, data):
#         new_node = Node(data, self.root)
#         self.root = new_node
#         self.size += 1
#
#     def __repr__(self):
#         next_n = self.root
#         res = ''
#         while next_n:
#             res += str(next_n.data) + '->'
#             next_n = next_n.next_node
#         return res
#
#     def remove(self, data):
#         this_node = self.root
#         prev_node = None
#         while this_node:
#             if this_node.data == data:
#                 if prev_node:
#                     prev_node.next_node = this_node.next_node
#                 else:
#                     self.root = this_node.next_node
#                 self.size -= 1
#                 return True
#             else:
#                 prev_node = this_node
#                 this_node = this_node.next_node
#         return False

# клас, в якому зберігається кожен елемент списку та посилання на його наступний член
# class Node:
#    def __init__(self, dataval=None):
#       self.dataval = dataval
#       self.nextval = None
#
#
# class SLinkedList:
#    def __init__(self):
#       self.headval = None
#    # почерзі виводить кожен елемент списку
#    def listprint(self):
#        printval = self.headval
#        while printval is not None:
#            print(printval.dataval)
#            printval = printval.nextval
#
#    def AtBegining(self, newdata):
#        NewNode = Node(newdata)
#        # Update the new nodes next val to existing node
#        NewNode.nextval = self.headval
#        self.headval = NewNode
#
#    def AtEnd(self, newdata):
#        NewNode = Node(newdata)
#        if self.headval is None:
#            self.headval = NewNode
#            # return
#        laste = self.headval
#        while (laste.nextval):
#            laste = laste.nextval
#        laste.nextval = NewNode
#
#    def Inbetween(self, middle_node, newdata):
#        if middle_node is None:
#            print("The mentioned node is absent")
#            return
#        NewNode = Node(newdata)
#        NewNode.nextval = middle_node.nextval
#        middle_node.nextval = NewNode
#
#    def RemoveNode(self, Removekey):
#        HeadVal = self.headval
#        if (HeadVal is not None):
#            if (HeadVal.dataval == Removekey):
#                self.headval = HeadVal.next
#                HeadVal = None
#                return
#        while (HeadVal is not None):
#            if HeadVal.dataval == Removekey:
#                break
#            prev = HeadVal
#            HeadVal = HeadVal.nextval
#        if (HeadVal == None):
#            return
#        prev.nextval = HeadVal.nextval
#        HeadVal = None
#
# list1 = SLinkedList()
# list1.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
# # Link first Node to second node
# list1.headval.nextval = e2
# # Link second Node to third node
# e2.nextval = e3
# list1.AtBegining('Sun')
# list1.AtEnd("Thu")
# list1.Inbetween(list1.headval.nextval.nextval.nextval.nextval, "1")
# list1.RemoveNode('1')
# list1.listprint()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.index = -1

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.index += 1
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.index += 1

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next

    def find(self, elem):
        current = self.head
        # res = False
        while current is not None:
            if current.data == elem:
                # res = True
                return True
            current = current.next
        return False

    def remove(self, elem):
        current = self.head
        previos = None
        while current is not None:
            if current.data == elem:
                previos.next = current.next
                print(elem, 'removed')
                return
            previos = current
            current = current.next
        print(elem, 'not removed')

    def find_ind(self, data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                return index
            index += 1
            current = current.next
        return False

    def insert_ind(self, index, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.index = index
            self.index = 0
            return
        # current = self.head
        # index = 0
        # while current is not None:
        #     if current.data == data:
        #         # res = True
        #         return index
        #     index += 1
        #     current = current.next
        # return False







linked_list = LinkedList()
linked_list.append(1)
linked_list.append("2")
linked_list.append("Stas")
linked_list.print_list()
print(linked_list.find("1"))
linked_list.remove("2")
print(linked_list.index)
print(linked_list.find_ind("Stas"))
linked_list.insert_ind(2, '2')
linked_list.print_list()

