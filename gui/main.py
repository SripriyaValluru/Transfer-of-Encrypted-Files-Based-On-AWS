import tkinter
from tkinter import *
import webbrowser
import thrain
import tkinter, tkinter.constants, tkinter.filedialog

'''
-----------------------------------------------------------------
OPEN FILE AND DIRECTORY
-----------------------------------------------------------------
'''
def openfileEnc():
	filename = tkinter.filedialog.askopenfilename(initialdir = "/home/parth/Desktop",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	fileToEncrptyEntryUpdate(filename)

def opendirectoryEnc():
	directory = tkinter.filedialog.askdirectory(initialdir = "/home/parth/Desktop",title = "Select directory")
	destinationFolderEncEntryUpdate(directory)

def openfileDec():
	filename = tkinter.filedialog.askopenfilename(initialdir = "/home/parth/Desktop",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	fileToDecryptEntryUpdate(filename)	
def opendirectoryDec():
	directory = tkinter.filedialog.askdirectory(initialdir = "/home/parth/Desktop",title = "Select directory")
	destinationFolderDecEntryUpdate(directory)
'''
-----------------------------------------------------------------
OPEN SOCIAL LINKS
-----------------------------------------------------------------
'''
def sendfilepage():
	webbrowser.open_new(r"http://127.0.0.1:5000/upload-file")

def recievefilepage():
	webbrowser.open_new(r"http://127.0.0.1:5000/file-directory")

def opengithub(event):
	webbrowser.open_new(r"https://github.com/SripriyaValluru/Secure-text-transfer-using-Diffie-Hellman-key-based-on-cloud")

def opensravslinkedin(event):
	webbrowser.open_new(r"https://www.linkedin.com/in/upparapalli-sravani-59a82415b")

def openshreshtalinkedin(event):
	webbrowser.open_new(r"https://www.linkedin.com/in/padmini-gopisetti-2648851a6")
'''
-----------------------------------------------------------------
UPDATE ENTRY LABELS
-----------------------------------------------------------------
'''
def fileToEncrptyEntryUpdate(filename):
	# Delete old value of entry
	inputEncFileEntry.delete(0,END)
	# Input new value of entry
	inputEncFileEntry.insert(0,filename)
def destinationFolderEncEntryUpdate(directory):
	# Delete old value of entry
	inputEncDirEntry.delete(0,END)
	# Input new value of entry
	inputEncDirEntry.insert(0,directory)
def fileToDecryptEntryUpdate(filename):
	# Delete old value of entry
	outputDecFileEntry.delete(0,END)
	# Input new value of entry
	outputDecFileEntry.insert(0,filename)
def destinationFolderDecEntryUpdate(directory):
	# Delete old value of entry
	outputDecDirEntry.delete(0,END)
	# Input new value of entry
	outputDecDirEntry.insert(0,directory)
'''
-----------------------------------------------------------------
ENCRYPT-DECRYPT TRIGGER BUTTON
-----------------------------------------------------------------
'''
def encryptor():
	EncryptBTN.config(state="disabled")
	public_key = publicKeyOfRecieverEntry.get()
	private_key = privateKeyOfSenderEntry.get()
	directory = inputEncDirEntry.get()
	filename = inputEncFileEntry.get()
	thrain.encrypt(filename,directory,public_key,private_key)

def decryptor():
	DecryptBTN.config(state="disabled")
	public_key = publicKeyOfSenderEntry.get()
	private_key = privateKeyOfRecieverEntry.get()
	directory = outputDecDirEntry.get()
	filename = outputDecFileEntry.get()
	thrain.decrypt(filename,directory,public_key,private_key)

def main():

	global filename
	global directory

	filename = ""
	directory = ""

	# Attributes of main dialog box
	global form
	form = tkinter.Tk()
	form.wm_title('CYBER SECURITY')
	'''
	-------------------------------------------------------------
	Form Label Configuration
	-------------------------------------------------------------
	'''
	EncryptStep = LabelFrame(form, text="File Encryption: ")
	EncryptStep.grid(row=0, columnspan=7, sticky='W', \
		padx=5, pady=5, ipadx=5, ipady=5)	

	DecryptStep = LabelFrame(form, text="File Decryption: ")
	DecryptStep.grid(row=2, columnspan=7, sticky='W', \
    	             padx=5, pady=5, ipadx=5, ipady=5)

	Aboutus = LabelFrame(form, text=" About Us ")
	Aboutus.grid(row=0, column=9, columnspan=2, rowspan=8, \
		sticky='NS', padx=5, pady=5)
	'''
	-------------------------------------------------------------
	Menu Bar
	-------------------------------------------------------------
	'''
	menu = Menu(form)
	form.config(menu=menu)

	menufile = Menu(menu)
	menufile.add_command(label = 'Send file', command = lambda:sendfilepage())
	menufile.add_command(label = 'Recieve file', command = lambda:recievefilepage())
	menufile.add_command(label = 'Exit', command = lambda:exit())
	menu.add_cascade(label = 'Menu', menu = menufile)
	'''
	-------------------------------------------------------------
	ENCRYPT-SECTION
	-------------------------------------------------------------
	'''
	global inputEncFileEntry
	global inputEncDirEntry
	global publicKeyOfRecieverEntry
	global privateKeyOfSenderEntry

	global EncryptBTN

	#-------------------------Select a file----------------------
	inputEncFile = Label(EncryptStep, text="Select the File:")
	inputEncFile.grid(row=0, column=0, sticky='E', padx=5, pady=2)

	inputEncFileEntry = Entry(EncryptStep)
	inputEncFileEntry.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

	inputEncBtn = Button(EncryptStep, text="Browse ...", command = openfileEnc)
	inputEncBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)
	#-------------------------Save file to ----------------------
	inputEncDir = Label(EncryptStep, text="Save File to:")
	inputEncDir.grid(row=1, column=0, sticky='E', padx=5, pady=2)

	inputEncDirEntry = Entry(EncryptStep)
	inputEncDirEntry.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

	inputEncDirBtn = Button(EncryptStep, text="Browse ...", command = opendirectoryEnc)
	inputEncDirBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)
	#-------------------------Public Key-------------------------
	publicKeyOfReciever = Label(EncryptStep, text="Public-Key of reciever:")
	publicKeyOfReciever.grid(row=2, column=0, sticky='E', padx=5, pady=2)

	publicKeyOfRecieverEntry = Entry(EncryptStep)
	publicKeyOfRecieverEntry.grid(row=2, column=1, sticky='E', pady=2)
	#-------------------------Private Key------------------------
	privateKeyOfSender = Label(EncryptStep, text="Private-Key of sender:")
	privateKeyOfSender.grid(row=2, column=5, padx=5, pady=2)

	privateKeyOfSenderEntry = Entry(EncryptStep)
	privateKeyOfSenderEntry.grid(row=2, column=7, pady=2)
	#-------------------------Encrypt Button---------------------
	EncryptBTN = tkinter.Button(EncryptStep, text="Encrypt   ", command=encryptor)
	EncryptBTN.grid(row=2, column=8, sticky='W', padx=5, pady=2)
	'''
	-------------------------------------------------------------
	DECRYPT-SECTION
	-------------------------------------------------------------
	'''
	global outputDecFileEntry
	global outputDecDirEntry
	global publicKeyOfSenderEntry
	global privateKeyOfRecieverEntry

	global DecryptBTN
	#-------------------------Select a file----------------------
	outputDecFile = Label(DecryptStep, text="Select the File:")
	outputDecFile.grid(row=0, column=0, sticky='E', padx=5, pady=2)

	outputDecFileEntry = Entry(DecryptStep)
	outputDecFileEntry.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

	outputDecBtn = Button(DecryptStep, text="Browse ...", command = openfileDec)
	outputDecBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)
	#-------------------------Save file to ----------------------
	outputDecDir = Label(DecryptStep, text="Save File to:")
	outputDecDir.grid(row=1, column=0, sticky='E', padx=5, pady=2)

	outputDecDirEntry = Entry(DecryptStep)
	outputDecDirEntry.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

	outputDecDirBtn = Button(DecryptStep, text="Browse ...", command = opendirectoryDec)
	outputDecDirBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)
	#-------------------------Public Key-------------------------
	publicKeyOfSender = Label(DecryptStep, text="Public-Key of sender:")
	publicKeyOfSender.grid(row=2, column=0, sticky='E', padx=5, pady=2)

	publicKeyOfSenderEntry = Entry(DecryptStep)
	publicKeyOfSenderEntry.grid(row=2, column=1, sticky='E', pady=2)
	#-------------------------Private Key------------------------
	privateKeyOfReciever = Label(DecryptStep, text="Private-Key of reciever:")
	privateKeyOfReciever.grid(row=2, column=5, padx=5, pady=2)

	privateKeyOfRecieverEntry = Entry(DecryptStep)
	privateKeyOfRecieverEntry.grid(row=2, column=7, pady=2)
	#-------------------------Decrypt Button---------------------
	DecryptBTN = tkinter.Button(DecryptStep, text="Decrypt   ", command = decryptor)
	DecryptBTN.grid(row=2, column=8, sticky='W', padx=5, pady=2)
	'''
	-------------------------------------------------------------
	ABOUTUS-SECTION
	-------------------------------------------------------------
	'''	
	intro = Label(Aboutus, text="\nCYBER SECURITY")
	intro.grid(row=0)
	text1 = Label(Aboutus, text="\nTRANSFER OF ENCRYPTED FILES BASED ON AWS\n")
	text1.grid(row=1)
	githublink = Label(Aboutus, text="Go to our Github Repo", fg="blue", cursor="hand2")
	githublink.bind("<Button-1>", opengithub)
	githublink.grid(row=2)
	# Add more content and remove padding newline accordingly
	padding = Label(Aboutus, text="\n\n\n\n")
	padding.grid(row=3)
	text2 = Label(Aboutus, text="Contributed by: ")
	text2.grid(row=4, sticky='S')
	priyasocial = Label(Aboutus, text="Sravani | Shreshta |")
	priyasocial.bind("<Button-1>",opensravslinkedin)
	priyasocial.grid(row=5, sticky='SW',padx = 8)
	#text3 = Label(Aboutus, text="Shreshta |")
	#text3.grid(row=5)
	parthsocial = Label(Aboutus, text="Gopi Chandhan |  Sri Priya")
	parthsocial.bind("<Button-1>",openshreshtalinkedin)
	parthsocial.grid(row=5, sticky='SE',padx = 8)
    


	form.mainloop()

if __name__ == "__main__":
	main()
