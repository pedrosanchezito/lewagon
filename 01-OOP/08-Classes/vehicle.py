# pylint: disable=missing-docstring

class Vehicle(object):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.started = False

    def start(self):
        self.started = True
        return self.started

    def stop(self):
        self.started = False
        return self.started
