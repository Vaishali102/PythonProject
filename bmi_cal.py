import eel


eel.init(".")

# Exposing the bmi_calculator function to javascript
@eel.expose
def bmi_calculator(height,  weight): 
     if height !="":
          if weight !="":
               bmi = int(weight)/((int(height)/100)**2)
               if bmi <18.5:
                    return "Your BMI IS " +format(bmi, ".1f")+" (Underweight)"
               elif bmi >19 and bmi <24.9:
                    return "Your BMI IS " +format(bmi, ".1f")+" (Normal)"
               elif bmi >25 and bmi <29.9:
                    return "Your BMI IS " +format(bmi, ".1f")+" (Overweight)"
               elif bmi >30 and bmi <200:
                    return "Your BMI IS " +format(bmi, ".1f")+" (Obesity)"
               else:
                    return "Something went wrong!"
          else:
               return "Weight is empty!"
     else:
               return "Height is empty!"


# Start the index.html file
eel.start("main.html", size=(800,600))