# -*- coding: UTF-8 -*-
from setuptools import setup


setup(
    name='Flask-APIForm',
    version='1.0',
    url='https://github.com/mayconbordin/flask-apiform/',
    license='BSD',
    author='Maycon Bordin',
    author_email='mayconbordin@gmail.com',
    description='A simple form validator for REST APIs in Flask',
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
