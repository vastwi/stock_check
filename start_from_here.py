from pprint import pprint
from alpha_vantage.timeseries import TimeSeries


def get_stock_symbols_for_text(search_text):
    data, metadata = ts.get_symbol_search(search_text)
    pprint(data[['1. symbol', '2. name', '8. currency']])
    option = input("Enter the company for which u want the info :")
    company = data.loc[int(option), ['1. symbol']].values
    get_final_quote(company)


def get_final_quote(company):
    data, meta_data = ts.get_quote_endpoint(company[0])
    print(data)


if __name__ == '__main__':
    ts = TimeSeries(key='A0IASAGQJJ1GUZDO', output_format='pandas', indexing_type='integer')
    # Get json object with the intraday data and another with  the call's metadata
    name = input("Enter the company name to search :")
    get_stock_symbols_for_text(name)
