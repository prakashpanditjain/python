import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format


path = './salaries_by_college_major.csv'

df = pd.read_csv(path)

print(df.iloc[0])

max_salary = df['Mid-Career 90th Percentile Salary'].max()

# print(df[(df['Mid-Career 90th Percentile Salary'].max() & (df['Undergraduate Major'] == 'Physics'))])

# print(df[df['Undergraduate Major'] == 'Physics']['Mid-Career 90th Percentile Salary'].max())

#print the second occurence of the number in a list

#which category of degrees has highest average salary? is it STEM or Business? or HASS
print(df.groupby('Group')['Mid-Career 90th Percentile Salary'].mean())

print("how many majors are there in each group?")
print(df.groupby('Group').count())

#For STEM majors, what is the average salary for each major?
print(df[df['Group'] == 'STEM']['Mid-Career 90th Percentile Salary'].mean())

#distinct Group
print(df['Group'].unique())

major_dict = {}

for group in df['Group'].unique()[:-1]:
    # Calculate the average salary for each group
    for major in df.columns.tolist():
        # Skip the 'Group' and 'Undergraduate Major' columns
        if major != 'Group' and major != 'Undergraduate Major':
            # Calculate the average salary for each major in the group
            avg_salary = round(df[df['Group'] == group][major].mean(),2)
            major_dict[group] = avg_salary
            print(f"Average salary for {major} major of {group}: {avg_salary}")

#print columns
print(df.columns.tolist())

