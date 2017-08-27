#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '' # Get local machine name
port = 3000            # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

                # Now wait for client connection.
while True:
   s.listen(5) 
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   while True:
	   chat = c.recv(1024)
	   print "Client: "+chat
	   if chat == "exit":
	   	 	print c.recv(1024)
	   	 	c.send('bye')
	   		s.close() 
	   else:
	   		text = raw_input("Server: ")
	   		c.send(text)