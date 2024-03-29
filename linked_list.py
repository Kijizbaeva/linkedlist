class LinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Item:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __len__(self):
        return self.length

    def append_begin(self, data):
        new_unit = LinkedList(data)
        new_unit.next = self.head
        self.head = new_unit
        self.length += 1

    def append_end(self, data):
        new_unit = LinkedList(data)
        if not self.head:
            self.head = new_unit
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_unit
        self.length += 1

    def remove_first(self):
        if not self.head:
            raise ValueError('Пустой список')
        self.head = self.head.next
        self.length -= 1

    def remove_last(self):
        if not self.head:
            raise ValueError('Пустой список')
        if not self.head.next:
            self.head = None
        else:
            second_last = self.head
            while second_last.next.next:
                second_last = second_last.next
            second_last.next = None
        self.length -= 1

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise ValueError('Неправильный индекс')
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.length -= 1

    def remove_first_value(self, value):
        if not self.head:
            raise ValueError('Пустой список')
        
        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next
        raise ValueError('Нет значения')

    def remove_last_value(self, value):
        if not self.head:
            raise ValueError('Пустой список')
        
        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return      
        current = self.head
        while current.next:
            if current.next.data == value and not current.next.next:
                current.next = None
                self.length -= 1
                return
            if current.next.data == value:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next
        raise ValueError('Нет значения')