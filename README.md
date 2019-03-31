# Segura
An application module acting as a bridge between rider and safety.

The module is meant to warn the rider of any sort of wrong-doings that was done due to his ignorance. The project is divided into four parts:

1- Tri-axial balancing- Gyroscope and accelerometer data analysis. 
2- Helmet Tech- Warning the riders to wear their helmet strap.
3- Emergency Module- In-built contact numbers that would aid during an emergency.
4- Tread wear Technology- Sensors that detect the wear in tyres and warn the rider.

#MIT App Inventor 

An open-source web application that was used to design the module, that uses blocks to denote functions.
Version-MIT App Inventor 2, originally provided by Google but now maintained by MIT.

Software requirements-

Windows XP/10/Vista Recommended browser- Chrome or Firefox.

Installing- Installing the App Inventor Setup software package. This step is the same for all Android devices, and the same for Windows XP, Vista, Windows 7, 8.1, and 10. If you choose to use the USB cable to connect to a device, then you'll need to install Windows drivers for your Android phone.

Steps:

Download the installer.
Locate the file MIT_Appinventor_Tools_2.3.0 (~80 MB) in your Downloads file or your Desktop. The location of the download on your computer depends on how your browser is configured.
Open the file.
Click through the steps of the installer. Do not change the installation location but record the installation directory, because you might need it to check drivers later. The directory will differ depending on your version of Windows and whether or not you are logged in as an administrator.
You may be asked if you want to allow a program from an unknown publisher to make changes to this computer. Click yes.

#PhonePi

An application module on the phone which when connected to the laptop/computer via IP address URL provide the data for acceleration, gyroscope, and magnetometer.

Available on Google Play Store. For all Android phones.

#Python Flask

Flask is a microframework for Python based on Werkzeug, Jinja 2.

This server was used to access data from PhonePI. Whenever there is variation in gyroscope or accelerometer values on the phone, the code runs and data that is shown is for all three coordinates. 
The csv_integration.py enables us to save the data in csv format which then can be easily read by the MIT app, the output is in form of a warning which depends on the data provided by the file.

Requirements: Latest version of Python.

#Hardware used

Helmet tech-

A bluetooth module(HC-05) is used to transmit data from helmet to the application by detecting whether the helmet strap is locked or not. Ultrasonic sensors placed in the vehicle detect the presence of rider and only then permit the transfer of rider behaviour data from the helmet.
The code is on Arduino but is saved as .py before uploading.
