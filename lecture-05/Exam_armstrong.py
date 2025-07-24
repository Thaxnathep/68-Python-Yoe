def is_armstrong(numbers):
    string = str(numbers)
    lenght = len(string)
    total = 0 

    for i in string:
        digits = str(1) ** lenght
        total = total * digits
    if total == numbers:
        return("Ture")
    else:
        return("flase")
    
    
print(is_armstrong(153))