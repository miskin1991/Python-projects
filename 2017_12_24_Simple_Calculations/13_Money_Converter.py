moneyInput = float(input())
inputCurrency = input()
outputCurrency = input()

BGN = float(1.79549)
EUR = float(1.95583)
GBP = float(2.53405)

if inputCurrency == "BGN":
    if outputCurrency == "USD":
        moneyOutput = moneyInput / BGN
    elif outputCurrency == "EUR":
        moneyOutput = moneyInput / EUR
    elif outputCurrency == "GBP":
        moneyOutput = moneyInput / GBP
    else:
        print("Wrong output currency")
        exit(1)
elif inputCurrency == "USD":
    if outputCurrency == "BGN":
        moneyOutput = moneyInput * BGN
    elif outputCurrency == "EUR":
        moneyOutput = moneyInput * BGN / EUR
    elif outputCurrency == "GBP":
        moneyOutput = moneyInput * BGN / GBP
    else:
        print("Wrong output currency")
        exit(1)
elif inputCurrency == "EUR":
    if outputCurrency == "BGN":
        moneyOutput = moneyInput * EUR
    elif outputCurrency == "USD":
        moneyOutput = moneyInput * EUR / BGN
    elif outputCurrency == "GBP":
        moneyOutput = moneyInput * EUR / GBP
    else:
        print("Wrong output currency")
        exit(1)
elif inputCurrency == "GBP":
    if outputCurrency == "BGN":
        moneyOutput = moneyInput * GBP
    elif outputCurrency == "EUR":
        moneyOutput = moneyInput * GBP / EUR
    elif outputCurrency == "USD":
        moneyOutput = moneyInput * GBP / BGN
    else:
        print("Wrong output currency")
        exit(1)
else:
    print("Wrong input currency")
    exit(1)

print(f"{moneyOutput:.2f} {outputCurrency}")
