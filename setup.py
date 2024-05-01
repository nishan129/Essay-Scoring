from setuptools import setup, find_packages
from typing import List,Any

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()



def get_requiremnts() -> List[str]:
    
    requirements_list: List[str] = []
    
    return requirements_list



setup(
    name= "Essay-scoring",
    version='0.0.0.0',
    author="Nishant Borkar",
    author_email="nishantborkar139@gmail.com",
    long_description= long_description,
    description="Automated Essay Scoring (AES) ",
    packages=find_packages(),
    install_requires=get_requiremnts()
)