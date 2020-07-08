from flask import Blueprint, render_template, request, redirect, url_for
from models.stock import Stock

stocks_blueprint = Blueprint('stocks', __name__)


@stocks_blueprint.route('/index', methods=['GET', 'POST'])
def index():
    stocks = Stock.get_all_stocks()
    total = Stock.get_total()
    return render_template('stocks/index.html', stocks=stocks, Stock=Stock, total=total)


@stocks_blueprint.route('/form', methods=['POST'])
def form():
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        num_of_shares = request.form['num_of_shares']
        purchase_price = request.form['purchase_price']
        Stock(stock_symbol, num_of_shares, purchase_price).save_to_mongo()
        return redirect(url_for('stocks.index'))