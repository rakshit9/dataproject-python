# Company Master :: Maharashtra

## Aim
To convert raw open data into plots, that tell a story on the state of company registration in Maharashtra.

## How to get the data
* The dataset can be downloaded from [link](https://data.gov.in/resources/company-master-data-maharashtra-upto-21st-april-2018)
* Download file change file name run `mv mca_maharashtra_21042018.csv mca_maharashtra.csv`

## Requirements
All the requirements and dependencies store in **requirements.txt** and install all requirements and dependencies run `pip3 install -r requirements.txt`

## How to run project
### 1.Authorized Capital plot a bar chart

* Plot the graph of authorized capital of different companies according to capital.
* Run command `python authorized_cap.py` in the repository folder which generate plot graph.

### 2.Bar Plot of company registration by year

* From the column, DATE_OF_REGISTRATION parse out the registration year. Using this data, plot a bar plot of the number of company registrations, vs. year.
* Run command `python company_register_by_year.py` in the repository folder which generate plot graph.

### 3.Top registrations by "Principal Business Activity" for the year 2015

* Plot the graph of top 10 principal business activities company in Maharashtra.
* Run command `python business_activity.py` in the repository folder which generate plot graph.

### 4.Grouped Bar Plot
* Plot the graph of Year of registration and 5 Principal business activity.
* Run command `python stacked_bar_plot.py` in the repository folder which generate plot graph.