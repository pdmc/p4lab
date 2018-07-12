from setuptools import setup

setup(
    name='P4Lab',
    version='0.1.0',
    long_description=__doc__,
    packages=['p4lab'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)