import os
from setuptools import setup

import codecs


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname),encoding="utf-8").read()


setup(name='botflow',
      description='Data-driven and Reactive  programming framework'
                  ' ',
      long_description=read("README.rst"),
      version='0.1.9',
      url='https://github.com/kkyx/botflow',
      author='Guojian Li',
      author_email='guojianlee@gmail.com',
      license='BSD',
      python_requires=">=3.6.5",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3'
      ],
      packages=['databot', 'databot.db', 'databot.http'],
      install_requires=[
          'aiohttp>=3.3.0',
          'aiomysql>=0.0.19',
          'graphviz'

      ],

      )
