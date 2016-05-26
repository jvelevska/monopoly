from setuptools import setup, find_packages

setup(
    name="Monopoly",
    version="0.1",
    packages=find_packages(),
    install_requires=['world>=1'],
    author="Janitsa Velevska",
    author_email="jvelevska@abv.bg",
    description="Monopoly in Python",
    license="GNU GENERAL PUBLIC LICENSE",
    keywords="monopoly game",
    url="https://github.com/jvelevska/monopoly"
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications :: Qt',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3),
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
