from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
#function to extract the packages which are required for the project
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of the requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("/n","")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements





setup (
 name='mlproject',
    version='0.0.1',
    author='sundar',
    author_email='sunc91@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)