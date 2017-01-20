import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='qgprofiler',
    version='0.1.9',
    description='Profiler with time deterministic profiling of functions',
    url='https://github.com/quantumgraph/qgprofiler',
    author='QuantumGraph',
    author_email='contact@quantumgraph.com',
    license='MIT',
    packages=['qgprofiler'],
    long_description=read('README.md'),
    keywords = ['profiler', 'monitoring', 'logging', 'utility'],
    zip_safe=False,
    include_package_data=True
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'License :: Freeware',
        'Programming Language :: Python',
    ],
)
