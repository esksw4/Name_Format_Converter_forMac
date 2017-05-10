# Written By. Eun-Sol Kim
# If Filename does not start with 'fromWhatName',
# then change the name to 'toWhatNameReplace'.
# fileDirect: should contain exact directory for that folder
import glob, os
from tkinter import *
import tkinter
import collections
import colorama

class GUIdisplay:
	def __init__(self, Parent):
		self.myParent = Parent
		self.myParent.geometry('550x200')
		self.myParent.title("Name & Format converter")

		self.UI_Width = 20
		self.inputLabel = ["Folder Directory", "To what name", "To which format"]
		self.fileName = []
		self.allFieldCheck = None

		self.Title_Frame = Frame(self.myParent)
		self.Title_Frame.pack(side=TOP, fill=X)
		self.Title_Label = Label(self.Title_Frame, text="Please enter valid information", font=("Courier",20))
		self.Title_Label.pack(side=LEFT, fill=X)

		self.error_Frame = Frame(self.myParent)
		self.error_Frame.pack(side=TOP)
		self.error_Label = Label(self.error_Frame)
		self.error_Label.pack()
		self.error_Label.exist = False

		self.createRadioButton(["Convert only Format", "Convert only Name", "Convert both"],[1,2,3])
		self.createUserInputForm()
		self.createEnterButton()

	def userInputFieldCheck(self):
		if len([v for v in self.userInfo.values() if v == '']) > 0 or (self.whichType.get() == 10):
				return False
		return True

	def displayErrorMessage(self, txt):
		if self.allFieldCheck == False:
			if self.error_Label.exist == False:
				self.error_Label.config(text=txt, fg='red')
				self.error_Label.pack(side=TOP)
				self.error_Label.exist = True
			else:
				self.error_Label.pack_forget()
				self.error_Label.config(text=txt, fg='red')
				self.error_Label.pack(side=TOP)
		else:
			if self.error_Label.exist == True:
				self.error_Label.pack_forget()
				self.error_Frame.pack_forget()
			if self.whichType.get() == 1: # Convert only Format
				self.convertFormat()
			elif self.whichType.get() == 2: # Convert only Name
				self.convertName()
			else: #Convert Both
				self.convertBoth()

	def createRadioButton(self, radioList, valueList):
		self.whichType = IntVar(value=10)
		radioRow_Frame = Frame(self.myParent)
		radioRow_Frame.pack(side=TOP, fill=X)
		radioLabel_Label = Label(radioRow_Frame,text="Select test type:      ", anchor='w')
		radioLabel_Label.pack(side=LEFT)
		for radioText,valueText in zip(radioList, valueList):
			radioButton_Button = Radiobutton(radioRow_Frame, text=radioText, variable=self.whichType, value=valueText)
			radioButton_Button.pack(side=LEFT)

	def createUserInputForm(self):
		self.fields=[]
		for i in self.inputLabel:
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
		self.userInfo = collections.OrderedDict(zip(self.inputLabel, value))
		del value

		if not self.userInfo['Folder Directory'].endswith('/'):
				self.userInfo['Folder Directory'] += str('/')
		if not self.userInfo['To which format'].startswith('.'):
			self.userInfo['To which format'] = str('.') + self.userInfo['To which format']

		try: 
			self.fileName = os.listdir(self.userInfo['Folder Directory'])
		except:
			self.allFieldCheck = False
			self.displayErrorMessage("Please provide valid directory")

		
		if not (self.fileName == []):
			self.allFieldCheck = self.userInputFieldCheck()
			self.displayErrorMessage("Please fill out all entries.")

	def createEnterButton(self):
		enterRow_Frame = Button(self.myParent, text="Enter", command=self.getUserInputInfo)
		enterRow_Frame.pack(side=RIGHT)

	def convertFormat(self):
		for filename in os.listdir(self.userInfo['Folder Directory']):
			if (not (filename.startswith("----________-----")) and filename != ".DS_Store"):
				Name = filename.split('.')[0]
				os.rename(self.userInfo['Folder Directory'] + "%s" %(filename), self.userInfo['Folder Directory']  + Name + ".%s" %(self.userInfo['To which format']))
	

	def convertName(self):
		for filename in os.listdir(self.userInfo['Folder Directory']):
			if (not (filename.startswith("----________-----")) and filename != ".DS_Store"):
				Format = filename.split('.')[1]
				os.rename(self.userInfo['Folder Directory'] + "%s" %(filename), self.userInfo['Folder Directory']  + self.userInfo['To what name'] + "%d%s" %(i,Format))
			i += 1

	def convertBoth(self):
		i = 0
		for filename in os.listdir(self.userInfo['Folder Directory']):
			if (not (filename.startswith("----________-----")) and filename != ".DS_Store"):
				os.rename(self.userInfo['Folder Directory'] + "%s" %(filename), self.userInfo['Folder Directory']  + self.userInfo['To what name'] + "%d%s" % (i,self.userInfo['To which format']))
			i += 1

# fileDirect = "/Users/eun-solkim/BBox-Label-Tool-master/"
# fromWhatName = "DonotEnter"
# toWhatNameReplace = ""
# toWhichFormat = "JPEG"

root = Tk()
display = GUIdisplay(root)
root.mainloop()


