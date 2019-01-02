import setuptools

setuptools.setup(
    name='test_proj',
    version='1.0.0',
    description='test',
    author='noone',
    author_email='noone@where.co.uk',
    license='Copyright 2016. All rights reserved.',
    url='https://github.com/bbcrgoliveira/test_proj',
    packages=setuptools.find_packages(),
    install_requires=[],
    dependency_links=[],
    scripts=[],
    setup_requires=['nose>=1.0'],
    tests_require=['nose'],
    test_suite='tests',
)
