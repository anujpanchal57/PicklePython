# Imported Pickle Module
import pickle

imelda = ('More Mayhem', 'Imelda May', '2011',
          ((1, 'Pulling the rug'),
          (2, 'Psycho'),
          (3, 'Mayhem'),
          (4, 'Kentish House Waltz')))

# This line writes the content into the 'imelda.pickle' file
with open("imelda.pickle", 'wb') as pickle_file:
    # This dumps the contents of imelda tuple in pickled file
    pickle.dump(imelda, pickle_file)

# Reading the contents from IMELDA.PICKLE file
with open("imelda.pickle", 'rb') as imelda_pickled:
    # Loads the content in var IMELDA2
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)

# Prints the track number and track titles in the output
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

imelda = ('More Mayhem', 'Imelda May', '2011',
          ((1, 'Pulling the rug'),
          (2, 'Psycho'),
          (3, 'Mayhem'),
          (4, 'Kentish House Waltz')))

# we added two lists EVEN and ODD
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

# This line writes the content into the 'imelda.pickle' file
with open("imelda.pickle", 'wb') as pickle_file:
    # This dumps the contents of imelda tuple in pickled file
    # Also, there are different kinds of protocols in PICKLE
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    # Pickling EVEN, ODD and a random number
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

# Reading the contents from IMELDA.PICKLE file
with open("imelda.pickle", 'rb') as imelda_pickled:
    # Loads the content in var IMELDA2
    imelda2 = pickle.load(imelda_pickled)
    # Reading the EVEN, ODD and random number X from imelda.pickle
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)

# Prints the track number and track titles in the output
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

# Printing out EVEN, ODD and RANDOM NUMBER X
print("= " * 40)

for i in even_list:
    print(i)

print("= " * 40)

for i in odd_list:
    print(i)

print("= " * 40)

print(x)

print("= " * 40)

# This piece of code is to remove the file IMELDA.PICKLE you can observe the DEL in the command
pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")

