def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

# Example usage of bubble sort
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)

# Example usage of Car class
my_car = Car("Toyota", "Camry", 2023)
print(my_car.get_info())
print(my_car.accelerate(30))
print(my_car.brake(10))

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self, increment):
        self.speed += increment
        return f"Speed increased to {self.speed} mph"
    
    def brake(self, decrement):
        if self.speed - decrement >= 0:
            self.speed -= decrement
        else:
            self.speed = 0
        return f"Speed decreased to {self.speed} mph"
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

