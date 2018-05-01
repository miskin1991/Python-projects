def littlenumbers(input_number: object = 1) -> object:
    if input_number == 1:
        output_string = 'one'
    elif input_number == 2:
        output_string = 'two'
    elif input_number == 3:
        output_string = 'three'
    elif input_number == 4:
        output_string = 'four'
    elif input_number == 5:
        output_string = 'five'
    elif input_number == 6:
        output_string = 'six'
    elif input_number == 7:
        output_string = 'seven'
    elif input_number == 8:
        output_string = 'eight'
    elif input_number == 9:
        output_string = 'nine'
    else:
        output_string = ""
    return output_string


def mediumnumbers(input_number=10):
    if input_number == 10:
        print('ten')
    elif input_number == 11:
        print('eleven')
    elif input_number == 12:
        print('twelve')
    elif input_number == 13:
        print('thirteen')
    elif input_number == 14:
        print('fourteen')
    elif input_number == 15:
        print('fifteen')
    elif input_number == 16:
        print('sixteen')
    elif input_number == 17:
        print('seventeen')
    elif input_number == 18:
        print('eighteen')
    elif input_number == 19:
        print('nineteen')


def largenumbers(input_number=2):
    if input_number == 2:
        output_string = 'twenty'
    elif input_number == 3:
        output_string = 'thirty'
    elif input_number == 4:
        output_string = 'forty'
    elif input_number == 5:
        output_string = 'fifty'
    elif input_number == 6:
        output_string = 'sixty'
    elif input_number == 7:
        output_string = 'seventy'
    elif input_number == 8:
        output_string = 'eighty'
    elif input_number == 9:
        output_string = 'ninety'
    else:
        output_string = ""
    return output_string


a = int(input())

if (a < 0) or (a > 100):
    print('invalid number')
    exit()
else:
    if a == 0:
        print('zero')
    elif a < 10:
        number_string = littlenumbers(a)
        print(number_string)
    elif a < 20:
        mediumnumbers(a)
    elif a < 100:
        decimalPart = int(a / 10)
        decimal_string = largenumbers(decimalPart)
        print(decimal_string, end="")
        numberPart = a % 10
        number_string = littlenumbers(numberPart)
        if number_string != "":
            print(" " + number_string)
    else:
        print('one hundred')
