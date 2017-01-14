from setuptools import setup

setup(name='alkahest',
      version='0.0.1',
      author='Kevin Batema',
      author_email='kevinbatema@gmail.com',
      packages=[
          'alkahest',
          'alkahest.blueprints',
      ],
      install_requires=[
          'Flask>=0.10.1',
          'SQLAlchemy=>1.1.4'
      ])
