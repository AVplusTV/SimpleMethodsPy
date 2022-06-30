def sum_numbers(text: str) -> int:
    # your code here
    list = text.split()
    j = 0
    
    for i in list:
        try:
            j += int(i)
        except:
            pass
    print(j)
    
sum_numbers('hi')
sum_numbers('who is 1st here')
sum_numbers('my numbers is 2')
sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year')
sum_numbers('5 plus 6 is')
sum_numbers('')

print(type(int(10)/int(5)))

