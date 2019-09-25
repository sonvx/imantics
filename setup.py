from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open('imantics/version.py').read())

setup(
    name='imantics',
    version=__version__,
    description='Python package for managing image annotations',
    url='https://github.com/jsbroks/imantics',
    author='Justin Brooks',
    author_email='jsbroks@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    install_requires=['numpy', 'opencv-python>=3', 'lxml'],
    packages=['imantics'],
    python_requires='>=2.7',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        'Topic :: Multimedia :: Graphics :: Capture',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
