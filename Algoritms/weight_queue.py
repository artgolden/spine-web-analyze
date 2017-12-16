

class QueueWithWeight:
    def __init__(self, *args):
        # in args is Nodes objects
        self.min_weight = float('inf')
        self.queue_dict = {}
        for i in args:
            self.add(i)


    def add(self, elem):
        if elem.weight < self.min_weight:
            self.min_weight = elem.weight
        if elem.weight in self.queue_dict.keys(): 
            self.queue_dict[elem.weight].append(elem)
        else:
            self.queue_dict[elem.weight] = [elem]
    def pop(self):
        out = self.queue_dict[self.min_weight].pop(0)
        if not self.queue_dict[self.min_weight]:
            self.queue_dict.pop(self.min_weight)
            if self.queue_dict:
                self.min_weight = min(self.queue_dict.keys())
            else:
                self.min_weight = float('inf')
        return out 
    def change(self, elem, old_weight):
        self.queue_dict[old_weight].pop(self.queue_dict[old_weight].index(elem))
        self.add(elem)


        