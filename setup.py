from setuptools import find_packages, setup
def get_requirements(file_path:str)-> list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[ req.replace('\n',"") for req in requirements ]
    return requirements

setup(
    name="vivek",
    version="0.0.1",
    author="vivek",
    author_email="viveksharma7497@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
