def square( x ):
    return x ** 2

result_type_int  = square( 3 )
print( result_type_int )

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

# Load the data
oecd_bli_type_DataFrame = pd.read_csv("data/oecd_bli_2015.csv", thousands=',')
gdp_per_capita_type_DataFrame = pd.read_csv("data/gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values="n/a")

print("\ndata/oecd_bli_2015.csv")
print(oecd_bli_type_DataFrame.columns)
print("\n")
print(oecd_bli_type_DataFrame.head())
print("\n")
print(oecd_bli_type_DataFrame.INEQUALITY)

print("\ndata/gdp_per_capita.csv")
print(gdp_per_capita_type_DataFrame.columns)
print("\n")
print(gdp_per_capita_type_DataFrame.head())
print("\n")
print(gdp_per_capita_type_DataFrame['2015'])



# Prepare the data

def prepare_country_stats(oecd_bli_type_DataFrame, gdp_per_capita_type_DataFrame):
    # get the pandas dataframe of GDP per capita and Life satisfaction
    oecd_bli_type_DataFrame = oecd_bli_type_DataFrame[oecd_bli_type_DataFrame["INEQUALITY"]=="TOT"]

    # what this does?
    oecd_bli_type_DataFrame = oecd_bli_type_DataFrame.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita_type_DataFrame.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita_type_DataFrame.set_index("Country", inplace=True)
    full_country_stats_type_DataFrame = pd.merge(left=oecd_bli_type_DataFrame, right=gdp_per_capita_type_DataFrame, left_index=True, right_index=True)
    return full_country_stats_type_DataFrame[["GDP per capita", 'Life satisfaction']]

country_stats_type_DataFrame = prepare_country_stats(oecd_bli_type_DataFrame, gdp_per_capita_type_DataFrame)
X_type_ndarray = np.c_[country_stats_type_DataFrame["GDP per capita"]]
y_type_ndarray = np.c_[country_stats_type_DataFrame["Life satisfaction"]]

# Visualize the data
country_stats_type_DataFrame.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
plt.show()

# Select a linear model
model_type_LinearRegression = sklearn.linear_model.LinearRegression()

# Train the model
model_type_LinearRegression.fit(X_type_ndarray, y_type_ndarray)

# Make a prediction for Cyprus
X_new_type_list = [[22587]] # Cyprus's GDP per capita
print(model_type_LinearRegression.predict(X_new_type_list)) # outputs [[ 5.96242338]]


import sklearn.linear_model
model_type_LinearRegression = sklearn.linear_model.LinearRegression()

import sklearn.neighbors
model_type_KNeighborsRegressor = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)
print("test")



print( "\nHello world!" )
# import the needed libraries
import os
import tarfile
import urllib

# get the necessary paths tp the data or folder as a string
DOWNLOAD_ROOT_type_str = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH_type_str = os.path.join("data/datasets", "housing")
HOUSING_URL_type_str = DOWNLOAD_ROOT_type_str + "datasets/housing/housing.tgz"

def fetch_housing_data( housing_url_type_str = HOUSING_URL_type_str, housing_path_type_str = HOUSING_PATH_type_str ):
    os.makedirs( housing_path_type_str, exist_ok = True )
    tgz_path_type_str = os.path.join( housing_path_type_str, "housing.tgz" )
    urllib.request.urlretrieve( housing_url_type_str, tgz_path_type_str )
    housing_tgz_type_TarFile = tarfile.open( tgz_path_type_str )
    housing_tgz_type_TarFile.extractall( path = housing_path_type_str )
    housing_tgz_type_TarFile.close()

fetch_housing_data( housing_url_type_str = HOUSING_URL_type_str, housing_path_type_str = HOUSING_PATH_type_str )

