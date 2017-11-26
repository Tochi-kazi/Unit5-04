# Created by : Sidney Kang
# Created on : 18 Nov. 2017
# Created for : ICS3UR
# Daily Assignment - Unit5-04
# This program

import ui
marks = []
number_of_numbers = 0

def enter_mark(sender):  
	
    mark_entered = float(view['marks_textbox'].text)
    
    if mark_entered > 100 or mark_entered < 0:
       view['marks_textbox'].text = ""
       view['condition_label'].text = "Please enter any mark between 0-100. "
    else:       
       marks.append(mark_entered)                         
       view['show_marks_textview'].text = str(marks) 
       view['marks_textbox'].text = ""

def calculate_average(marks):
    
    average = int((sum(marks)/len(marks) + 0.5))
   
    return average
            
def show_average(sender):
	
    calculate_average(marks)
    
    final_average = calculate_average(marks)
    
    view['show_final_average_label'].text = "The average is: " + str(final_average)	+ "%"   
    
view = ui.load_view()
view.present('sheet')


