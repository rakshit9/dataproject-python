# Plot the chart ...
import matplotlib.pyplot as plt
import numpy as np


def horizontal_bar_graph(dict_name, x_label, y_label, title):
    '''
    Ploting graph
    '''

    names = dict_name.keys()
    values = dict_name.values()
    fig, axs = plt.subplots(figsize=(6, 4))
    axs.bar(names,
            values,
            color='#607c8e',
            width=0.30)
    axs.set_title(title,
                  color="#607c8e")
    axs.tick_params(labelcolor='#607c8e', labelsize='medium', width=1)
    axs.spines['top'].set_color('#607c8e')
    axs.spines['bottom'].set_color('#607c8e')
    axs.spines['left'].set_color('#607c8e')
    axs.spines['right'].set_color('#607c8e')
    axs.tick_params(axis='x', colors='#607c8e')
    axs.tick_params(axis='y', colors='#607c8e')
    axs.xaxis.label.set_color('#607c8e')
    axs.yaxis.label.set_color('#607c8e')

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.show()


def veritcal_bar_graph(dict_name, x_label, y_label, title):
    '''
    Ploting graph
    '''

    names = list(dict_name.keys())
    values = list(dict_name.values())

    fig, axs = plt.subplots(figsize=(8, 4))
    fig.subplots_adjust(left=0.4)
    axs.barh(names,
             values,
             color="#607c8e")
    axs.set_title(title,
                  color="#607c8e")
    axs.tick_params(labelcolor='#607c8e', labelsize='medium', width=1)
    axs.spines['top'].set_color('#607c8e')
    axs.spines['bottom'].set_color('#607c8e')
    axs.spines['left'].set_color('#607c8e')
    axs.spines['right'].set_color('#607c8e')
    axs.tick_params(axis='x', colors='#607c8e')
    axs.tick_params(axis='y', colors='#607c8e')
    axs.xaxis.label.set_color('#607c8e')
    axs.yaxis.label.set_color('#607c8e')

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=7)
    plt.show()


def stacked_bar_graph(stack_result, x_label, y_label, title):
    '''
    Ploting graph
    '''

    x = np.arange(len(stack_result["year"]))  # the label locations
    width = 0.18  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x,
           stack_result['business_services'],
           width,
           color="black",
           label='Business Services')
    ax.bar(x+width,
           stack_result['community_services'],
           width,
           color="yellow",
           label="Community,personal & Social Services")
    ax.bar(x+width*2,
           stack_result["finance"],
           width,
           color="red",
           label="Finance")
    ax.bar(x-width*2,
           stack_result['food_manufacturing'],
           width,
           color="blue",
           label="Manufacturing (Food stuffs)")

    ax.bar(x-width,
           stack_result['trading'],
           width,
           color="orange",
           label="Trading")
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(stack_result["year"])
    ax.legend()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
