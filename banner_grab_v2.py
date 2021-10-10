#! /usr/bin/python3

"""Python script that loops for a list of specified ports and grabs the banner information for each port."""
import socket  # Imports the module socket

Ports = [21, 22, 25, 3306]

for port in Ports:
    s = socket.socket()  # Creates an object to initiate an object from the socket class
    print("This is the banner for the port ")
    print(port)

    s.connect((" ", port))  # Takes the function connect from the module this allows the program to open a network
    # connection

    answer = s.recv(1024)  # Receives 1024 bytes of data from the connection in s.connect and stores them
    # This 1024 bytes is the banner information

    print(answer)  # Prints the banner information

    s.close()  # Closes the network connection
