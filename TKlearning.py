import tkinter
#window
window = tkinter.Tk()
#window.config(bg="white")
window.title("BMI Calculator")
window.config(padx=30,pady=30)
window.minsize(250,250)
#weight_label
weight_input_label = tkinter.Label(text="Enter your weight(kg)")
weight_input_label.pack()
#weight_entry
weight_input_entry = tkinter.Entry()
weight_input_entry.config(width=10)
weight_input_entry.pack()
#height_label
height_input_label = tkinter.Label(text="Enter your height(cm)")
height_input_label.pack()
#height_entry
height_input_entry = tkinter.Entry()
height_input_entry.config(width=10)
height_input_entry.pack()
#function_BMI
def calculate_BMI():
    height = height_input_entry.get()
    weight = weight_input_entry.get()
    if height == "" or weight == "" :
        result_label.config(text="Enter both weight or height!")
    else:
        try:
            bmi = float(weight) / (float(height)/100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=f"Your bmi : {result_string}")
        except:
            result_label.config(text="Enter a valid number")
#calculate_button
calculate_button =tkinter.Button(text="Calculate",command=calculate_BMI)
calculate_button.pack()
#result_label
result_label = tkinter.Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is : {bmi}.You are "
    if bmi<=16:
        result_string += "severely thin!"
    elif bmi> 16 and bmi<=17:
        result_string += "moderately thin!"
    elif bmi > 17 and bmi <= 18.5:
        result_string += "mild thin!"
    elif bmi > 18.5 and bmi <= 25:
        result_string += "normal!"
    elif bmi > 25 and bmi <= 30:
        result_string += "over weight!"
    elif bmi > 30 and bmi <= 35:
        result_string += "obese class 1!"
    elif bmi > 35 and bmi <= 40:
        result_string += "obese class 2!"
    else:
        result_string += "obese class 3!"

    return result_string



window.mainloop()