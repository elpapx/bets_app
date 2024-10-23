from distributed.utils_test import requires_ipv6
from setup import HYPEN_E_DOT
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT
def get_requirements(file_path:str) ->List[str]:
    """
    this function will return the list of requiremrnts
    :param file_path:
    :return:
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements =  file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = 'ml_bets_beta',
    version = '0.1.0',
    packages = find_packages(),
    author = 'pcamacho447',
    install_requires = get_requirements('requirements.txt'),
)