temperature = 38.5
original = temperature

print("Temperature = {0}".format(id(temperature)))
print("Original    = {0}".format(id(original)))
print()

temperature = 100.05
original += 50

print("Temperature = {0}".format(id(temperature)))
print("Original    = {0}".format(id(original)))
print()

original -= 50

print("Temperature = {0}".format(id(temperature)))
print("Original    = {0}".format(id(original)))
print()