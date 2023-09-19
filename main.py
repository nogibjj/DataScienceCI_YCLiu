#import libraries
import pandas as pd
import lib

# Read dataset from a csv file
Dataset_raw = pd.read_csv('Dataset.csv')
print(Dataset_raw.head())
Dataset = Dataset_raw[(Dataset_raw['YEAR']>=1990)&(Dataset_raw['YEAR']<=2010)].copy()

# Define categorical Variable
def catSuicideRate(rate):
    if rate < 5:
        return 'low'
    elif rate < 15:
        return 'medium'
    else:
        return 'high'

Dataset['Suicide Rate Cat'] = Dataset['Suicide Rate'].apply(catSuicideRate)

# Summarize GDP per Capita and Suicide Rate data in France
Dataset_FRA = Dataset[Dataset['COUNTRY_REGION']=='FRA']
print("Descriptive Statistics for France from 1990 to 2010:")
print(lib.printNumStats(Dataset_FRA, 'GDP per Capita'))
print(lib.printNumStats(Dataset_FRA, 'Suicide Rate'))
print(lib.printOccStats(Dataset_FRA, 'Suicide Rate Cat', 'high'))
print(lib.printOccStats(Dataset_FRA, 'Suicide Rate Cat', 'medium'))
print(lib.printOccStats(Dataset_FRA, 'Suicide Rate Cat', 'low'))

Dataset_ALB = Dataset[Dataset['COUNTRY_REGION']=='ALB']
print("Descriptive Statistics for Albania from 1990 to 2010:")
print(lib.printNumStats(Dataset_ALB, 'GDP per Capita'))
print(lib.printNumStats(Dataset_ALB, 'Suicide Rate'))
print(lib.printOccStats(Dataset_ALB, 'Suicide Rate Cat', 'high'))
print(lib.printOccStats(Dataset_ALB, 'Suicide Rate Cat', 'medium'))
print(lib.printOccStats(Dataset_ALB, 'Suicide Rate Cat', 'low'))