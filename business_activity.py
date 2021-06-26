# # Plot the third problem, ....
import csv
from plotutils import veritcal_bar_graph


def business_activity_data():
    '''
     Extract csvfile and set business name data in dictionary
    '''

    with open('mca_maharashtra.csv', encoding='latin-1') as csv_file:
        business_name_data = {}
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            business_name_data[row[11]] = business_name_data.get(
                row[11], 0) + 1
    return business_name_data


def sort_business_name_data(business_name_data):
    '''
    Business name data
    [(), ()] -> [], [] => zip()
    '''

    number_of_company = {}
    result = sorted(business_name_data.items(),
                    key=lambda x: x[1],
                    reverse=True)
    name, count = zip(*result)
    number_of_company = dict(zip(name[:10], count[:10]))
    return number_of_company


if __name__ == "__main__":
    business_name_data = business_activity_data()
    number_of_company = sort_business_name_data(business_name_data)
    veritcal_bar_graph(
        number_of_company,
        'Number of Companies',
        'Business Activity Name',
        'Principal Business Activity in 2015')
