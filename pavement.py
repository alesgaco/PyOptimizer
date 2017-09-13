from paver.easy import *
import paver.doctools
from paver.setuputils import setup
setup(
    name='PyOptimizer',
    version='1.0',
    packages=['PyOptimizer'],
    url='https://github.com/alesgaco/PyOptimizer',
    license='MIT',
    author='Aldo Esteban Garces Correa',
    author_email='aegarcesc@unal.edu.co',
    description='No linear optimizer focused on heuristic methods',
    sphinx = Bunch(
    builddir="_build"
    )
)
