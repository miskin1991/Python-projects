amountBitCoins = int(input())
amountYuan = float(input())
commission = float(input())

bitCoinsInBGN = 1168
yuanInUSD = 0.15
USDinBGN = 1.76
EURinBGN = 1.95

bitCoinsValueInEUR = amountBitCoins * bitCoinsInBGN / EURinBGN

yuanValueInEUR = amountYuan * yuanInUSD * USDinBGN / EURinBGN

amountOfMoneyInEUR = bitCoinsValueInEUR + yuanValueInEUR

commissionInEUR = amountOfMoneyInEUR * commission / 100

totalMoney = amountOfMoneyInEUR - commissionInEUR

print("{0:.2f}".format(totalMoney))
