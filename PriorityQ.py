from boltons import queueutils as qu

class PriorityQ:

    def __init__(self, size):
        self.size = size
        self.q = qu.SortedPriorityQueue()
        self.dict_tuple_priority = dict()

    def get_front_element(self):
        res = self.q.pop()
        self.dict_tuple_priority.pop(res)
        return res

    def insert_with_piority(self, item, priority):

        if len(self.q) == self.size:
            min_priority = min([a for a in self.dict_tuple_priority.values()])
            if priority >= min_priority:
                self.remove_item_less_priority()
                self.q.add(item, priority)
                self.dict_tuple_priority.setdefault(item, priority)
        else:
            self.q.add(item, priority)
            self.dict_tuple_priority.setdefault(item, priority)


    def remove_item_less_priority(self):
        min_prio = min([a for a in self.dict_tuple_priority.values()])
        item = None
        for i in self.dict_tuple_priority.keys():
            if self.dict_tuple_priority.get(i) == min_prio:
                item = i
                break
        self.dict_tuple_priority.pop(item)
        self.q.remove(item)


    def __str__(self):
        return str(self.dict_tuple_priority)

    def __len__(self):
        return len(self.q)

