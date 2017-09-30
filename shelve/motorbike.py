import shelve

# with shelve.open("bike") as bike:

# I've renamed this as BIKE2 to see that if it shows an error
# But now if we see our project files, then code has created database files
with shelve.open("bike2") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["colour"] = "black"
    # bike["engine_size"] = 250

    # If I print this line, it will still give us the result as 250 as it has created database
    # of its own after executing the code
    # print(bike["engin_size"])

    # del bike["engin_size"]

    # This will print MAKE, MODEL, COLOUR and ENGINE_SIZE
    for key in bike:
        print(key)

    # print(bike["engin_size"])
    print(bike["engine_size"])
    print(bike["colour"])


#     # I've made this mistake deliberately to see that if it shows the error or not
#     bike["engin_size"] = "250"

