Prog day service

Service for getting the 256th day of input year

Input date format:

Y - year number, 4 digits (Examples: 1999, 2007)

Example: http://localhost/?year=2019

    {"errorCode": 200, "dataMessage": "13/9/2019"}
    
Run:


☻ git clone https://github.com/KiriII/Flex.git


☻ gradle startService


Errors:

☻ No date:

    ☺ Example: http://localhost/?map=2019
    
     {"errorCode": 27, "dataMessage": "There is no date"}
     
☻ Error in date format:

    ☺ Example: http://localhost/?year=999 or http://localhost/?year=14888
    
    {"errorCode": 54, "dataMessage": "error in date format"}
