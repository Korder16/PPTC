import os
import sys


def is_dir_empty(path: str) -> bool:

    """ Checks if dir is empty """
    if len(os.listdir(path)) == 0:
        return True
    else:
        return False


def create_dirs(project_path: str) -> int:

    """ Creating main dirs for every python project """
    dirs = frozenset(
            {
                'docs',
                'module',
                'tests'
                }
            )

    for dir in dirs:
        try:
            os.mkdir(dir)
        except OSError:
            print(f'Cannot create dir: {dir}.')
        else:
            print(f'Successfully created dir: {dir}.')

    return 0


def create_files(project_path: str) -> int:

    """ Creating main files for every python project """
    files = frozenset(
            {
                'docs/conf.py',
                'docs/index.rst',
                'module/__init__.py',
                'module/core.py',
                'tests/core.py',
                'LICENCE',
                'README.rst',
                'requirments.txt',
                'setup.py'
                }
            )

    for file in files:
        try:
            f = open(file, 'w')
            f.close()
        except OSError:
            print(f'Cannot create file: {file}.')
        else:
            print(f'Successfully created file: {file}.')

    return 0


def create_template(project_path: str) -> int:

    """ Creaing whole project template """
    os.chdir(project_path)
    create_dirs(project_path)
    create_files(project_path)

    return 0


if __name__ == '__main__':

    # Read console argument (directory), where script should create a template
    project_path = sys.argv[1]
    print(project_path)

    if is_dir_empty(project_path):
        create_template(project_path)
    # If dir is not empty, do not create a template
    else:
        print(f'Directory: {project_path} is not empty')
