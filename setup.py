import setuptools

import hippocrates

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='hippocrates',
    version=hippocrates.__version__,
    author='Chris Hannam',
    author_email='ch@chrishannam.co.uk',
    description='Mental health questionnaires.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chrishannam/hippocrates',
    packages=setuptools.find_packages(exclude=('tests', 'examples')),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    install_requires=['click==7.0', 'pick>=0.6.4', 'tabulate>=0.8.2'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'hippocrates=hippocrates.command_line:main',
            'hippocrates-results=hippocrates.results:main',
        ]
    },
)
