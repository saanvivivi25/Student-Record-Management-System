Student Record Management System
This project is a Python-based menu-driven application designed to manage student records efficiently. The system allows users to add student details, view all stored records, identify the highest-scoring student, calculate the class average, and exit the application through a simple interactive menu. The program continues running until the user explicitly selects the Exit option, making it a practical example of a continuous menu-driven system.
The application stores student information using a list of dictionaries. Each dictionary represents a single student record containing the student's name and marks, while the list stores multiple student records. This approach provides a structured and scalable way to organize and manage data.
The project is divided into multiple functions, each responsible for a specific task. Functions are used to add students, display student records, find the highest-scoring student, calculate the class average, and display the menu. This modular approach improves code readability, maintainability, and reusability.
A while loop is used to display the menu repeatedly until the user chooses to exit the program. The loop ensures continuous interaction with the user and demonstrates the implementation of menu-driven applications. A for loop is used whenever the program needs to traverse all student records, such as displaying student details, finding the highest score, or calculating the class average.
The program uses conditional statements (if, elif, and else) to process user choices, validate marks, and determine the appropriate action based on the selected menu option. Input validation ensures that marks entered by the user are within the valid range of 0 to 100.
To improve reliability, exception handling is implemented using try-except blocks. This prevents the program from crashing when users enter invalid data, such as text instead of numbers. If invalid input is detected, an appropriate error message is displayed, and the user is prompted to enter the data again.
The project also demonstrates the use of break statements to terminate loops when required. The menu loop ends only when the user selects the Exit option, while the marks validation loop stops once valid marks are entered.

Features
•	Add new student records. 
•	Store student information using a list of dictionaries. 
•	View all student records. 
•	Find the highest-scoring student in the class. 
•	Calculate the class average. 
•	Validate marks to ensure they are numeric and between 0 and 100. 
•	Handle invalid input using exception handling. 
•	Continuous menu-driven interface. 
•	Exit the application safely using the Exit option. 

Concepts and Technologies Used
•	Functions 
•	Lists 
•	Dictionaries 
•	For Loops 
•	While Loops 
•	Conditional Statements (if, elif, else) 
•	Exception Handling (try, except) 
•	Break Statements 
•	Input Validation 
•	Menu-Driven Programming 
•	Data Storage and Retrieval 

Conclusion
The Student Record Management System is a beginner-friendly Python project that combines multiple core programming concepts into a single application. It provides hands-on experience with data storage, retrieval, validation, and menu-driven program design while demonstrating how functions, loops, dictionaries, and exception handling work together to build a complete and interactive software solution.

