
import yaml


with open('yaml_example2','r') as yaml1_file:
      py_object=list(yaml.safe_load_all(yaml1_file))
      print('\n\033[1m original python data structure is {}'.format(py_object))