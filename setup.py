from setuptools import setup, find_packages
from typing import List

HYPHEN='-e .'
def get_requirements(file_path:str)->List[str]:
    '''this function will return list of requirements'''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n', ' ') for req in requirements]
        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
    return requirements


setup(
    name='ml_package',
    version='0.01',
    author='Prshotm',
    author_email='prshotm7694@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)