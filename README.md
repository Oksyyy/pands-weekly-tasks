# Programming and Scripting 
by Oksana Abrosimova

This repository contains multiple Python programms created as part of the Programming and Scripting study module. To demonstrate learning and understanding of the module's materials, a set of assigned task has been completed. References to resources used and any other documentation are provided below under sections corresponding to each week task.  

 ## Week 02 task
 The task was completed primarely using lecture materials. 
 
 To round the final amount to two decimal places, the `:.2f` method within f-strings was used. For guidance on handling f-strings the following [DataCamp guide](https://www.datacamp.com/tutorial/python-f-string) was reviewed.


 ## Week 03 task
 For week 3, two programs were created: 
  1.  accounts.py - This program handles the main task, which involves generating an account number of a specified length (10 digits)
  2.  accounts_extra.py - This program addresses the extra task, which involves generating an account number of unspecified length 
 
 The task was completed using W3schools tutorials where I learned the following:
 - Slicing strings: [W3school](https://www.w3schools.com/python/python_strings_slicing.asp)
 - Replacing strings: [W3school](https://www.w3schools.com/python/python_strings_modify.asp)
 - The `len()` function: [W3school](https://www.w3schools.com/python/ref_func_len.asp)
 
 For the extra task, I found an article on string multiplication, which helped me mask an unspecified number of digits dynamically: [GeeksforGeeks](https://www.geeksforgeeks.org/create-multiple-copies-of-a-string-in-python-by-using-multiplication-operator/).


 ## Week 04 task
The task was completed primarely using week 4 lecture materials, with a focus on `while loop` and `if` functions.

Additional context on while loops was reviewed in the following [RealPython](https://realpython.com/python-while-loop/) tutorial.

To print out numbers on the same line (I wasn't sure if it was a part of the weekly task or just unintended format of the provided example) - I referred to the [GeeksforGeeks](https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/) article that explaind the use of `end=''` function.


 ## Week 05 task
The task was completed using [3wschools Python Datetime](https://www.w3schools.com/python/python_datetime.asp) tutorial, where I learned the following:
   - Requirement to import `datetime` module
   - The `datetime.datetime.now()` function to access current date
   - The `strftime()` method that was used to return current date in a format where a weekday is represented by a number.

Additionally, I used the following [3wschools](https://www.w3schools.com/python/ref_func_range.asp) tutorial to learn about the `range()` function, which was used in the if condition. 


 ## Week 06 task
For week 6, I read multiple articles and watched videos to understand the Newton-Raphson Method for calculating square roots. While I reviewed a variety of sources, I would highlight the following as the most helpful:
1) A comprehensive concept explanation can be found here: [Graphic Maths](https://graphicmaths.com/pure/numerical-methods/newton-raphson-method/)
2) These two sources provided the necessary logic to implement Newton's method in Python: 
   - [Altcademy](https://www.altcademy.com/blog/how-to-square-root-in-python/#:~:text=The%20Newton%2DRaphson%20Method,-The%20Newton%2DRaphson&text=refine%20the%20guess%3A-,Start%20with%20an%20initial%20guess%20x0%20.,smaller%20than%20a%20predefined%20threshold.)
   - [HackerNoon](https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo)


 ## Week 07 task
For the Week 7 task, I assumed that the moby-dick.txt file needed to be downloaded and available locally on the machine in order for the program to read the filename passed as an argument on the command line. The text file was downloaded from 
[Project Gutenberg](https://www.gutenberg.org/ebooks/2701) and storred in the same directory as the program itself.

The second part of the task involved passing a text file as an argument on the command-line. This was implemented using `sys.argv()function`, which is a part of the `sys module`. A helpful explanation on how to use sys.argv and relevant examples can be found in the following article: [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/). For further information on the sys module, I also referred to the official [Python Documentation](https://docs.python.org/3/library/sys.html).

To count the occurences of the charachter 'e', I used the `count()` function.  Information on this method is available under Python String Methods in [W3schools](https://www.w3schools.com/python/python_ref_string.asp#gsc.tab=0).

While not directly related to the lecture topic, I also had to revisit the concept of initializing variables in Python in order to implement charachters count. I found this [Medium article](https://medium.com/@esaiahsamuel710/python-variables-data-initialization-and-declaration-647719a470c2
) to be helpful in clarifying the topic.


## Week 08 task
The task was comlited primarely using lecture materials as a reference. To create a normal distribution for the histogram, I used the `numpy.random.normal()` function. For guidance and examples, I referred to [W3schools](https://www.w3schools.com/python/numpy/numpy_random_normal.asp).

To define the function `h(x)=x**3`, I chose to use NumPy's `linspace()` function to generate a range of values. I found the following [Medium article](https://ogre51.medium.com/python-range-numpy-arange-and-numpy-linspace-17235c629710) helpful in comparing different approaches. For further understanding of how linspace() works, I also referred to this
[DataCamp tutorial](https://www.datacamp.com/tutorial/how-to-use-the-numpy-linspace-function).