from pathlib import Path

from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

entry_points = {
    'console_scripts': [
        'partnertools-cli = partner_tools.cli.cli:main'
    ]
}

install_requires = [
    "click>=8.0,<8.1",
    "questionary==1.10.0",
    "requests==2.27.1",
    "azure-identity>=1.8.0",
    "pydantic==1.10.2"
]

setup(
    name='ms-partner-tools',
    version='0.0.2',
    author='TechStorm PC',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Intended Audience :: Information Technology",
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    author_email='nathan@techstormpc.com',
    description='SDK for interacting with the Microsoft Partner Center',
    packages=find_packages(include=['partner_tools*']),
    install_requires=install_requires,
    url='https://github.com/techstormpc/ms-partner-tools',
    entry_points=entry_points,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
