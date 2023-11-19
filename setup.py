from setuptools import setup, find_packages

setup(
    name='metabolitics3d',
    version='0.0.12',
    packages=find_packages(),
    description='metabolitics3d',
    author="Onurcan Ersen",
    author_email="ocersen@gmail.com",
    url="https://github.com/onurcanersen/metabolitics3d",
    install_requires=[
        'numpy>=1.8.2',
        'pyfunctional>=1.0.0',
        'pandas>=0.17.0',
        'scipy>=0.13.3',
        'scikit-learn>=0.18.0',
        'cobra>=0.9.1',
        'joblib>=0.11',
        'sklearn_utils>=0.0.15',
    ],
    include_package_data=True,
    test_suite='metabolitics3d.tests',
    keywords=['bioinformatics', 'metabolomics', 'pip-package'],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ])
