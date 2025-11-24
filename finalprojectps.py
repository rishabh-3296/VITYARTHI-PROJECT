import tkinter 

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray = "#D4D4D2"#these values are hexadecimal values for colors
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

#window setup
window = tkinter.Tk() #create the window
window.title("Calculator")#set window title
window.resizable(False, False)

frame = tkinter.Frame(window)#show window
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black,
                      foreground=color_white, anchor="e", width=column_count)#setting the  fornt , size , 
                                                          #foregrund color ,background color , and create space to type

label.grid(row=0, column=0, columnspan=column_count, sticky="we")#creatinf lable in grid format to place the buttons

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]#gets the button values in the grid
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))#setting the size and frame of the 
                                                                                  #buttons
        
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)#setting text color to black and background to light gray
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)#setting text color to white and background to orange
        else:
            button.config(foreground=color_white, background=color_dark_gray)#setting text color to white and background to dark gray
        
        button.grid(row=row+1, column=column)

frame.pack()

#A+B, A-B, A*B, A/B 
A = "0"#global first operato
operator = None#global operator
B = None#global second operator

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):#this function works when we enter a number it replaces the zero with the entered number
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):#assigning work to each button
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:#complete logic for operating
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)
                
                clear_all()

        elif value in "+-×÷": #500 +, *
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
            
            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)           
        
    else: #digits or .
        if value == ".":
            if value not in label["text"]:
                label["text"] += value

        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value #replace 0
            else:
                label["text"] += value #append digit




window.mainloop()