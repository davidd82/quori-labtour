from typing import Any
from statemachine import StateMachine, State
import lab_Students

class LabTourMachine(StateMachine):
    "Quori Lab Tour"
    greeting = State(initial=True)
    checking_list = State()
    moving = State()
    talking = State()
    pause = State()
    outro = State(final=True)

    start_tour = greeting.to(checking_list)

    check_list = (
        checking_list.to(outro, cond ="no_more_locations")
        | checking_list.to(moving, unless="no_more_locations")
    )

    check_location = (
        moving.to(talking, cond="reached_location")
        | moving.to(moving, unless="reached_location")
    )

    check_person = (
        talking.to(pause, cond="person_present")
        | talking.to(checking_list, unless="person_present")
    )

    check_person_talking = (
        pause.to(checking_list, cond = "person_finished_talking")
        | pause.to(pause, unless="person_finished_talking")
    )

    def __init__(self):
        self.locations = 6
        super(LabTourMachine, self).__init__()

    def no_more_locations(self):
        return self.locations == 0
    
    def reached_location(self):
        return True
    
    def person_present(self):
        return True
    
    def person_finished_talking(self):
        return True
    
    def before_start_tour(self):
        print("Starting Tour!")

    def on_enter_checking_list(self):
        print("Checking List!")
    
    def on_enter_outro(self):
        print("No more locations! Saying outro!")

    def on_enter_moving(self):
        print("Moving to next location!")

    def on_enter_talking(self):
        print("Talking!")
        print(lab_Students.labStudentDescriptions[lab_Students.phd_students[self.locations]])
        self.locations -= 1
    
    def on_enter_pause(self):
        print("Person is talking!")

q = LabTourMachine()
q.start_tour()
q.check_list()
q.check_location()
q.check_person()
q.check_person_talking()
q.check_list()
q.check_location()
q.check_person()
q.check_person_talking()

