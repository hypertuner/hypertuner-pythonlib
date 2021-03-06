import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hypertuner",
    version="0.0.1",
    author="Klemen Kotar, Dian Niu",
    author_email="klemen@cs.washington.edu, dian.niu.11@gmail.com",
    description="A library for passing arguments and graphing with HyperTuner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hypertuner/hypertuner-pythonlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'torch>=1.0.0',
    ]
)
