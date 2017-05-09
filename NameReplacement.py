# Written By. Eun-Sol Kim
# If Filename does not start with 'fromWhatName',
# then change the name to 'toWhatNameReplace'.
# fileDirect: should contain exact directory for that folder
import glob, os
from Tkinter import *
import collections

fileDirect = "/Users/eun-solkim/BBox-Label-Tool-master/"
fromWhatName = "DonotEnter"
toWhatNameReplace = ""
toWhichFormat = "JPEG"

class GUIdisplay:
	def __init__(self, Parent):
		self.myParent = Parent
		self.myParent.geometry('550x240')
		self.myParent.title("Name & Format converter")

		self.UI_Width = 20

		self.Title_Frame = Frame(self.myParent)
		self.Title_Frame.pack(side=TOP, fill=X)
		self.Title_Label = Label(self.Title_Frame, text="Please enter valid information")
		self.Title_Label.pack(side=LEFT, fill=X)
		self.createRadioButton(["Convert only Format", "Convert only Name", "Convert both"], [1,2,3])
		self.createUserInputForm(["Folder Directory", "From what name", "To what name", "From which format", "To which format"])
		self.createEnterButton()

	def createRadioButton(self, radioList, valueList):
		self.whichType = IntVar()
		radioRow_Frame = Frame(self.myParent)
		radioRow_Frame.pack(side=TOP, fill=X)
		radioLabel_Label = Label(radioRow_Frame,text="Select test type:      ", anchor='w')
		radioLabel_Label.pack(side=LEFT)
		for radioText,valueText in zip(radioList, valueList):
			radioButton_Button = Radiobutton(radioRow_Frame, text=radioText, variable=self.whichType, value=valueText)
			radioButton_Button.pack(side=LEFT)

	def createUserInputForm(self, inputLabel):
		self.fields=[]
		for i in inputLabel:
			userInputRow_Frame = Frame(self.myParent)
			userInputLabel_Label = Label(userInputRow_Frame, width = 15, text=i, anchor=SW)
			userInputEntry_Entry = Entry(userInputRow_Frame)
			userInputRow_Frame.pack(side=TOP,fill=X)
			userInputLabel_Label.pack(side=LEFT)
			userInputEntry_Entry.pack(side=RIGHT, expand=YES, fill=X)
			self.fields.append(userInputEntry_Entry)

	def getUserInputInfo(self):
		value = []
		for f in self.fields:
			value.append(f.get())
		self.userInfo = collections.OrderedDict(zip(self.fields, value))
		del self.fields, value
		
	def createEnterButton(self):
		enterRow_Frame = Button(self.myParent, text="Enter", command=self.getUserInputInfo)
		enterRow_Frame.pack(side=RIGHT)



	def convert(self):
		i = 0
		for filename in os.listdir(fileDirect):
			if filename != ".DS_Store":
				if not (filename.startswith(fromWhatName)):
					os.rename(fileDirect + "%s" %(filename), fileDirect + toWhatNameReplace + "%d.%s" % (i,toWhichFormat))
			i += 1

root = Tk()
display = GUIdisplay(root)
root.mainloop()


