from abc import ABC, abstractmethod

class Observable :
    def __init__(self):
        self.state = False
        self.observers = []

    def add_observers(self, observer) :
        return self.observers.append(observer)
    
    def notify_observers(self) :
        if (self.state) :
            self.state = False
            for obs in self.observers :
                obs.action(self)

    def clear_observers(self) :
        self.observers = []

    def set_changed(self) :
        self.state = True

    def remove_observers(self, observer) :
        self.observers.pop(self.observers.index(observer))


class Observer(ABC) :
    @abstractmethod
    def action(self, observable) :
        pass