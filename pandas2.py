import pandas as pd

df=pd.read_csv("adultData.csv")

race_count=pd.Series(df["race"].value_counts())
average_age_men = round(df[df["sex"]=="Male"]["age"].mean(),1)
percentage_bachelors=round((len(df[df["education"]=="Bachelors"])/len(df["education"]))*100,1)
total_bachelors=(df[((df["education"] == "Bachelors") |
                                (df["education"] == "Masters")|
                                (df["education"] == "Doctorate"))])

bachelors_and_high_salary = (df[((df["education"] == "Bachelors") |
                                (df["education"] == "Masters")|
                                (df["education"] == "Doctorate")) 
                                & (df["salary"] == ">50K")])

higher_education_earners_50k=round((len(bachelors_and_high_salary) / len(total_bachelors)) * 100)
lower_education = (df[((df["education"] != "Bachelors") |
                                (df["education"] != "Masters")|
                                (df["education"] != "Doctorate"))]) 
lower_education_50k = (df[((df["education"] != "Bachelors") |
                                (df["education"] != "Masters")|
                                (df["education"] != "Doctorate")) 
                                & (df["salary"] == ">50K")])      
lower_education_earners_50k=round((len(lower_education_50k) / len(lower_education)) * 100,1)

minimum_work_hour=round(df["hours-per-week"].min())
people_work_h_wk=(df["hours-per-week"]==1)
people_min_work_hour_sal=(df[(df["hours-per-week"]==1)& (df["salary"] == ">50K")])

perc_higher_salary_min_hour_wk=round((len(people_min_work_hour_sal)/ len(people_work_h_wk))*100,1)
country_highest_salary= round((df[(df["salary"]==">50K")]["native-country "].value_counts()/ df["native-country "].value_counts())*100,1)
country_highest_salary= country_highest_salary.sort_values(ascending = False)
highest_earning_country=country_highest_salary.index[0]
highest_earning_country_per = country_highest_salary[0]

print("Number of each race:",race_count)
print("Average age of men:",average_age_men)
print("Percentage of people with Bachelors degrees:",{percentage_bachelors},"%") 
print("Percentage of people with higher education that earn >=50K:",{higher_education_earners_50k},"%")
print("Percentage of people with no advanced education make more than 50k:",{lower_education_earners_50k},"%")
print("Minimum number of hours a person work per week:",minimum_work_hour)
print("Percentage of the people who works the minimum number of hours per week and that earn  >50k :",{perc_higher_salary_min_hour_wk},"%")
print("Coutry with the highest percentage of people that earn >50k:",{highest_earning_country_per},"%")

