# Объектно-ориентированное программирование

## Методы класса

В классе можно создать метод который привязан к классу, а не к объекту:

```python
class Car:
    tax_rate = 0.5

    @classmethod
    def set_tax_rate(cls, new_tax_rate):
        # данный метод изменяет общий для всех автомобилей процент налога
        cls.tax_rate = new_tax_rate

    def __init__(self, model, price):
        self.model = model
        self.price = price
    
    def get_tax(self):
        return self.price * self.tax_rate / 100.0

camry = Car('Toyota Camry', 2_000_000)
largus = Car('Lada Largus', 1_000_000)
print(camry.get_tax())  # 10000
print(largus.get_tax())  # 5000
Car.set_tax_rate(0.2)
print(camry.get_tax())  # 4000
print(largus.get_tax())  # 2000
```

## Свойства (динамические атрибуты)

В классе можно создать **свойства** — методы, к которым можно обращаться как к атрибутам класса:

```python
class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# обращаемся к full_name как будто это атрибут, а не метод
p = Person('Smith', 'John')
print(p.full_name)  # John Smith
```

## Статические методы

В классе можно создать метод, который привязан к классу только формально.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def hello(self):
        return f"Привет, я {self.breed} по кличке {self.name}!"

    @staticmethod
    def new_bulldog(name):
        return Dog(name, 'бульдог')

    @staticmethod
    def new_kolli(name):
        return Dog(name, 'колли')

lassie = Dog.new_kolli('Лесси')
print(lassie.hello())  # Привет, я колли по кличке Лесси!
```

## Специальные методы класса

* `__init__(self, ...)` — конструктор объекта, вызывается для инициализации объекта.
* `__str__(self)` — возвращает результат преобразования объекта в строку (например при печати объекта).

```python
class Car:
    def __init__(self, model, number):
        self.model = model
        self.number = number 

    def hello(self):
        return f"Автомобиль {self.model} с госномером {self.number}"

car = Car("Toyta Land Cruiser", "A222AA")
print(car)  # Автомобиль Toyta Land Cruiser с госномером A222AA
```

Арифметические операции:

* `__add__(self, other)` — вызывается при сложении.
* `__mul__(self, other)` — вызывается при умножении.
* `__sub__(self, other)` — вызывается при вычитании.
* `__div__(self, other)` — вызывается при делении.

[Описание в документации](https://docs.python.org/3/reference/datamodel.html#special-method-names)
