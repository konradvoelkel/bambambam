from setuptools import setup, find_packages

setup(
    name='bambambam',
    version = '0.5',
    install_requires=[
        "pygame",
    ],
    description='Teach toddlers human-computer interaction in a fun way',
    author='Konrad Voelkel',
    author_email='bambambam-at-konradvoelkel.com',
    license = 'public domain',
    url = 'http://www.github.com/konradvoelkel/bambambam',
    package_dir = {'': 'src'},
#    packages = ['bambambam'],
    packages = find_packages(),
    package_data = {
        'bambambam-data': ['data/*.*'],
        'bambambam-audio-letters': ['data/audio-letters/*.*'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: Public Domain',
        'Topic :: Games/Entertainment',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    use_2to3 = False,
)

#TODO could investigate how to package Gnome(=.desktop), Debian (.deb), OSX (???) and Windows (.exe) versions.
