import serialization
import json

with open('book_entry.json','w') as json_file:
    json.dump(serialization.book_entry,json_file,indent=4)
    print ('\n\033[1m{:s} file is serialized successfully and wriiten in disk'.format(json_file.name))

with open('book_entry.json', 'r') as json_file:
    book_entry = json.load(json_file)
    print ('\n\033[1m original python data structure is {}'.format(book_entry))



