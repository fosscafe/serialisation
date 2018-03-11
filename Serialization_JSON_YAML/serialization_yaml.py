import serialization
import yaml


with open('en_book_entry.yaml','w') as yaml_file:
    yaml.dump(serialization.book_entry,yaml_file)
    print('\n\033[1m{:s} file is serialized successfully using YAML and wriiten in disk'.format(yaml_file.name))

with open('en_book_entry.yaml','r') as yaml_file:
    py_object = yaml.load(yaml_file)
    print('\n\033[1m original python data structure is {}'.format(py_object))