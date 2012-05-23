from setuptools import setup, find_packages

setup(
    name='chunks',
    version='0.1',

    description='Encode and decode http chunked encoding.',
    author="Simon Engledew",
    author_email="simon@engledew.com",
    url="http://www.engledew.com",

    install_requires = [
    ],
    zip_safe=True,
    include_package_data=False,
    packages=find_packages(),
    license='MIT',
    keywords = [
        'chunked',
        'http',
        'chunks',
        'encoding',
        'decode'
    ],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
