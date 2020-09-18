import os
import sys


def create_dirs(project_path: str) -> int:

    """ Creating main dirs for every python project """
    dirs = ['docs',
            'module',
            'tests'
            ]

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
    files = ['docs/conf.py',
             'docs/index.rst',
             'module/__init__.py',
             'module/core.py',
             'tests/core.py',
             'LICENCE',
             'README.rst',
             'requirments.txt',
             'setup.py'
             ]

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
    project_path = sys.argv[1]
    print(project_path)

    create_template(project_path)
