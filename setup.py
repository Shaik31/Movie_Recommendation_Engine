'''from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    #this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="Movie Recommendation Engine",
    version=1.0,
    author="Shaik Abdul Khadar",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)'''

from setuptools import setup, find_packages

setup(
    name='movie_recommendation_engine',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'scikit-learn>=0.24.0',
        'streamlit>=0.87.0',
        'pickle>=4.0'
        # Add other dependencies here
    ],
)

