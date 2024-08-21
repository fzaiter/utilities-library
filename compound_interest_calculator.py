"""
Calculator for compound interest.
It interactively takes initial deposit, annualized return,
monthly contribution, and duration of the investment in years
as input and displays the results in a tabular format.
"""

from tabulate import tabulate, SEPARATING_LINE

print("""
       ________________________________
       COMPOUND INTEREST CALCULATOR
       ________________________________
       """)
initial_deposit = int(input("Enter the initial deposit: "))
annualized_return = (float(
    input("Enter the annualized return on investment (the percentage value): ")))/100
monthly_contribution = int(input("Enter the monthly contribution: "))
duration_years = int(input("Enter the duration of the investment in years: "))

monthly_return = annualized_return/12
duration_months = duration_years/12

final_result = list()
total_interest_obtained = 0
total_contribution = 0
initial_value = initial_deposit

print("""
       ________________________________
       COMPOUND INTEREST RESULTS
       ________________________________
       """)

for year in range(duration_years):
    for month in range(12):
        interest_obtained = initial_value*monthly_return
        final_value = (initial_value + interest_obtained)+monthly_contribution
        initial_value = final_value
        monthly_results = [year+1, month+1,
                           round((interest_obtained), 2), round((final_value), 2)]
        total_interest_obtained += interest_obtained
        total_contribution += monthly_contribution
        final_result.append(monthly_results)
    final_result.append(SEPARATING_LINE)

print(tabulate(final_result, headers=[
      'Year', 'Month', 'Interest Earned (€)', 'Final Value (€)'], tablefmt='pretty'))
print("Total Contribution: "+str(round((total_contribution), 2)) + " €")
print("Total interest earned: "+str(round((total_interest_obtained), 2)) + " €")
