from node import Node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node


node_1 = Node("First node")
node_2 = Node("Second node")
node_3 = Node("Third node")
node_4 = Node("First node")

my_ll = LinkedList()

my_ll.insert_beginning(node_1.get_value())
my_ll.insert_beginning(node_2.get_value())
my_ll.insert_beginning(node_3.get_value())
my_ll.insert_beginning(node_4.get_value())
print(my_ll.stringify_list())
my_ll.remove_node("First node")
print(my_ll.stringify_list())
