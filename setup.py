from setuptools import setup

with open("README.txt") as f:
    long_description = f.read()

setup(
    name='ChessCalc',
    version='0.0.1',
    long_description=long_description,
    description='Tournament and league chess manager.',
    license="MIT",
    author='Greg Denyes',
    author_email='Greg.Denyes@gmail.com',
    packages=['ChessCalc'],
    install_requires=[
            'tkinter',
            'sqlite3',
            ],
    package_data=['chess.db'],
    classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: MIT License',
            'Operating System :: Win',
            ]



    )
