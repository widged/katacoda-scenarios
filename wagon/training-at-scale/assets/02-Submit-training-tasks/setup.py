from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'gcsfs==0.6.0',
    'google-cloud-storage==1.26.0',
    'pandas==0.24.2',
    'scipy==1.2.2',
    'scikit-learn==0.20.4',
    'joblib']

setup(name='TaxiFareModel',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Taxi Fare Prediction Pipeline')
