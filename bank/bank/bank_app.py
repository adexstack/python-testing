from flask import Flask, render_template, request
from bank.bank.bank import Bank
from bank.bank.account import Account

app = Flask(__name__)
BANK = Bank()


@app.route('/')
def hello_world():
    account_number = request.args.get('account_number')
    balance = BANK.get_account_balance(account_number)
    return render_template('index.html', balance=balance)


def main():
    account = Account('1111', 50)  # pylint: disable=C0103
    Bank.add_account(account)
    app.run(debug=True)


if __name__ == '__main__':
    main()
