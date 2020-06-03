import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
###################################################################

crime_data = pd.read_csv(r'D:\Hetav Documents\Medium Blogs\Black Racism in US\Main-data-hate_crime\hate_crime.csv')
c_data = crime_data[crime_data['BIAS_DESC'].str.contains('Anti-Black')]
print(c_data.tail())
stateList = np.zeros(53)
j = 0
stateName = sorted(list(set(c_data['STATE_NAME'])))
print(stateName)

for i in range(53):
    stateList[i] = list(c_data['STATE_NAME']).count(stateName[i])

###################################################################
## Plotting crimes from 1991 - 2018

plt.bar(stateName, stateList, color = 'fuchsia' ,align='center')
plt.title("Black Hate Crimes by State [US]")
plt.xticks(rotation=90)
plt.xlabel('States')
plt.ylabel('Cases')
plt.show()

crime_latest = c_data.query('DATA_YEAR == "2018" or DATA_YEAR == "2017"')
print(crime_latest)
latestList = np.zeros(53)


for i in range(53):
    latestList[i] = list(crime_latest['STATE_NAME']).count(stateName[i])

print(latestList)
print(stateName)

# Plotting crimes from 2017-2018

plt.bar(stateName, latestList, color = 'chartreuse', align = 'center')
plt.title("Recent Black Hate Crimes by State [US]")
plt.xticks(rotation=90)
plt.xlabel('States')
plt.ylabel('Cases')
plt.show()

# print(crime_latest['BIAS_DESC'])

###################################################################
# Plotting school enrolment of blacks in US by states

school_data = pd.read_excel(r'D:\Hetav Documents\Medium Blogs\Black Racism in US\NCES School data\tabn203.70.xls')
# print(school_data.head())
stateList = list(school_data['State or jurisdiction'][1:53])
black_per_2000 = list(school_data['Black'][1:53])
print(len(black_per_2000))
plt.bar(stateList, black_per_2000, color = 'cyan', label = '2000 Stats')
plt.title("Black Student Enrolment by State - 2000 [US]")
plt.xticks(rotation=90)
plt.xlabel('States')
plt.legend(loc = 'best')
plt.ylabel('Percentage Enrolment')
plt.show()

black_per_2017 = list(school_data['Black.1'][1:53])
plt.bar(stateList, black_per_2000, color = 'yellow', label = '2017 Stats')
plt.title("Black Student Enrolment by State - 2017 [US]")
plt.xticks(rotation=90)
plt.xlabel('States')
plt.ylabel('Percentage Enrolment')
plt.legend(loc = 'best')
plt.show()

Plotting the comparison between 2000 and 2017 enrolment data
n_groups = 52

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 1.0
print(index)
rects1 = plt.bar(index, black_per_2000, bar_width,alpha=opacity,color='cyan',label='2000')

rects2 = plt.bar(index + bar_width, black_per_2017, bar_width,alpha=opacity,color='grey',label='2017')

plt.xlabel('States')
plt.ylabel('Percentage Enrolment')
plt.title('Black Student Enrolment by State [US]')
plt.xticks(index + bar_width, stateList)
plt.xticks(rotation=90)
plt.legend()
plt.show()

###################################################################

income_data = pd.read_csv(r'D:\Hetav Documents\Medium Blogs\Black Racism in US\Us_2017_census_tract_data.csv\acs2017_census_tract_data.csv')
income_data = income_data.sort_values(by=['State'])
state_inc = np.zeros(52)
unemploy_stats = np.zeros(52)

income_data['IncomePerCap'] = income_data['IncomePerCap'].replace(np.nan, 0)
income_data['Unemployment'] = income_data['Unemployment'].replace(np.nan, 0)

state_name = sorted(list(set(income_data['State'])))
j = 0

for i in range(74001):
    if (list(income_data['State'])[i] == state_name[j]):
        state_inc[j] += list(income_data['IncomePerCap'])[i]
        unemploy_stats[j] += list(income_data['Unemployment'])[i]
    else:
        state_inc[j] = state_inc[j] / (list(income_data['State']).count(state_name[j]))
        unemploy_stats[j] = unemploy_stats[j] / (list(income_data['State']).count(state_name[j]))
        print(state_name[j])
        j += 1

state_inc[-1] = state_inc[-1] / (list(income_data['State']).count(state_name[j]))
unemploy_stats[-1] = unemploy_stats[-1] / (list(income_data['State']).count(state_name[j]))

print("i: ", i)
print("j: ", j)
print(state_inc)

plt.bar(state_name, state_inc, color = 'peachpuff', label = 'Per Capita Income')
plt.xlabel('States')
plt.ylabel('Per capita Income')
plt.title('Per Capita Income by State [US]')
plt.xticks(rotation=90)
plt.legend()
plt.show()

plt.bar(state_name, unemploy_stats, color = 'blue', label = 'Unemployment Percentage')
plt.xlabel('States')
plt.ylabel('Percentage')
plt.title('Unemployment Percentage by State [US]')
plt.xticks(rotation=90)
plt.legend()
plt.show()

###################################################################

parity_data = pd.read_csv(r'D:\Hetav Documents\Medium Blogs\Black Racism in US\US_income_census.csv\census.csv')
parity_data = parity_data[parity_data['race'].str.contains("Black|White", na=False)]
parity_data = parity_data.sort_values(by=['race'])
parity_data = parity_data.sort_values(by=['sex'])

## Checking for null values
print(parity_data.isnull().values.any())

print(parity_data['race'])
bMale = 0
wMale = 0
bFemale = 0
wFemale = 0
BMsum = 0
WMsum = 0
BFsum = 0
WFsum = 0

for i in range(len(parity_data['race'])):
    print(i)
    if list(parity_data['race'])[i] == 'Black':
        if list(parity_data['sex'])[i] == 'Male':
            bMale += 1
            BMsum += list(parity_data['fnlwgt'])[i]
        else:
            bFemale += 1
            BFsum += list(parity_data['fnlwgt'])[i]
    elif list(parity_data['race'])[i] == 'White':
        if list(parity_data['sex'])[i] == 'Male':
            wMale += 1
            WMsum += list(parity_data['fnlwgt'])[i]
        else:
            wFemale += 1
            WFsum += list(parity_data['fnlwgt'])[i]

print(bMale, bFemale, wMale, wFemale)
print(BMsum, WMsum, BFsum, WFsum)

category = 'Black Male', 'Black Female', 'White Male', 'White Female'
sizes = [BMsum/bMale, BFsum/bFemale, WMsum/wMale, WFsum/wFemale]

colors = ['cyan', 'chartreuse', 'magenta', 'yellow']
explode = (0.1, 0.1, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=category, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
