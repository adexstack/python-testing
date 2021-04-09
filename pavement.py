from paver.tasks import task, BuildFailure
from paver.easy import sh, needs


@task
def unit_tests():
    sh('python -m pytest --cov=bank/bank bank/test/unit')


@task
def py_tests():
    sh('pytest bank/test/bdd')


@task
def run_pylint():
    try:
        sh('pylint --msg-template="{path}:{line}:{{msg_id}({symbol}), {obj}] {msg}" bank/ > pylint.txt')
    except BuildFailure:
        pass


#@needs('unit_tests', 'py_tests', 'run_pylint')
@needs('unit_tests')
@task
def default():
    pass



