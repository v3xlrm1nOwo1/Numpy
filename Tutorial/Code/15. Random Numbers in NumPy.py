import numpy as np

### Create Random Number


# 1. Return Random Number Between 0 And !
random_number = np.random.rand()
print(random_number)

# 2. Return Random Number Between low number and hight number
random_number = np.random.randint(10, 100)
print(random_number)

# 3. Return Random Number from List 
random_number = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(random_number)


### Create Random Array

# 1. rand()
random_array = np.random.rand(10)
print(random_array)

random_array = np.random.rand(2,5)
print(random_array)

random_array = np.random.rand(2,3,5)
print(random_array)

# 2. randint()
random_array = np.random.randint(100, size=10)
print(random_array)

random_array = np.random.randint(100, size=(10))
print(random_array)

random_array = np.random.randint(100, size=(2, 5))
print(random_array)

# 3. choice()
random_array = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], size=5)
print(random_array)

random_array = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], size=(2,4))
print(random_array)

random_array = np.random.choice(np.random.randint(1000, size=100), size=(5,10))
print(random_array)


