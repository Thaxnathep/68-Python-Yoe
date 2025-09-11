def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError as e:
        print("Exception: ", e)
    except ValueError as a:
        print("Exception: ", a)
    else:
        return result

a,b = map(int, input("Y").split())
print(divide(a,b))
print("End of the Program")