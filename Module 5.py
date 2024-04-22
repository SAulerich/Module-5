Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> total_Rainfall = float(0.0)
>>> total_Months = int(0)
>>> total_Years = int(input("Enter the number of years: "))
Enter the number of years: 2
>>>
>>> for year in range(1, total_Years + 1):
... for month in range(1, 13):
  File "<stdin>", line 2
    for month in range(1, 13):
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for year in range(1, total_Years + 1):
...     for month in range(1, 13):
...             rainfall = float(input(f' During the {month} month of the {year} year, there was approximately this much rainfall that occurred (in inches): '))
...             total_Rainfall += rainfall
...             total_Months += 1
...
 During the 1 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 3.2
 During the 2 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 2.5
 During the 3 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 4.6
 During the 4 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 3.1
 During the 5 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 4.4
 During the 6 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 4.6
 During the 7 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 3.8
 During the 8 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 3.9
 During the 9 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 2.4
 During the 10 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 3.0
 During the 11 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 3.1
 During the 12 month of the 1 year, there was approximately this much rainfall that occurred (in inches): 3.3
 During the 1 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 4.5
 During the 2 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 5.6
 During the 3 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 4.2
 During the 4 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 5.4
 During the 5 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 4.8
 During the 6 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 4.0
 During the 7 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 3.3
 During the 8 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 4.1
 During the 9 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 3.6
 During the 10 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 3.2
 During the 11 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 4.9
 During the 12 month of the 2 year, there was approximately this much rainfall that occurred (in inches): 3.4
>>>
>>> average_Rainfall = total_Rainfall / total_Months
>>> print("{:.2f}".format(average_Rainfall))
3.87
>>>
>>> print("The number of months:", total_Months,"\n Total inches of rainfall:", total_Rainfall, "\n Average rainfall per month for the entire period: {a
verage_Rainfall:.2f}")
The number of months: 24
 Total inches of rainfall: 92.9
 Average rainfall per month for the entire period: {average_Rainfall:.2f}
>>> print("The number of months:", total_Months,"\nTotal inches of rainfall:
", total_Rainfall, f"\nAverage rainfall per month for the entire period: {av
erage_Rainfall:.2f}")
The number of months: 24
Total inches of rainfall: 92.9
Average rainfall per month for the entire period: 3.87
>>>
>>>
>>>
>>>
>>>
>>> total_Points =
  File "<stdin>", line 1
    total_Points =
                   ^
SyntaxError: invalid syntax
>>> total_Points = 0
>>>
>>> books_Bought = int(input("Please, enter the number of books you have purchased this month: "))
Please, enter the number of books you have purchased this month: 7
>>>
>>> if 0 <= books_Bought <= 1:
...     points = 0
... elif 2 <= books_Bought <= 3:
...     points = 5
... elif 4 <= books_Bought <=5:
...     points = 15
... elif 6 <= books_Bought <= 7:
...     points = 30
... else:
...     points = 60
...
>>> total_Points += points
>>>
>>> print(f"Amazing! You received {total_Points} points this month. How exci
ting!!")
Amazing! You received 30 points this month. How exciting!!
>>>
