class Product:
    _discount = 0

    def __init__(self, name, price):
        self._price = price
        self.name = name
        
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if price<=0:
            return
        self._price = price
        return
    
    @classmethod
    def get_discount(cls):
        return cls._discount

    @classmethod
    def set_discount(cls, discount):
        if discount>0:
            cls._discount = discount
        return
    
    @property
    def current_price(self):
        return self._price - self._price/100*self._discount
    
    def create_fix_price(self, name):
        self.name = name
        self._price = 99

    def __str__(self):
        return self.name + self._price