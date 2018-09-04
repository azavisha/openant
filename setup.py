from setuptools import setup, find_packages

setup(name='openant',
      packages=find_packages(),
      install_requires=['pyserial', 'pyusb']
      )
