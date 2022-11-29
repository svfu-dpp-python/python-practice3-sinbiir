# Объектно-ориентированное программирование

## Свойства (динамические атрибуты)

В классе можно создать **свойства** — методы, к которым можно обращаться как к атрибутам класса.

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

## Методы класса

```python
class (object):
    

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s, %s)" % (cls, x)
```

## Статические методы

```python
class A(object):
    def foo(self,x):
        print "executing foo(%s, %s)" % (self, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x
```

## Специальные методы класса

* `__new__()` — конструктор класса, вызывающийся когда объект еще не создан.
* `__init__()` — конструктор объекта.
* `__del__()` — деструктор объекта.
* `__repr__()` — строковое представление объекта.
* `__str__()` — 
* `__enter__()` — 
* `__exit__()` — 
* `__getitem__()` — 
* `__setitem__()` — 
* `__getattr__()` — 
* `__setattr__()` — 

Работа с итераторами:

* `__iter__()`
* `__next__()`

Арифметические операции:

* `__add__()`
* `__mul__()`
* `__sub__()`
* `__div__()`

Сравнения:

[Описание в документации](https://docs.python.org/3/reference/datamodel.html#special-method-names)
