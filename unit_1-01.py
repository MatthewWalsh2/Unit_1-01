#created by Matthew Walsh
#created on:sep 2017
#created for ics3u
#this program displays the school name and mascot

import ui

def mother_teresa_button(sender):
	#display mother teresa and its mascot
	view['school_name_label'].text = 'Mother Teresa HS'
	view['mascot_label'].text = 'Titans'
	
def st_joe_button(sender):
	#displays st joe and its mascot
	view['school_name_label'].text = 'St Joe HS'
	view['mascot_label'].text = 'Jaguars'
	
def st_mark_button(sender):
	#displays st mark and its mascot
	view['school_name_label'].text = 'St Mark HS'
	view['mascot_label'].text = 'Lions'



view = ui.load_view()
view.present('full_screen')
