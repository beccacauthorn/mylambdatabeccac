# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="mylambdatabeccac",
    version="1.0",
    author="Becca Cauthorn",
    author_email="beccacauthorn@gmail.com",
    description="For learning purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/beccacauthorn/mylambdatabeccac",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)