# Dir_tree

> print directory tree

Similar as tree in terminal.

## Install

`pip install dir-tree`

## How to use

Import tree function:


```python
from dir_tree import tree
```


```python
tree('test_dir')
```
???+ done "output"  
    <pre> test_dir  - 3 dirs 0 files
         sub_dir_1  - 4 dirs 0 files
             sub_dir_1_1  - 0 dirs 0 files
             sub_dir_1_2  - 0 dirs 0 files
             sub_dir_1_3  - 0 dirs 0 files
             sub_dir_1_4  - 0 dirs 0 files
         sub_dir_2  - 5 dirs 0 files
             sub_dir_2_1  - 0 dirs 0 files
             sub_dir_2_2  - 0 dirs 0 files
             sub_dir_2_3  - 0 dirs 0 files
             sub_dir_2_4  - 0 dirs 0 files
             sub_dir_2_5  - 0 dirs 0 files
         sub_dir_3  - 6 dirs 0 files
             sub_dir_3_1  - 0 dirs 0 files
             sub_dir_3_2  - 0 dirs 0 files
             sub_dir_3_3  - 0 dirs 0 files
             sub_dir_3_4  - 0 dirs 0 files
             sub_dir_3_5  - 0 dirs 0 files
             sub_dir_3_6  - 0 dirs 0 files


You can sent string or Path object to tree function.


```python
from pathlib import Path
```


```python
path = Path('test_dir')
```

Now we can use path: 

`tree(path)`

And we can 'patch' Path as:  

`Path.tree = tree`

Now we can use it as:

`path.tree()`

If you want look to files content, use `print_files=True` argument.  
It print filenames, limited to `num_files` quantity.

In terminal it can be used as dir_tree command.   

It uses only standart library.

Now it has only base functionality.  
