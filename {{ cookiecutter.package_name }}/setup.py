#
# Copyright (c) {{ cookiecutter.year }}, {{ cookiecutter.author_name }}
#

from setuptools import setup, find_packages


setup(
    name='{{ cookiecutter.package_name }}',
    version='0.1.0',
    description='',
    long_description=open('README.rst', 'r').read(),
    keywords='',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    url='https://github.com/{{ cookiecutter.author_github }}/{{ cookiecutter.package_name }}',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=True,
    include_package_data=True,
    install_requires=[
    ],
)

