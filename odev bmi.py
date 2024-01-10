from tkinter import *
window = Tk()
window.title("BMI CALCULATOR")
window.minsize(width=300,height=200)

#Labels
my_label1 =Label(text="BMI Calculator",font=("ariel",20,"italic"))
my_label1.config(fg="white")
my_label1.pack()

my_label2 =Label(text="What is your weight?",font=("ariel",13,"italic"))
my_label2.config(fg="white")
my_label2.place(x=1,y=50)

my_label3 =Label(text="How tall are you?",font=("ariel",13,"italic"))
my_label3.config(fg="white")
my_label3.place(x=1,y=70)


#entrys
my_entry =Entry(width=15)
my_entry.place(x=145 ,y=50)

my_entry2 = Entry(width=15)
my_entry2.place(x=145 ,y=70)

#Button
def calculator_bmi():
    weight_input =my_entry.get()
    tall_input = my_entry2.get()
    if weight_input and tall_input :
        weight_bmi =float(my_entry.get())
        tall_bmi = float(my_entry2.get())
        bmi_calculator =weight_bmi/((tall_bmi/100)*(tall_bmi/100))
        if bmi_calculator <= 18.5:
            my_label4.config(text=f"BMI:{bmi_calculator:.2f} Weak")
        elif bmi_calculator > 18.5 and bmi_calculator <= 25 :
            my_label4.config(text=f"BMI:{bmi_calculator:.2f} Normal")
        elif bmi_calculator > 25 and bmi_calculator <= 30:
            my_label4.config(text=f"BMI:{bmi_calculator:.2f} Excess weight")
        elif (bmi_calculator > 30 and bmi_calculator <= 35):
            my_label4.config(text=f"BMI:{bmi_calculator:.2f} 1. Extremely obese")
        elif bmi_calculator > 35 and bmi_calculator <= 40:
            my_label4.config(text=f"BMI:{bmi_calculator:.2f} 2. Extremely obese")
        else:
            my_label4.config(text=f"BMI:{bmi_calculator:.2f} Morbid obese")
    else:
     my_label4.config(text="please enter the value")
def   check_button():

    print("button actief")
    print(bmi_calculator)
my_label4=Label(text=calculator_bmi,font=("ariel",13,"italic"))
my_label4.config(fg="white")
my_label4.place(x=50,y=130)
my_button = Button(window,text="Calculator",bg='green',fg="blue",width=10,command=calculator_bmi)
my_button.place(x=100 ,y=100)

window.mainloop()

