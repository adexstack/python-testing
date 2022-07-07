from flask import Flask, render_template, request
from account import Account
from bank.bank.bank import Bank

app = Flask(__name__)
bank = Bank()

@app.route('/')
def hello_world():
    account_number = request.args.get('account_number')
    balance = bank.get_account_balance(account_number)
    return render_template('index.html', balance=balance)


if __name__ == '__main__':
    import cProfile

    account = Account('1111', 50)
    bank.add_account(account)
    cProfile.run('appunittest.run(debug=True)')
