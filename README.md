# Interaction Lab Robotic Tour Guide
Goal: We want a program that we can run when we have a lab tour group come in. A robot will move around the lab and introduce all of the Ph.D. Students to people who want to tour the lab.

Motivation: Since we are a human-robot interaction robotics lab, we should have a robot interaction for people who come to visit. By having a robot, we can help inspire people who come to visit our lab to enter the field of robotics.

Anticipated Approach: We can use the Astro robot to move around the room. Previously, we programmed the robot using Alexa skills, but Alexa skills are limited in what they can do. Instead, we can use text-to-speech to issue commands to the robot and use a blossom robot to have more fine-grained control over what happens during the interaction.

# Getting Started
In the 'src' folder run

`python3 astro_statemachine.py`

to begin the Astro Interaction Lab Tour. The program will start outputting audio of the intro, go-to commands, Ph.D. student descriptions about their research, and an outro. Audio can be emitted from a Bluetooth speaker, to allow Astro to hear the next go-to command on the go. When Astro has reached the next stop on the lab tour, the user will be prompted via the terminal to answer whether Astro has finished moving. If the answer is yes, then the user will prompted again to confirm if a person is present to talk. If the answer is no, then Astro will play an audio file explaining the current Ph.D. student's research. If the answer is yes, the user will be prompted one more time to confirm if the person present is done talking. Astro will visit all locations before finally playing an outro that ends the tour. 

## Changing Order of Locations

The order of the lab tour can be changed/updated in the `astro_statemchine.py` file. The dictionary named `STOP_2_STUDENTS` holds the ordering of the stops from 1-7. Astro will go to each student's desk in ascending order. 