#Import the tkinter library
from tkinter import *
#import datetime library
import datetime

def refresh_times():
	#starting times
	time_start = [0,50,100,150,200,250,300]

	#origin date, just a day in the past were the event started at 0000
	origin = 738484

	#todays date converted to gregorian
	today = datetime.datetime.now().toordinal()
    
	choice_zone = time_zone.get()

	match choice_zone:
		case 'EST':
			pass
		case 'CST':
			today = today-2
		case 'MST':
			today = today+3
		case 'PST':
			today = today+1
		case 'AK':
			today = today-1
		case 'HAST':
			today = today-3

	#doing the maths
	position = (today-origin)%7

	#enable text boxes for clearing/adding times
	today_entry.config(state='normal')
	tom_entry.config(state='normal')

	today_entry.tag_configure("center", justify='center')
	tom_entry.tag_configure("center", justify='center')
	today_entry.tag_add('center','1.0','end')

	#clear out text boxes
	today_entry.delete('1.0','end')
	tom_entry.delete('1.0','end')

	#while loop to fill in todays soup times
	i=0
	while (time_start[position] +(i*350)) < 2400:
		temp = str(time_start[position]+(i*350)).zfill(4)
		if temp[2]==str(5):
			temp=list(temp)
			temp[2]= '3'
			temp=''.join(temp)
		today_entry.insert(INSERT,str(temp)+'\n')
		i += 1

	#setting up logic for the next day
	position = 0 if position==6 else position+1

	#while loop to fill in tomorrows soup times
	i=0
	while (time_start[position] +(i*350)) < 2400:
		temp = str(time_start[position]+(i*350)).zfill(4)
		if temp[2]==str(5):
			temp=list(temp)
			temp[2]= '3'
			temp=''.join(temp)
		tom_entry.insert(INSERT,str(temp)+'\n')
		i += 1

	#make it look pretty, ie. center justify
	today_entry.tag_add('center','1.0','end')
	tom_entry.tag_add('center','1.0','end')

	#disable text boxes again
	today_entry.configure(state='disabled')
	tom_entry.configure(state='disabled')


#Create an instance of tkinter frame
win = Tk()

#Set the Title 
win.title("Yes Chef!")

#Set the geometry
win.geometry("300x238")

#Make the window resizable false
win.resizable(False,False)

time_zone = StringVar()

options = [
	'EST',
	'CST',
	'MST',
	'PST',
	'AK',
	'HAST'
]

time_zone.set('EST')

main_frame = Frame(win)

time_drop = OptionMenu(main_frame,time_zone,*options)
time_drop.config(width=4)
time_drop.pack(side=RIGHT, anchor=NE)

main_label = Label(main_frame, text= "Soup Times", font=('Times New Roman bold',20))
main_label.pack(side=TOP, expand=1)

main_frame.pack(fill=X)

date_frame = Frame(win)
today_label = Label(date_frame,text="Today", font=('Times New Roman bold',14))
today_label.pack(side=LEFT,expand=True)

tom_label = Label(date_frame,text="Tomorrow", font=('Times New Roman bold',14))
tom_label.pack(side=LEFT,expand=True)
date_frame.pack(fill=X)

times_frame = Frame(win)
today_entry = Text(times_frame,width=12,height=7,state='disabled')

today_entry.pack(side=LEFT,expand=True)
tom_entry = Text(times_frame,width=12,height=7,state='disabled')

tom_entry.pack(side=LEFT,expand=True)
times_frame.pack(fill=X)

refresh_button = Button(win, padx=8, text='Refresh', command= refresh_times,font=('Times New Roman bold',12))
refresh_button.pack(side=TOP, pady=15)


win.mainloop()