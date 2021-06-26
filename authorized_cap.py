# Plot the first problem, ....
import csv
from plotutils import horizontal_bar_graph

# TODO:
# 1. Comment all functions with docstring
# 2. Try to make code pythonic
# 3. Make authoried_cap as dict
# 4. Implement DRY functions


def auth_data():
    '''
    Extract csvfile and set authorized capital data
    '''

    with open('mca_maharashtra.csv', encoding='latin-1') as csv_file:
        authoried_cap = {'<=1L': 0,
                         '1L to 10L': 0,
                         '10L to 1Cr': 0,
                         '1Cr to 10 Cr': 0,
                         '>10Cr': 0}

        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if float(row[8]) <= 100000:
                authoried_cap['<=1L'] = authoried_cap.get('<=1L', 0) + 1
            elif 100000 < float(row[8]) <= 1000000:
                authoried_cap['1L to 10L'] = authoried_cap.get(
                    '1L to 10L', 0) + 1
            elif 1000000 < float(row[8]) <= 10000000:
                authoried_cap['10L to 1Cr'] = authoried_cap.get(
                    '10L to 1Cr', 0) + 1
            elif 10000000 < float(row[8]) <= 100000000:
                authoried_cap['1Cr to 10 Cr'] = authoried_cap.get(
                    '1Cr to 10 Cr', 0) + 1
            else:
                authoried_cap['>10Cr'] = authoried_cap.get(
                    '>10Cr', 0) + 1
    return authoried_cap


if __name__ == "__main__":
    authoried_cap = auth_data()
    horizontal_bar_graph(authoried_cap,
                         "Capitals",
                         "Number of Companies",
                         "Authorized Capital in Maharashtra")
