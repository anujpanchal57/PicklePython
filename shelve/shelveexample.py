import shelve

# SHELVE basically doesn't require its mode to be specified, it is generally READ/WRITE by nature

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

print(fruit)


# This is same as the above code but it is done using KEY and VALUE PAIRS
with shelve.open('ShelfTest') as fruit:
    fruit = {"orange": "a sweet, orangish fruit",
             "apple": "good for making cider",
             "lemon": "a sour, yellow citrus fruit",
             "grape": "a small, sweet fruit",
             "lime": "a sour, green citrus fruit"}

print(fruit["lemon"])
print(fruit["apple"])

print(fruit)

# Another alternative instead of using WITH command, we can directly
# declare a variable FRUIT and pass the SHELVE in it and it will give the same results
fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit"
fruit['lime'] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])

# But in this approach we have to close the shelve manually
fruit.close()

print(fruit)

