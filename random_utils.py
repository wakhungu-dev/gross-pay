import random
for i in range(10):
    x = random.Random()
    print(x)
    print(x.random())
    print(x.randint(1, 10))
    print(x.choice([1, 2, 3, 4, 5]))
    print(x.choices([1, 2, 3, 4, 5], k=2))
    print(x.shuffle([1, 2, 3, 4, 5]))
    print(x.sample([1, 2, 3, 4, 5], 3))
    print(x.uniform(1, 10))
    print(x.triangular(1, 10))
