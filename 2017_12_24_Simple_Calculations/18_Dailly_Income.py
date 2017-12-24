workDaysPerMonth = int(input())
incomePerDay = float(input())
USDinBGN = float(input())

monthSalaryUSD = workDaysPerMonth * incomePerDay

yearSalaryBeforeTaxUSD = monthSalaryUSD * 12 + monthSalaryUSD * 2.5

yearSalaryAfterTaxUSD = yearSalaryBeforeTaxUSD * 0.75

averageIncomePerDayUSD = yearSalaryAfterTaxUSD / 365

averageIncomePerDayBGN = averageIncomePerDayUSD * USDinBGN

print("{0:.2f}".format(averageIncomePerDayBGN))
