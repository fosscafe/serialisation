import serialization
import pickle

#print (serialization.book_entry)

#WITH clause ensures that the file gets closed when the block inside the WITH clause executes.It doesn’t require to call the close() method explicitly

with open('book_entry.pickle','wb') as bin_file:
    pickle.dump(serialization.book_entry,bin_file)
    print ('\n\033[1m{:s} file is serialzied successfully and wriiten in disk'.format(bin_file.name))


with open('book_entry.pickle', 'rb') as bin_file:
    book_entry = pickle.load(bin_file)
    print ('\n\033[1m original python data structure is {}'.format(book_entry))


#print (book_entry['published_date'])

#Examine pickle file
#Example 2:
#The most interesting piece of information in that disassembly is on the last line, because it includes the version of the pickle protocol with which this file was saved. There is no explicit version marker in the pickle protocol.

import pickletools

with open('book_entry.pickle', 'rb') as bin_file:
      pickletools.dis(bin_file)
