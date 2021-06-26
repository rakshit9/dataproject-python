# Plot the second problem....
import csv
from plotutils import horizontal_bar_graph


def company_register_data():
    '''
    Extract csvfile and set company register data in dictionary
    '''

    with open('mca_maharashtra.csv', encoding='latin-1') as csv_file:
        company_data = {}
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            year = row[6][-4:]
            company_data[year] = company_data.get(year, 0) + 1
    return company_data


def sort_company_data(company_data):
    '''
    Sort comapany data
    '''

    year = []
    no_of_company = []

    for data in sorted(company_data.keys()):
        no_of_company.append(company_data[data])
        year.append(data)
    company_register = dict(zip(year[109:119], no_of_company[109:119]))
    return company_register


if __name__ == "__main__":
    company_data = company_register_data()
    company_register = sort_company_data(company_data)
    horizontal_bar_graph(
        company_register,
        "Date of Registration",
        "Number of Companies",
        "Company Registration in Maharashtra From 2009 to 2018")
