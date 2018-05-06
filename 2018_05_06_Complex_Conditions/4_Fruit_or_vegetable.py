fruit = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetable = ['tomato', 'cucumber', 'pepper', 'carrot']

product = input().lower()
found = 'false'

for item in fruit:
   if product == item:
       print('fruit')
       found = 'true'
       break
for item in vegetable:
    if product == item:
        print('vegetable')
        found = 'true'

if found == 'false':
    print('unknown')
