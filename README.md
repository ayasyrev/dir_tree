# dir_tree
> print directory tree


Similar as tree in terminal.

## Install

`pip install dir-tree`

## How to use

Import tree function:

```python
from dir_tree.dir_tree import tree
```

```python
tree('test_dir')
```

     test_dir  - 3 dirs 0 files
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

`Path.tree = tree'

Now we can use it as:

`path.tree()`

And better, if you use fastcore, you can patch it using @patch decorator.  
I didnt use it becouse won't use any dependences.

Now it has only base functionality.  
In plans: ipywidgets and cl functionalitys.
