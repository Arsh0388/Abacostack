import random
"""
building bounded stack with only limited funcctions that we will use such as pop,push
first initializing the variables and checking whether the capacity is integer or not and greaater than 0
push methods swaps the element present at that position with the input item
in the intialization we put * as the element at each and every position
"""
class BStack:
    def __init__(self,capacity) :
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity)))
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))

        self.count = 0
        self.head = 0
        self.tail = 0
        self.items = []
        self.capacity = capacity
        for i in range(self.capacity) :
            self.items.append('*')

    def push(self,item) :
        if self.isFull():
            print(" stack is full")
        else :
            self.items[self.head] = item
        self.head += 1
        self.count += 1
    """
    the pop method takes out the element at that position and places * instead of the item
    """
    def pop(self) :
        if self.count == 0 :
            print(" stack is empty")
        else :
            item = self.items[self.tail]
            self.items[self.head - 1] = '*'
            self.head = self.head - 1
            self.count -= 1
            return item
    def stack_repr(self) :
        return (''.join(self.items[::-1]))
    def isFull(self) :
        return self.count == self.capacity

    """
    in the Card class we will intitalize the stacks of the game with the letters or the colors  of a certain height
    and certain width entered by the player
    reset gives us the configuration or the target
    stack instance intialize the stacks with seperate colors or letters
    """
class Card :
    def __init__(self,length,height) :
        self.height = height
        self.length = length
        self.alpha = 'ABCDE'
        self.beads = []
        for i in range(length) :
            self.beads = self.beads + [self.alpha[i]] * self.height
        print(self.beads)

    def reset(self) :
        random.shuffle(self.beads)
        return self.beads

    def stack(self,number) :
        start = (number - 1) * self.height
        end = self.height * number
        return self.beads[start:end]
    '''
    show method shows us the target in the card form
    '''
    def show(self,i) :
            return f"{' '.join(self.beads[i:len(self.beads):self.height])}"

    def __str__(self) :
        string = ''
        for i in range(self.length) :
            string = string + f"|{''.join(self.stack(i + 1))}|"
        return string

    def replace(self,filename,n) :
        with open(filename,'r') as f :
            f.readlines()
            self.beads1 = f[n].split()
            self.beads2 = []
            if self.beads1 == self.height * self.length:
                for i in range(len(self.beads1 % self.height)) :
                    if self.beads1.count(self.alpha[i]) == self.height :
                        self.beads2.append[self.alpha[i] * self.height]
                    else :
                        print("  wrong move ")
            else :
                print(" wrong move ")

"""
initializing all the variables, stacks, count
"""
class AbacoStack (Card) :
    def __init__(self,length,height) :
        self.length = length  # intializing the length or no of stacks  , height or depths of stacks
        self.height = height
        self.cards  = Card(length,height)  # creating a card object which gives us the intial card and return configuration
        self.main_top_list = ['*'] * (length + 2)   # intializing the main list oor top list
        self.Stack_initial = []   # a list of stacks
        ordered_stacks = []
        for i in range(1,self.length + 1) :
            ordered_stacks.append(self.cards.stack(i))      # getting the stacks colors in a list

        for i in range(1,self.length+1) :
            self.Stack_initial.append(BStack(self.height))   #creating numerous objects of stacks

        for i in range(1,self.length + 1) :
            for j in range(len(ordered_stacks[i - 1])) :
                self.Stack_initial[i - 1].push(ordered_stacks[i - 1].pop())   # settig up the first basic structure of stacks

        self.count = 0
        self.target = ''.join(self.cards.reset())   # getting the configuration in a variable to check whether the target is achieved of not

    def movebead(self,moves) :
        item_number = int(moves[0])
        move = moves[1]
        if move == 'r' :
            if self.main_top_list[item_number + 1] == '*' :
                self.main_top_list[item_number],self.main_top_list[item_number + 1] = self.main_top_list[item_number + 1],self.main_top_list[item_number]
                self.count += 1
            else :
                print(" Move cannot be places")

        elif move == 'l':
            if self.main_top_list[item_number - 1] == '*' :
                self.main_top_list[item_number - 1],self.main_top_list[item_number] = self.main_top_list[item_number],self.main_top_list[item_number - 1 ]
                self.count += 1

        elif move == 'u' :
            if self.main_top_list[item_number] == '*' :
                stack_item = self.Stack_initial[item_number - 1].pop()
                self.main_top_list[item_number],stack_item = stack_item,self.main_top_list[item_number]
                self.count += 1
            else :
                print(" incorrect move ")

        elif move == 'd' :
            if self.main_top_list[item_number] == '*' :
                print(" No element is present at that place ")
            else :
                stack_item = self.main_top_list[item_number]
                self.Stack_initial[item_number - 1].push(stack_item)
                self.main_top_list[item_number] = '*'
                self.count += 1

    def show(self) :
        numbers = [str(x) for x in range(self.length + 2)]
        length = len(' '.join(numbers))
        print(' '.join(numbers))
        print(f"{' '.join(self.main_top_list)}           card ")
        self.card = ''
        for i in range(len(self.Stack_initial)) :
                self.card = self.card  + self.Stack_initial[i].stack_repr()
        for i in range(self.height) :
            print(f"| {' '.join(self.card[i:len(self.card):self.height])} |         | {self.cards.show(i)} | ")
        print(f"+{'*'*(length - 2)}+           moves {self.count}")
        #print(" your target is given below and no of steps done are ", self.count)


    def reset(self) :   # resets all the variables and generate new problem or target
        self.__init__(self.length,self.height)

    def isSolved(self) :  # checks whether the target is achieved or not . by checking the configuratiooonn we got as a target
        # and by comparing it with the current state of stacks
        return self.card == self.target
