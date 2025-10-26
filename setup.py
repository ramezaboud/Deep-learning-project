from setuptools import find_packages, setup

def get_requriments(file_path: str) -> list[str]:
    requirments = []
    with open(file_path) as file:
        requirments = file.readlines()
    requirments = [req.replace("\n", "") for req in requirments]
    if "-e ." in requirments:
        requirments.remove("-e .")
    return requirments


setup(
name="Xray" ,
version = "0.0.1",
author = "Ramez Fawzy",
author_email= "ramezaboud248@gmail.com",
install_requires=get_requriments(),
packages=find_packages()

)