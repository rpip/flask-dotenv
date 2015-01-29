"""
Flask-DotEnv
----------

The .env file support for Flask.
"""

from setuptools import setup


setup(
    name='Flask-DotEnv',
    version='0.0.1',
    url='https://github.com/grauwoelfchen/flask-dotenv/',
    license='BSD',
    author='Yasuhiro Asaka',
    author_email='grauwoelfchen@gmail.com',
    description='The .env file support for Flask',
    long_description=__doc__,
    py_modules=['flask_dotenv'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'python-dotenv'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)