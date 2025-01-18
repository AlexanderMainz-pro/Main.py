class SampleClass:
    def __init__(self, name):
        self.name = name
        self.value = 42

    def greet(self):
        return f"Hello, {self.name}!"

def introspection_info(obj):
    info = {
        "type": str(type(obj)),
        "attributes": dir(obj),
        "methods": [method for method in dir(obj) if callable(getattr(obj, method))],
        "module": obj.__module__,
        "doc": obj.__doc__,
    }
    return info

# Пример использования
sample = SampleClass("Alice")
info = introspection_info(sample)

for key, value in info.items():
    print(f"{key}: {value}")