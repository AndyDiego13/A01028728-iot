import csv
import pandas as pd
import ast

#with open("TextFiles/populationbycountry19802010millions.csv") as csvFile:
    #reader = csv.reader(csvFile)

    #for row in reader:
         #print(row)
def pandas(filepath, names):
     df = pd.read_csv(filepath, names = names)
     df.fillnan(0)
     return df



if __name__ == "__main__":
     filepath = "TextFiles/populationbycountry19802010millions.csv"
     names = ['country_or_area', 'year', 'value', 'category']
     df = pandas(filepath,names)
     #null_columns = df.columns[df.isnull().any()]
     #df[null_columns].isnull().sum()
     #print(df[df.isnull().any(axis=1)][null_values].head())
     #df_sin_nan = df.dropna(how = 'all')

     #df2 = df.head(10)
     df_filtered = df[df['value']].fillnan(0)
     print(df_filtered['value'].mean())

     #df['ca'+'ct'] = df['country_or_area'] + df['year']
     #print(df)

     #df_filtered = df['year']
     #print(df_filtered)

    #reader = csv.DictReader(csvFile)
    
    #print(reader.fieldnames)


    