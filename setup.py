from setuptools import setup, find_packages

setup_requires = [
    ]

install_requires = [
    'django==4.0',
    'markdown==3.1',
    'pyyaml==6.0',
    'pillow==9.1.1',
    'lxml==4.8.3',
    'beautifulsoup4==4.9.0',
    ]

dependency_links = [
    'git+https://github.com/django/django.git@stable/1.6.x#egg=Django-1.6b4',
    ]

setup(
    name='Flowdas-Books',
    version='0.5.0',
    description='Flowdas Books',
    author='Flowdas',
    author_email='spammustdie@flowdas.com',
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    scripts=['manage.py'],
    entry_points={
        'console_scripts': [
            'publish = flowdas.books.script:main',
            'scan = flowdas.books.script:main',
            'update = flowdas.books.script:main',
            ],
        },
    )