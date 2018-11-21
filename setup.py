import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='hippocrates',
    version='0.1.1',
    author='Chris Hannam',
    author_email='ch@chrishannam.co.uk',
    description='Mental health questionnaires.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chrishannam/hippocrates',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pick>=0.6.4',
    ],
)
