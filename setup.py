import sys
from setuptools import setup, find_packages

setup_requires = [
    ]

install_requires = [
    # 'django==4.0',
    # 'markdown==3.1',
    'pyyaml==6.0',
    # 'pillow==9.1.1',
    # 'lxml==4.8.3',
    # 'beautifulsoup4==4.9.0',
    ]

tests_require = [
    'nose==1.3.7',
    'coverage==6.4.1',
]

if sys.version_info < (2,7):
    test_require.append('unittest2==0.5.1')

dependency_links = [
    ]

setup(
    name='aiffel-git',
    version='0.1.0a',
    license='MIT',
    description='easy git push system',
    long_description=open('README.md').read(),
    author='hchang',
    author_email='cake0103@nate.com',
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    scripts=['manage.py'],
    entry_points={
        'console_scripts': [
            'publish = bin:main',
            'scan = bin:main',
            'update = bin:main',
            ],
        },
    extras_require={
        'test': tests_require,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
    )