from typing import Any
from statemachine import StateMachine, State
from playsound import playsound
import time
from transitions import Machine

locations = ["../scripts/audio/A'di.mp3",'../scripts/audio/Amy.mp3','../scripts/audio/Kaleen.mp3',
             '../scripts/audio/Leticia.mp3','../scripts/audio/Mina.mp3','../scripts/audio/Nathan.mp3',
             '../scripts/audio/Zhonghao.mp3']

GOTO_Commands = ["../scripts/audio/GOTO A'di's Desk.mp3","../scripts/audio/GOTO Amy's Desk.mp3","../scripts/audio/GOTO Kaleen's Desk.mp3",
             "../scripts/audio/GOTO Leticia's Desk.mp3","../scripts/audio/GOTO Mina's Desk.mp3","../scripts/audio/GOTO Nathan's Desk.mp3",
             "../scripts/audio/GOTO Zhonghao's Desk.mp3"]

people = {
    "A'di"     : 0,
    'Amy'      : 1,
    'Kaleen'   : 2,
    'Leticia'  : 3,
    'Mina'     : 4,
    'Nathan'   : 5,
    'Zhonghao' : 6,
}

class LabTourMachine(StateMachine):
    "Quori Lab Tour"
    
    # init = State(initial = True)
    # check_list = State()
    # moving = State()
    # check_person = State()
    # talking = State()
    # check_person_talking = State()
    # outro = State(final=True)

    STATES = ['init', 'check_list', 'moving', 'check_person', 'check_person_talking', 'talking', 'outro']

    
    def __init__(self, person_there=False, no_more_locations=False):
        self.machine = Machine(model=self, states=LabTourMachine.STATES, initial='init')
        self.person_there = person_there
        self.no_more_locations = no_more_locations
        self.locations = 6
        playsound('../scripts/audio/intro.mp3')
    
        self.machine.add_transition(trigger='proceed',source='init', dest='check_list')

        self.machine.add_transition(trigger='proceed',source='check_list', dest='outro', conditions=["no_more_locations_"])
        self.machine.add_transition(trigger='proceed',source='check_list', dest='moving')


        self.machine.add_transition(trigger='proceed',source='moving', dest='check_person')

        self.machine.add_transition(trigger='proceed',source='check_person', dest='check_person_talking', conditions=['person_is_there'])
        self.machine.add_transition(trigger='proceed',source='check_person', dest='talking')

        self.machine.add_transition(trigger='proceed',source='check_person_talking', dest='check_list')

        self.machine.add_transition(trigger='proceed',source='talking', dest='check_list')


    def no_more_locations_(self):
        return self.no_more_locations

      
    def person_is_there(self):
        return self.person_there

        
    def on_enter_init(self):
        print("Begin")

    def on_enter_check_person(self):
        response = input('is there a person?')
        if response == 'y':
            self.person_there = True
        else:
            self.person_there = False

    def on_enter_check_person_talking(self):
        response = input('is person done talking?')
        self.locations -= 1
        print(self.locations)

    def on_enter_check_list(self):
        print("Checking List!")
        if self.locations == -1:
            self.no_more_locations = True
        else:
            self.no_more_locations = False
    
    def on_enter_outro(self):
        print("No more locations! Saying outro!")
        playsound('../scripts/audio/outro.mp3')

    def on_enter_moving(self):
        print("Moving to next location!")
        playsound(GOTO_Commands[self.locations])
        input('is astro done moving?')
       

    def on_enter_talking(self):
        print("Talking!")
        playsound(locations[self.locations])
        self.locations -= 1
        print(self.locations)

    

q = LabTourMachine()

while q.state != "outro":
    q.proceed()



