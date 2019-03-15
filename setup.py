import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Module name
    name="ppipinstall",
 
    #Module version
    version="0.0.1",
 
    #Name of Author
    author="Aniket Mishra",
 
    #Author's email address
    author_email="mishra1997aniket@gmail.com",
 
    #Small Description about module
    description="Package Installer",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 

    #link to reach this module, i.e. any webpage or github profile

    url="https://github.com/codezoned/pipinstall",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
