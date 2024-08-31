# MicroServices Project

This project consists of several microservices implemented using Flask in Python. 
  
1 - Hafez Microservice : Returns a random poem from Hafez  
2 - Khayam Microservice : Returns the current date and time   
3 - QRCode Microservice : Converts text to QR code image adn save it
4 - Main Microservice : Retruns the response from hafez and khayam microservices 

## Running

- To run each microservice 

  - python hafez_micro.py
  - python khayyam_micro.py
  - python main.py
  - python qrcode_micro.py 

- The main microservice will call the Hafez microservice and the Kayyam microservice and get the results, then merge them in json format  
- The QR Code microservice gets the json data from main microservice and finally returns the result image

