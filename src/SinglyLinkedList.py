# Classe do nó da linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Classe da linked list
class SinglyLinkedList:

    # Construtor da linked list
    def __init__(self):
        self.head = None

    # Inserindo valores na linked list
    def append(self, data):

        new_node = Node(data)

        # Se a lista estiver vazia, insere na cabeça (head)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        # Pega o ultimo elemento da linked list para inserir após ele
        while current_node.next:
            current_node = current_node.next

        # Insere no final da linked list
        current_node.next = new_node
        return

    # Pega um elemento da linked list pelo indice
    def get(self, index):

        # Verifica se o indice informado é inválido
        if index > self.length() or index < 0:
            print("Error: Index out of range")
            return None
        idx = 0
        current_node = self.head

        # Busca e retorna o respectivo item
        while current_node is not None:
            if index == idx:
                return current_node.data
            current_node = current_node.next
            idx += 1

    # Verifica se determinado item existe na linked list
    def search_item(self, item):
        current_node = self.head
        while current_node:
            if current_node.data == item:
                print("item is in the linked list.")
                return True
            current_node = current_node.next
        print("item is not in the linked list.")
        return False

    # Insere no início da linked list
    def insert_at_start(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    # Remove do inicio da linked list
    def remove_at_start(self):
        current_node = self.head
        if current_node is None:
            print("Linked List is empty.")
            return None
        self.head = self.head.next

    # Insere no fim da linked list
    def insert_at_end(self, item):
        current_node = self.head
        node = Node(item)
        if current_node is None:
            self.head = node
            return
        while current_node:
            if current_node.next is None:
                current_node.next = node
                return
            current_node = current_node.next

    # Remove no fim da linked list
    def remove_at_end(self):
        current_node = self.head
        if current_node is None:
            print("Linked List is empty.")
            return
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None

    # Retorna o tamanho da linked list
    def length(self):
        len = 0
        if self.head is None:
            return len

        current_node = self.head
        while current_node:
            len += 1
            current_node = current_node.next
        return len

    # Converte de linked list para list
    def to_list(self):
        nodes_list = []
        current_node = self.head
        while current_node:
            nodes_list.append(current_node.data)
            current_node = current_node.next
        return nodes_list

    # Mostra todos os nós(elementos) da linked list
    def show_nodes(self):
        current_node = self.head
        if current_node is None:
            print("singly linked list has no elements.")

        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # Reverte a linked list
    def reverse_linked_list(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head = previous_node

    # Insere um item na linked list pelo indice
    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 1
        current_node = self.head
        while i < index-1 and current_node is not None:
            current_node = current_node.next
            i = i + 1
        if current_node is None:
            print("ERROR: Index out of range.")
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    # Remove elemento da linked list pelo valor
    def remove_element_by_value(self, value):
        current_node = self.head

        # Verifica se a cabeça (head) contém o valor a ser excluído
        if current_node is not None:
            if current_node.data == value:
                self.head = current_node.next
                current_node = None
                return

        # Procura pelo valor a ser excluido, salvando o nó anteior
        # pos precisamos alterar o seu 'next'
        while current_node is not None:
            if current_node.data == value:
                break
            prev = current_node
            current_node = current_node.next

        # Se o valor não estiver na linked list
        if current_node is None:
            return

        # Removendo nó da linked list
        prev.next = current_node.next
        current_node = None
