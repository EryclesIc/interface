class Node:
    # função construtora que define como o nó vai ser iniciado
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # função construtora que define como a lista vai ser iniciada
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):  # função que adiciona um novo elemento na lista
        if self.head:
            # inserção quando a lista já possui elemento
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    # como a lista não pode ser exibida de forma sequencial,
    # a função abaixo possibilita que a lista seja exibida
    # enviando o indice em colchetes assim como a sequencial
    # é exibida.
    # ex.: print(lista[1])
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    # como a lista não pode setar um valor de forma direta pelo indice,
    # como na lista sequencial, a função abaixo possibiita que a lista set um novo valor
    # para um nó pelo seu indice, assim como é feito na lista sequencial
    # ex.: lista[1] = elem
    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    # a função abaixo recebe o elemento e ao passar por toda a lista, retorna o indice dele
    def index(self, elem):
        """Retorna o indice do elem na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError("{} is not in list".format(elem))

    # a função abaixo remove um elemento da lista
    def remove(self, elem):
        if self.head is None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            return True
        raise ValueError("{} is not in list".format(elem))

    # as funções a baixo possibilitam que a lista seja exibida por completo
    # printando ela de forma direta
    # ex.: print(lista)
    def __repr__(self):
        r = ""
        pointer = self.head
        while pointer:
            if pointer.next is None:
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

lista = LinkedList()
lista.append(1)
lista.append(3)
lista.append(2)
print(lista)
print("\n")
print(lista.index(3))
