from setuptools import setup
setup(
    name='tlib',
    version='0.0.1',
    description='A collection of some rather useless functions',
    url='git@github.com:TrevoR313/tlib.git',
    author='TrevoR',
    license='MIT',
    packages=['tlib'],
    install_requires=[
        'tqdm',
        'requests'
    ],
    zip_safe=False
)
