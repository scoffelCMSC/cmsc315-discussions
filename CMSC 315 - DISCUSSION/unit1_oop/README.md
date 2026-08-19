# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Approach

For this assignment I made a parent class ModelTrainTest to show some potential route data for model trains. I needed this to give me information on the engine, car number, simulated passengers, and travel time. The child class Detours shows some potential alterations one could make mid-route to the train's pathing. This serves me more as practice for a future project that I am working on at home with an actual setup much further down the line when me and my father intend to switch our cars from entirely manual to partially automated. I have worked with abstraction before in Java and very lightly in Python, so returning to it was a good challenge especially with the differences between both languages and my time away from Python. Before I got to pseudocode I made myself a list of things I wanted to functionally accomplish, moving to a UML diagram first to have a closer visualization of what I set out to achieve. Using child classes like I did wih Detour made it very clear to me again the importance of encapsulation. This separate class doesn't need to repeat the work of its parent, and keeping main data within the parent file would allow me to add additional child classes onto it without messing with the existing Detour class.

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class
 ModelTrainTest, with variables for the engine type, passenger count, car count, and estimated run duration and a class variable called railway for which rail it would run on- in this case, the passenger rail.
2. Create a child class using inheritance
 Detour is a child class of ModelTrainTest that inherits variables from its parent class and adds variables for an estimated delay, number of detour stops, and a list of the stop names.
3. Demonstrate class and instance namespaces
 The objects detour1 and detour2 were defined under the demonstrate_namespace() function to print the necessary information about the namespace. 
4. Demonstrate shallow and deep copying
 A shallow and deep copy of the alternative stops in the child class was created to showcase the differences by displaying the different stops that the detoured train would take under the defined demonstrate_copying(). The original is initialized, then the shallow and deep copy are created. The shallow copy demonstrates a new item not being present in the deep copy's list, whilst being present in the shallow copy's due to the original data being modified. Both are explained briefly using comments within the code. The original, copy, and shallow copy are displayed.
5. Create and test objects in `main()`
Both parent and child class were given test objects to fill each variable and display them as needed, the overrides for the child class, and displaying the requested demonstrations.
6. Add a student-created extension
I created a boolean check within the parent class using an if/else statement so that if the engine or car was supposed to have maintenance it would display that the tested engine is not ready to go on the rail for the test. 

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
I was able to refresh myself on Python's flow and language, which I had not had practice with in a long time. I had not yet before encountered copying in python, and learning how to apply it was a good challenge; I learned more by practicing with it than reading it, as it threw me off somewhat the first time. I have also never made my own repository on GitHub, which I think is a very important thing to learn how to do in CS related fields. 
2. What challenges did you encounter, and how did you overcome them?
My main challenge was relearning how to use Python, which at the time I hadn't had time to go through the refresher section in our texts. In order to do this, I mostly referenced to my own previous work in Java to remember the workflow. Creating UML and pseudocode helped me significantly visualize what I needed, and going through the lab first helped solidify my skills further.
3. Compare OOP to procedural programming.
Procedural programming takes a more linear approach. It's an instruction book that is meant to be started at page one and proceed forward up those pages with how functions operate within a procedural language. Object  oriented programming is as if your instruction book instead had separate sections you could choose to do, but still reach the same end result. The objects in OOP are more relational to one another and their attributes in a less linear fashion.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.
Maintainability and reusability allow one to more easily expand upon an existing program with relative ease, even if they were not the ones to originally create the program. Maintainability specifically allows a program to be easily debugged, and reusability helps reduce overhead by not having the user remake existing variables from scratch when one can call on the main class.