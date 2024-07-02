from setuptools import setup

setup(
    name='Test',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='Anjali Goel',
    author_email='arg8qqv@virginia.edu',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)