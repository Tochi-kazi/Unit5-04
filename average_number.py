# Created by : Tochuhwu Iroakazi
# Created on : Nov 2017
# Created for : ICS3UR
# Daily Assignment - Unit5-04
# This program displays average


import ui
numbers = []

def add_number_touch_up_inside(sender):
    marks = float(view['numbers_textfield'].text)
    
    if marks >= 1 and marks <= 100:
       numbers.append(marks)
       view['show_number_textview'].text = str(numbers)
       view['numbers_textfield'].text = ""
    else:
      view['numbers_textfield'].text = ""

def average(numbers):
    average = int((sum(numbers)/len(numbers) + 0.5))
    return average 
    
def show_average_touch_up_inside(sender):
    total_average = average(numbers)
    view['average_label'].text = 'The average is: ' + str(total_average) + ' %'
    
view = ui.load_view()
view.present('sheet')
