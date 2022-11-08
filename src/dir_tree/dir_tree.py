import os
from pathlib import Path
from typing import List, Union


__all__ = ["create_sub_dirs", "create_test_dir", "get_dirs_files", "tree"]


def create_sub_dirs(
    path: Path,
    num_sub_dirs: int,
    sub_dir_name: str = "sub_dir",
    levels: int = 1,
) -> None:
    for i in range(num_sub_dirs):
        sub_dir = path / (sub_dir_name + f"_{i + 1}")
        sub_dir.mkdir(exist_ok=True)
        if levels:
            create_sub_dirs(sub_dir, i + 1 + num_sub_dirs, sub_dir.name, levels - 1)


def create_test_dir(
    path: Union[str, Path] = "test_dir",
    num_sub_dirs: int = 3,
    sub_dir_name: str = "sub_dir",
    levels: int = 1,
) -> None:
    path = Path(path)
    path.mkdir(exist_ok=True)
    create_sub_dirs(path, num_sub_dirs, sub_dir_name, levels)


def get_dirs_files(path: Union[str, Path]) -> tuple[List[Path], List[Path]]:
    """Return tuple of lists -> directories and files"""
    res = {True: [], False: []}
    for dir_entry in os.scandir(Path(path)):
        res[dir_entry.is_dir()].append(Path(dir_entry))
    return sorted(res[True]), sorted(res[False])


def tree(
    path: Union[str, Path] = ".",
    ident: int = 0,
    print_files: bool = False,
    num_files: int = 3,
) -> None:
    """Print dir tree. Input - str or Path-like obj.
    If print_files is True, print files, limited to num_files."""
    path = Path(path)
    dirs, files = get_dirs_files(path)
    print(" " * ident, f"{path.name}  - {len(dirs)} dirs {len(files)} files")
    for dir_entry in dirs:
        tree(Path(dir_entry), ident + 4, print_files, num_files)
    if print_files:
        len_files = len(files)
        for dir_entry in files[:num_files]:
            print(" " * (ident + 4), "-", dir_entry.name)
        if len_files > num_files and len_files != 0:
            print(
                " " * (ident + 4),
                "--",
                f"{len_files - num_files} more files in this dir",
            )
