
class Observable:

    def __init__(self):
        self.observers = []

    def add_observer(self, o):
        self.observers.append(o)
        self.notify_observers()

    def notify_observers(self):
        for o in self.observers:
            o.update(self)