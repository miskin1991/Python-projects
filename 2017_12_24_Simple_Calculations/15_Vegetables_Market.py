priceVegetables = float(input())
priceFruits = float(input())
kgVegetables = int(input())
kgFruits = int(input())

incomeVegetables = kgVegetables * priceVegetables
incomeFruits = kgFruits * priceFruits

incomeTotal = incomeVegetables + incomeFruits

incomeTotalInEuro = incomeTotal / 1.94

print(incomeTotalInEuro)
