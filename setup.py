from setuptools import setup, find_packages

setup(
    name="django-jooy-reporting",
    version="0.0.1",
    author="Baris Bilgic",
    author_email="baris@jooysoft.com",
    description=("Ready-to-user basic django reports"),
    license="BSD",
    keywords="django report",
    url="",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        'django>=1.7',
        'djangorestframework>=3.0.2',
        "six"
    ]
)