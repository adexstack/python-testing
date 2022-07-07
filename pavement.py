from paver.tasks import task, BuildFailure
from paver.easy import sh, needs
from paver.setuputils import setup, find_package_data

package_data = find_package_data()
entry_points = {
    'console_scripts': [
        'run_server = bank.bank.bank_app:main'
    ]
}

setup(name='bank_app',
      version='0.0.1',
      author='Seyi Adex',
      maintainer='Seyi Adex',
      description='Application for Python Testing Techniques',
      licence='Licence :: Public Domain',
      include_package_data=True,
      packages=['bank'],
      package_data=package_data,
      entry_points=entry_points)

@task
@needs('paver.misctasks.generate_setup',
       'distutils.command.sdist')
def sdist():
    """
    Generates the setup file and packages up the commercial_inventory application.
    """

# I am adding python -m for code execution in Jenkins (External server).
# Not needed in running directly here on linux venv35
#--cov=bank/bank
@task
def unit_tests():
    sh('python -m pytest --cov-report xml:coverage.xml --cov=bank bank/test/')


@task
def py_tests():
    sh('python -m behave bank/test/bdd')


@task
def run_pylint():
    try:
        sh('python -m pylint --msg-template="{path}:{line}:[{msg_id}({symbol}), {obj}] {msg}" bank/ > pylint.txt')
    except BuildFailure:
        pass


@needs('unit_tests', 'py_tests', 'run_pylint', 'sdist')
#@needs('unit_tests')
@task
def default():
    pass



