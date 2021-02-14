from setuptools import setup


setup(
    name='Flask-Bismillah',
    version='1.0',
    url='http://example.com/flask-sqlite3/',
    license='Apache 2.0',
    author='Touhid Mia',
    author_email='hmtmcse.com@gmail.com',
    description='This is example Flask Extension',
    long_description=__doc__,
    py_modules=['flask_sqlite3'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)