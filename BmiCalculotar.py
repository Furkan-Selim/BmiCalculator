from tkinter import *
from tkinter import messagebox


def click_button():
    user_input = my_entry.get()
    user_input_2 = my_entry_2.get()
    print(user_input, user_input_2)

def get_height():
    height = float(my_entry_2.get())
    return height

def get_weight():
    weight = float(my_entry.get())
    return weight

def calculate_bmi(a=""):
    print(a)

    try:
        heigt = get_height()
        weight = get_weight()
        heigt = heigt / 100.0
        bmi = weight / (heigt ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res = "Your BMİ is" + str(bmi) + "\nRemarks: Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)


window = Tk()
window.bind("<Return>", calculate_bmi)
window.title("BMI Calculator")
window.minsize(width=350, height= 250)

my_label= Label(text="Enter Your Weight (kg)", font=('Arial', 10, "normal"))
my_label.config(padx=10,pady=20)
my_label.pack()

my_entry = Entry(width=15)
my_entry.pack()
my_entry.focus()


my_label2 = Label(text="Enter Your Height (cm)", font=('Arial', 10, "normal"))
my_label2.config(padx=0,pady=20)
my_label2.pack()

my_entry_2 = Entry(width=15)
my_entry_2.pack()
my_entry_2.focus()


my_button = Button(text="Calculate", bg="white", width=10, command=calculate_bmi)
my_button.pack()

click_button()

window.mainloop()