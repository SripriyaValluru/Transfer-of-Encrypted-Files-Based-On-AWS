# Tranfer of Encrypted Files based on AWS

##### Dependencies and Tools

Software: Python3
```
For GUI:
pip install secretsharing
pip install tkinter
pip install pycryptodome
pip install hashlib
pip install webbrowser

For Web Application:
pip install flask
```

#### To run the GUI:
```
Go to gui: cd gui
For Windows: python main.py
For linux: python3 main.py
```
### To run the web application:
```
It works only on Linux as we have used AWS EC2 LINUX machine.
Go to linux machine:
Go to web-app: cd web-app
command: python app.py
Open the port.
```
## PROJECT

This implementation can be explained in two parts
* stand-alone-application
* web-application

### Standalone-application

![stand-alone-application](/web-app/static/cybergui.gif)

* This portion deals with encryption and decryption of file
* The file is encrypted using AES algorithm
* *Menu* option also helps to toggle the menu to upload and download files</br></br>

### Web-application
![web-application](/web-app/static/webapp.png)


Once file is encrypted it has to be uploaded on an online directory. Another directory is needed where public-key of all the users is stored. Thus, we built an online directory and hosted it on cloud. The unique thing about hosting is that dynamic files are being generated while adding a new user or uploading a text file. Thus, we needed a cloud service which could run the program and incorporate the dynamic files. 

### Hosting on AWS

* Fork this repository
* create an amazon EC2 instance.
* Select and create **Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type**
* While creating the machine, toggle to menu *Configure Security Group* menu.
* Here, enable port SSH, HTTP, RDP and in port, change *Source* to **Anywhere**
* Download and keep the **publicKeyPair.pem file**
* Install *putty* and *puttygen*
* Open puttygen, select the publicKeyPair.pem and generate a private key. Now, save it as **Save private key**
* Open the AWS machine dashboard ad copy the *IPv4 Public IP* of the instance created
* Open putty
* In putty, copy the IP in *Host Name(or IP address)*
* In putty, toggle the SSH>Auth and here, select the *private key* you generated.
* Click open and voila! The terminal of instance opens
-----------------------------------------------------
* Enter "login as:" ec2-user
* Enter following command
* $sudo bash
* $yum install python-pip
* $yum install git
* $pip install flask
* Now, clone the forked repository on local machine
* In web-app/app.py, comment on line 169 and uncomment line 168
* Update the github repository
* On the terminal of instance, clone the repository and enter command
* $python app.py

