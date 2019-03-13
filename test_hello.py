# This program says hello and asks for my name

def greet(name):
    return 'It is good to meet you, ' + name

def measure(name):
    return len(name)

def increment(age):
    return age + 1

def test_greet():
    assert greet('Ricky') == 'It is good to meet you, Ricky'

def test_measure():
    assert measure('Ricky') == 5

def test_increment():
    assert increment(31) == 32
