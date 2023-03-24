# Dynamic plot of matrix-multiplication

For main.py, the program asks the user to enter the dimension for the square matrix and the time interval. 

It will then create an n x n matrix with random values and an 1 x n matrix with random values for matrix multiplication.

It will then feed the data to function.py to do the matrix multiplication and transfer back the results to main.py.

It will continue doing multiplication for every duration based on the time interval input (can go down to 1ms). 

Press CTRL + C to cancel the program.

After canceling, it will output a dynamic plot, Output.gif, that shows the plot for each variable result of the matrix.

master.py, is a combining script that call main.py and function.py.

The source files are also compiled to .exe files using pyinstaller that can use for Windows which can be found [here](https://drive.google.com/drive/folders/1cger0ftq7A_Lra9puRBEwgwmZrF9f1ue?usp=sharing)
