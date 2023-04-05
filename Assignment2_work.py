"""
@author: Dileepa Jayamanne: 22031359
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import stats as st
import seaborn as sns

file_name = 'climate-change.csv'


def Obtain_dataframes(file_name):
    """This function will accept the file name of the csv file to read and
    output two dataframes one with years as columns and one with countries 
    as columns.
    """
    DF = pd.read_csv(file_name, sep='delimitor', header=None, skiprows=(3))
    DF.set_axis(['Data'], axis='columns', inplace=True)
    DF1 = DF['Data'].str.split(',', expand=True)

    for k in range(DF1.shape[0]):
        DF1.iloc[k] = DF1.iloc[k].str.strip(
            '"')  # Getting rid of double quotes

    DF2 = DF1.T.copy()          # For countries as columns
    DF1.columns = DF1.iloc[0]   # making the 1st row as the column head
    DF1 = DF1.drop(axis=0, index=0).reset_index(
        drop=True)  # Droping the first row

    #countries = ['United States','United Kingdom', 'Germany', 'Brazil', 'Russian Federation', 'India', 'China', 'South Africa', 'Sri Lanka', 'Nigeria', 'Cuba', 'Ecuador']
    countries = ['United States', 'United Kingdom']

    US = DF1[(DF1["Country Name"] == f"{countries[0]}") |
             (DF1["Country Name"] == f"{countries[1]}")].reset_index(drop=True)
    print(type(US))
    US.to_csv("US.csv")

    DF2.columns = DF2.iloc[0]  # making the 1st row as each column head
    DF2 = DF2.drop(0).reset_index(drop=True)  # Dropping the 1st row
    return (DF1, DF2)


[DF1, DF2] = Obtain_dataframes(file_name)

print(DF1.head())
print(DF2.head())


def stat_func(distribution, name):
    """ This function accepts the numerical column of data of a dataframe and
    output skewness and kurtosis using two methods.
    """
    average = distribution.mean()
    std = distribution.std()
    skewness = distribution.skew()
    skewness_using_stats = st.skew(distribution)
    kurtosis = distribution.kurtosis()
    kurtosis_using_stats = st.kurtosis(distribution)
    print(
        f"\nDistribution: {name}\nStandard Deviation: {std}\nSkewness: {skewness}\nKurtosis: {kurtosis}")
    print(f"skewness using stats: {skewness_using_stats}")
    print(f"kurtosis using stats: {kurtosis_using_stats}")
    return


# Obtaining Statistics and Multiple bargrapgh : CO2 Emission

CO2_emissions = DF1.loc[DF1.loc[:, 'Indicator Code']
                        == 'EN.ATM.CO2E.KT', :].reset_index(drop=True)
CO2_emissions.to_csv('Urban_population.csv')

CO2_emissions_temp = CO2_emissions.T

ROWS = np.asarray(list(CO2_emissions_temp.index.values))
ROWS = np.delete(ROWS, [1, 2, 3])
CO2_emissions_temp = CO2_emissions_temp.loc[ROWS]
# making the 1st row as each column head
CO2_emissions_temp.columns = CO2_emissions_temp.iloc[0]
CO2_emissions_window = CO2_emissions_temp.loc['1990':'2015']

print("Exploring Statistical Properties of CO2 emissions for United States from 1990 to 2015\n")
CO2_emissions_US = pd.DataFrame(CO2_emissions_window["United States"])
CO2_emissions_US.columns = ["United States CO2 emission"]
print(CO2_emissions_US.describe())

name = "US CO2 emissions"
stat_func(CO2_emissions_US, name)

print("\nExploring Statistical Properties of CO2 emissions for United Kingdom from 1990 to 2015\n")
CO2_emissions_UK = pd.DataFrame(CO2_emissions_window["United Kingdom"])
CO2_emissions_UK.columns = ["United Kingdom CO2 emission"]
print(CO2_emissions_UK.describe())

print("\nExploring Statistical Properties of CO2 emissions of countries from 1990 to 2015\n")
print(CO2_emissions_window.describe())


years = [f"{i:04d}" for i in range(1990, 2015+1, 5)]
countries = ['United States', 'United Kingdom', 'Germany', 'Brazil', 'Russian Federation',
             'India', 'China', 'South Africa', 'Sri Lanka', 'Nigeria', 'Cuba', 'Ecuador']
X_axis = np.arange(len(countries))
frame = {}
for country in countries:
    case = {
        f"{country}": CO2_emissions_window.loc[years, country].astype(float)}
    frame.update(case)

# Creating DataFrame by passing Dictionary
DF_temp = pd.DataFrame(frame)
DF_temp = DF_temp.T
#row_labels = DF_temp.index.values
row_labels = ['US', 'UK', 'Germany', 'Brazil', 'Russia', 'India',
              'China', 'South Africa', 'Sri Lanka', 'Nigeria', 'Cuba', 'Ecuador']
DF_temp["Country"] = row_labels
plt.figure()
DF_temp.plot(x="Country", y=years, kind="bar")
plt.legend(years)
plt.xlabel('Country Name')
plt.ylabel('CO2 emission (kt)')
plt.title('CO2 emission (kt) of countries over the years')
plt.xticks(rotation=30.0)
plt.savefig("CO2_emissions_multiple_barchart.png",
            dpi=300, bbox_inches="tight")


# Obtaning Statistics and Multiple bargrapgh : GDP

file_name = 'economy-and-growth.csv'
[DF3, DF4] = Obtain_dataframes(file_name)

GDP = DF3[DF3['Indicator Code'] == 'NY.GDP.MKTP.CD'].reset_index(drop=True)
GDP_temp = GDP.T

ROWS = np.asarray(list(GDP_temp.index.values))
ROWS = np.delete(ROWS, [1, 2, 3])
GDP_temp = GDP_temp.loc[ROWS]
GDP_temp.columns = GDP_temp.iloc[0]  # making the 1st row as each column head
GDP_window = GDP_temp.loc['1990':'2015']

print("\nExploring Statistical Properties of GDP US($) of countries from 1990 to 2015")
print(GDP_window.describe())


years = [f"{i:04d}" for i in range(1990, 2015+1, 5)]
countries = ['United States', 'United Kingdom', 'Germany', 'Brazil', 'Russian Federation',
             'India', 'China', 'South Africa', 'Sri Lanka', 'Nigeria', 'Cuba', 'Ecuador']
X_axis = np.arange(len(countries))
frame = {}
for country in countries:
    case = {f"{country}": GDP_window.loc[years, country].astype(float)}
    frame.update(case)

# Creating DataFrame by passing Dictionary
DF_temp = pd.DataFrame(frame)
DF_temp = DF_temp.T
#row_labels = DF_temp.index.values
row_labels = ['US', 'UK', 'Germany', 'Brazil', 'Russia', 'India',
              'China', 'South Africa', 'Sri Lanka', 'Nigeria', 'Cuba', 'Ecuador']

DF_temp["Country"] = row_labels
plt.figure(dpi=300)
DF_temp.plot(x="Country", y=years, kind="bar")
plt.legend(years)
plt.xlabel('Country Name')
plt.ylabel('GDP (US $)')
plt.title('GDP (US $) of countries over the years')
plt.xticks(rotation=30.0)
plt.savefig("GDP_multiple_barchart.png", dpi=300, bbox_inches="tight")


# Multiple Line Graphs: Energy use %

energy_use = DF1[DF1['Indicator Code'] ==
                 'EG.USE.PCAP.KG.OE'].reset_index(drop=True)
energy_use_temp = energy_use.T
ROWS = np.asarray(list(energy_use_temp.index.values))
ROWS = np.delete(ROWS, [1, 2, 3])
energy_use_temp = energy_use_temp.loc[ROWS]
# making the 1st row as each column head
energy_use_temp.columns = energy_use_temp.iloc[0]
energy_use_window = energy_use_temp.loc['1990':'2015']
energy_use_window.to_csv('energy_usage.csv')

# f string to generate years
years = [f"{i:04d}" for i in range(1990, 2016, 3)]
print("Years for plot: ", years)

countries = ['United States', 'United Kingdom', 'Germany', 'Brazil', 'Russian Federation',
             'India', 'China', 'South Africa', 'Sri Lanka', 'Nigeria', 'Cuba', 'Ecuador']

plt.figure()
for country in countries:
    #plt.plot(energy_use_window[f"{country}"] , label=country, linestyle = '-.')
    plt.plot(energy_use_window.loc[years, country].astype(
        float), label=country, linestyle='-.')
plt.xlabel("Years")
plt.ylabel("Energy use - kg of oil equivalent per capita")
plt.title('Energy use (kg of oil equivalent per capita) of countries over the years')
plt.legend(loc=(1.04, 0))
plt.savefig("Energy_use_multiple_linechart.png", dpi=300, bbox_inches="tight")


# Multiple Line Graph: Electric power consumption %

electric_consumption = DF1[DF1['Indicator Code']
                           == 'EG.USE.ELEC.KH.PC'].reset_index(drop=True)
electric_consumption_temp = electric_consumption.T
ROWS = np.asarray(list(energy_use_temp.index.values))
ROWS = np.delete(ROWS, [1, 2, 3])
electric_consumption_temp = electric_consumption_temp.loc[ROWS]
# making the 1st row as each column head
electric_consumption_temp.columns = electric_consumption_temp.iloc[0]
electric_consumption_window = electric_consumption_temp.loc['1990':'2015']
electric_consumption_window.to_csv('electric_consumption.csv')

# f string to generate years
years = [f"{i:04d}" for i in range(1990, 2016, 3)]
print("Years for plot: ", years)

countries = ['United States', 'United Kingdom', 'Germany', 'Brazil', 'Russian Federation',
             'India', 'China', 'South Africa', 'Sri Lanka', 'Nigeria', 'Cuba', 'Ecuador']

plt.figure()
for country in countries:
    #plt.plot(energy_use_window[f"{country}"] , label=country, linestyle = '-.')
    plt.plot(electric_consumption_window.loc[years, country].astype(
        float), label=country, linestyle='-.')
plt.xlabel("Years")
plt.ylabel("Electric power consumption per capita")
plt.title('Electric power consumption per capita of countries over the years')
plt.legend(loc=(1.04, 0))
plt.savefig("Electric_power_consumption_multiple_linechart.png",
            dpi=300, bbox_inches="tight")


# Table : Urban Population as a percentage of over all population

urban_population = DF1[DF1['Indicator Code'] ==
                       'SP.URB.TOTL.IN.ZS'].reset_index(drop=True)
urban_population_temp = urban_population.T
ROWS = np.asarray(list(urban_population_temp.index.values))
ROWS = np.delete(ROWS, [1, 2, 3])
urban_population_temp = urban_population_temp.loc[ROWS]
# making the 1st row as each column head
urban_population_temp.columns = urban_population_temp.iloc[0]
urban_population_window = urban_population_temp.loc['1990':'2015']
urban_population_window.to_csv('urban_population.csv')

countries = ['United States', 'United Kingdom', 'Germany', 'Brazil', 'Russian Federation',
             'India', 'China', 'South Africa', 'Sri Lanka', 'Nigeria', 'Cuba', 'Ecuador']
frame = {}
for country in countries:
    case = {f"{country}": urban_population_window[f"{country}"].astype(float)}
    frame.update(case)

Table = pd.DataFrame(frame)

# f string to generate years
years = [f"{i:04d}" for i in range(1990, 2016, 5)]
print("Years for consideration: ", years)

Table_extract = Table.loc[years].T
print(Table_extract.head())


# Access to Electricity:

electricity_access = DF1[DF1['Indicator Code']
                         == 'EG.ELC.ACCS.ZS'].reset_index(drop=True)
electricity_access_temp = electricity_access.T
ROWS = np.asarray(list(electricity_access_temp.index.values))
ROWS = np.delete(ROWS, [1, 2, 3])
electricity_access_temp = electricity_access_temp.loc[ROWS]
# making the 1st row as each column head
electricity_access_temp.columns = electricity_access_temp.iloc[0]
electricity_access_window = electricity_access_temp.loc['1990':'2015']
electricity_access_window.to_csv('electricity_access.csv')


# Renewable energy consumption %

renewable_energy_cons = DF1[DF1['Indicator Code']
                            == 'EG.FEC.RNEW.ZS'].reset_index(drop=True)
renewable_energy_cons_temp = renewable_energy_cons.T
ROWS = np.asarray(list(renewable_energy_cons_temp.index.values))
ROWS = np.delete(ROWS, [1, 2, 3])
renewable_energy_cons_temp = renewable_energy_cons_temp.loc[ROWS]
# making the 1st row as each column head
renewable_energy_cons_temp.columns = renewable_energy_cons_temp.iloc[0]
renewable_energy_cons_window = renewable_energy_cons_temp.loc['1990':'2015']
renewable_energy_cons_window.to_csv('renewable_energy_consumption.csv')


# Correlation heat maps for countries

#countries = ['China', 'United States']
countries = ['United States', 'China', 'Brazil',
             'Russian Federation', 'India', 'China']
for country in countries:
    C1 = CO2_emissions_window[f"{country}"].replace(
        r'^\s*$', np.nan, regex=True)
    C1 = C1.loc["1990":"2015"].astype(float)
    C2 = electric_consumption_window[f"{country}"].replace(
        r'^\s*$', np.nan, regex=True)
    C2 = C2.loc["1990":"2015"].astype(float)
    C3 = energy_use_window[f"{country}"].replace(r'^\s*$', np.nan, regex=True)
    C3 = C3.loc["1990":"2015"].astype(float)
    C4 = GDP_window[f"{country}"].replace(r'^\s*$', np.nan, regex=True)
    C4 = C4.loc["1990":"2015"].astype(float)
    C5 = urban_population_window[f"{country}"].replace(
        r'^\s*$', np.nan, regex=True)
    C5 = C5.loc["1990":"2015"].astype(float)
    C6 = electricity_access_window[f"{country}"].replace(
        r'^\s*$', np.nan, regex=True)
    C6 = C6.loc["1990":"2015"].astype(float)
    C7 = renewable_energy_cons_window[f"{country}"].replace(
        r'^\s*$', np.nan, regex=True)
    C7 = C7.loc["1990":"2015"].astype(float)

    result = pd.concat([C1, C2, C3, C4, C5, C6, C7], axis=1).reset_index()
    result.columns = ['years', 'CO2 emissions (kt)', 'electric consumption %',
                      'energy use %', 'GDP in US($)', 'urban population %',
                      'electricity access %', 'renewable energy usage %']
    # print(result.corr())
    correlation_matrix = result.corr()
    plt.figure()

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(correlation_matrix, cmap=cmap, center=0,
                square=True, linewidths=.5, annot=True)
    plt.title(f"Correlation Matrix for {country}")
    plt.savefig(f"Correlation_matrix_{country}.png",
                dpi=300, bbox_inches="tight")
