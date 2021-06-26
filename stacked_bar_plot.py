# Ploat the fourth problem...
import csv
from plotutils import stacked_bar_graph


def yearwise_business_name_store():
    '''
    Extract csvfile and set  yearwise business name store in stack_dic
    dictionary
    '''
    with open('mca_maharashtra.csv', encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        stack_dic = {}
        for row in csv_reader:
            if '2000' < row[6][-4:] <= '2010':
                stack_dic[row[6][-4:]] = stack_dic.get(row[6][-4:], {})
                if (row[11] == "Business Services" or
                        row[11] == "Community, personal & Social Services" or
                        row[11] == "Finance" or
                        row[11] == "Trading" or
                        row[11] == "Manufacturing (Food stuffs)"):
                    if row[11] in stack_dic[row[6][-4:]]:
                        stack_dic[row[6][-4:]][row[11]] += 1
                    else:
                        stack_dic[row[6][-4:]][row[11]] = 1

        return stack_dic


def sort_by_year_store_businessname_list(stack_dic):
    '''
    sort and store data in dictionary
    '''

    stack_result = {}
    year = []
    business_services = []
    community_services = []
    finance = []
    food_manufacturing = []
    trading = []

    for i in sorted(stack_dic.keys()):
        year.append(i)
        business_services.append(stack_dic[i]["Business Services"])
        community_services.append(
            stack_dic[i]["Community, personal & Social Services"])
        finance.append(stack_dic[i]["Finance"])
        food_manufacturing.append(
            stack_dic[i]["Manufacturing (Food stuffs)"])
        trading.append(stack_dic[i]["Trading"])

    stack_result["year"] = year
    stack_result["business_services"] = business_services
    stack_result["community_services"] = community_services
    stack_result["finance"] = finance
    stack_result["food_manufacturing"] = food_manufacturing
    stack_result["trading"] = trading
    return stack_result


if __name__ == "__main__":
    stack_dic = yearwise_business_name_store()
    stack_result = sort_by_year_store_businessname_list(stack_dic)
    stacked_bar_graph(
        stack_result,
        'Number of Companies',
        'Total Companies',
        'Principal Business Activities in Maharashtra from 2001 to 2010')
