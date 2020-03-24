import setuptools

setuptools.setup(
    name="Emmental-API-centralesupelec",
    version="0.1",
    author="Emmental CS student group",
    author_email="theo.bonnard@supelec.fr",
    description="API of a platform for self-learning cybersecurity stuff",
    url="https://gitlab.centralesupelec.fr/cs-emmental/platform/tree/master/back",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
