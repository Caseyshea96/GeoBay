from setuptools import setup, find_packages

setup(
    name="geobay",
    version="1.0.0",
    description="A package for Geography",
    author="Casey Shea",
    author_email="shea96@gmail.com",
    packages=find_packages(),  # Automatically find packages in your directory
    install_requires=[],  # Add your dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
