import random
import copy


class Hat:
    def __init__(self, **balls): #balls argument takes in user-determined balls
        self.contents = [] #instantiates Hat object with an empty list

        for color, count in balls.items():
            for i in range(count):
                self.contents.append(color) #append each ball to the list

        self.replica = copy.deepcopy(self.contents) #create copy of contents list

    def draw(self, amount): #function to draw balls from Hat object
        self.contents = copy.deepcopy(self.replica) #create copy of the copy

        if amount > len(self.contents):
            return self.contents #if drawn amount exceeds available nr of balls return all

        else:
            drawn_balls = []
            for i in range(amount):
                drawn = random.choice(self.contents) #pick random ball
                self.contents.remove(drawn) #remove that ball from contents
                drawn_balls.append(drawn) #append ball to drawn_balls list

            return drawn_balls #return all drawn balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments): #function to calculate probability of events
    M = 0 #number of successful experiments

    expected = []

    for color, count in expected_balls.items(): #populates expected list the same way the initial contents list is created
        for i in range(count):
            expected.append(color)

    for i in range(num_experiments):
        box = [] #collects the expected balls that are actually drawn
        actual = hat.draw(num_balls_drawn) #create actual list by calling the draw function
        for e in expected:
            if e in actual: #if expected ball is among the drawn ones
                actual.remove(e) #remove ball from list of drawn ones to avoid counting a ball twice
                box.append(e) #add ball to box
        if len(expected) == len(box):
            M += 1 #experiment is successful if the expected balls match the drawn ones

    return M / num_experiments #calculate probability by dividing successful experiments by total experiments





