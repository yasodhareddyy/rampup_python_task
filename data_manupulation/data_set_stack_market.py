import csv

def read_stock_data(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            parts = row['Date'].split('-')
            if len(parts) == 3:
                year, month, _ = map(int, parts)
                key = (year, month, row['Company'])
                data[key] = data.get(key, []) + [float(row['Closing Price'])]

    for (year, month, company), prices in data.items():
        yield year, month, company, sum(prices) / len(prices)

# Usage
filename = 'stock_market_data.csv'
for year, month, company, avg_price in read_stock_data(filename):
    print(f"Year: {year}, Month: {month}, Company: {company}, Average Closing Price: {avg_price:.2f}")










# import csv
#
# def read_stock_data(filename):
#     data = {}
#     with open(filename, 'r') as file:
#         reader = csv.DictReader(file)
#
#         for row in reader:
#
#             parts = row['Date'].split('-')
#             if len(parts) == 3:
#                 year, month, _ = map(int, parts)
#
#                 key = (year, month, row['Company'])
#
#                 data[key] = data.get(key, []) + [float(row['Closing Price'])]
#
#
#     for (year, month, company), prices in data.items():
#         yield year, month, company, sum(prices) / len(prices)
# #
# # # Usage+
# filename = 'stock_market_data.csv'
# obj=read_stock_data(filename)
# for year, month, company, avg_price in obj:
#     print(f"Year: {year}, Month: {month}, Company: {company}, Average Closing Price: {avg_price:.2f}")
#
#
# # for year, month, company, avg_price in read_stock_data(filename):
# #     print(f"Year: {year}, Month: {month}, Company: {company}, Average Closing Price: {avg_price:.2f}")
