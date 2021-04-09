from paver.tasks import task, BuildFailure
from paver.easy import sh, needs

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


@needs('unit_tests', 'py_tests', 'run_pylint')
#@needs('unit_tests')
@task
def default():
    pass



