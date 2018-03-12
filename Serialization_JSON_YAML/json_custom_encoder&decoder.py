import simplejson
import serialization

def _to_json(python_object) :
    if isinstance(python_object, tuple) :
        python_object = {'__class__': 'tuple',
                         '__value__': list(python_object)}
    else :
        raise TypeError(repr(python_object) + ' is not JSON serializable')

    return python_object

def _from_json(json_object):
    if isinstance(json_object,dict):
        if '__class__' in json_object.keys():
             if json_object['__class__'] == 'tuple':
               return tuple(json_object['__value__'])
    else:
        print (json_object,'no dict')
    return json_object


json_out = simplejson.dumps((serialization.book_entry),
                       default=_to_json,
                       tuple_as_array=False,indent=4)
print (json_out)
tuple_out = simplejson.loads(json_out, object_hook=_from_json)

print (tuple_out)

with open('encode_book_entry.json','w') as file:
    simplejson.dump(serialization.book_entry,file,default=_to_json,tuple_as_array=False,indent=4)
    print('\n\033[1m{:s} file is serialized successfully and wriiten in disk using Custom Encoder'.format(file.name))

with open('encode_book_entry.json','r') as file:
    py_tuple=simplejson.load(file, object_hook=_from_json)
    print('\n\033[1m original python data structure is {}'.format(py_tuple))
