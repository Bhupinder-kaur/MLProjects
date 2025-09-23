from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This def function will return the list of Requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
name='MLPROJECTS',
version='0.01',
author='Bhupinder Kaur',
author_email='bhupinderkaur027@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
