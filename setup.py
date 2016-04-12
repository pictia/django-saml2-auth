"""The setup module for django_saml2_auth.
See:
https://github.com/fangli/django_saml2_auth
"""

from codecs import open
from setuptools import (setup, find_packages)
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django_saml2_auth',

    version='1.0.2b1',

    description='Django SAML2 Authentication Made Easy, integrate with SAML2 SSO such as Okta easily',
    long_description=long_description,

    url='https://github.com/fangli/django-saml2-auth',

    author='Fang Li',
    author_email='surivlee+djsaml2auth@gmail.com',

    license='Apache 2.0',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='Django SAML2 Authentication Made Easy, integrate with SAML2 SSO such as Okta easily',

    packages=find_packages(),

    install_requires=['pysaml2==4.0.5'],
    include_package_data=True,
)