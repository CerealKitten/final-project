import random #calls in the random library so i can use the randint function

#defines the probabilities for the head characteristics
head_choice = ['Head'] + ['Yes'] * 90 + ['No'] * 10
head_shape = ['Head Shape'] + ['round'] * 35 + ['boxy'] * 20 + ['long'] * 30 + ['thin'] * 15
head_size = ['Head Size'] + ['large'] * 5 + ['medium large'] * 15 + ['medium'] * 40 + ['medium small'] * 25 + ['small'] * 15

#define probabilities for eye characteristics
eye_choice = ['Eyes'] + ['Yes'] * 95 + ['No'] * 5
eye_amount = ['Eye Amount'] + ['1'] * 16 + ['2'] * 30 + ['3'] * 10 + ['4'] * 13 + ['5'] * 8 + ['6'] * 8 + ['7'] * 6 + ['8'] * 5 + ['9'] * 4

#define probabilities for nose characteristica
nose_choice = ['Nose'] + ['Yes'] * 78 + ['No'] * 22
nose_type = ['Nose Type'] + ['flat'] * 27 + ['domestic'] * 20 + ['flush'] * 23 + ['flared'] * 23 + ['snout'] * 7

#define probabilities for mouth characteristica
mouth_choice = ['Mouth'] + ['Yes'] * 90 + ['No'] * 10
mouth_amount = ['Mouth Amount'] + ['1'] * 85 + ['2'] * 10 + ['3'] * 5
mouth_type = ['Mouth Type'] + ['protrusion'] * 34 + ['no protrusion'] * 33 + ['beak'] * 33
mouth_size = ['Mouth Size'] + ['large'] * 10 + ['medium large'] * 20 + ['medium'] * 40 + ['medium small'] * 20 + ['small'] * 10

#define probabilities for teeth characteristica
teeth_choice = ['Teeth'] + ['Yes'] * 91 + ['No'] * 9
teeth_type = ['Teeth Type'] + ['herbivore'] * 30 + ['carnivore'] * 30 + ['omnivore'] * 30 + ['tusks'] * 10

#define probabilities for neck characteristica
neck_choice = ['Neck'] + ['Yes'] * 60 + ['No'] * 40
neck_length =['Neck Length'] + ['long'] * 15 + ['medium long'] * 15 + ['medium'] * 25 + ['medium short'] * 30 + ['short'] * 15

#define probabilities for arm characteristica
arm_choice = ['Arms'] + ['Yes'] * 7 + ['No'] * 93
arm_amount = ['Arm Amount'] + ['1'] * 15 + ['2'] * 40 + ['3'] * 15 + ['4'] * 30
arm_joints = ['Arm Joints'] + ['2'] * 55 + ['3'] * 10 + ['4'] * 5 + ['tentacle'] * 30
arm_length = ['Arm Length'] + ['long'] * 10 + ['medium long'] * 20 + ['medium'] * 40 + ['medium short'] * 20 + ['short'] * 10

#define probabilities for hand and finger characteristica
fingers_amount = ['Fingers'] + ['2'] * 30 + ['3'] * 25 + ['4'] * 20 + ['5'] * 15 + ['6'] * 6 + ['7'] * 5 + ['8'] * 4 + ['9'] * 3 + ['10'] * 2
claw_type = ['Claw Type'] + ['Sharp'] * 50 + ['rounded'] * 50
claw_length = ['Claw Length'] + ['long'] * 10 + ['medium long'] * 15 + ['medium'] * 20 + ['medium short'] * 25  + ['short'] * 30

#define probabilities for leg characteristica
leg_choice =['Legs'] + ['Yes'] * 85 + ['No'] * 15
leg_amount =['Leg Amount']  + ['1'] * 10 + ['2'] * 45 + ['3'] * 10 + ['4'] * 25 + ['5'] * 4 + ['6'] * 3 + ['lots'] * 3
leg_joints = ['Leg Joints'] + ['2'] * 40 + ['3'] * 35 + ['4'] * 5 + ['tentacle'] * 20
leg_length = ['Leg Length'] + ['long'] * 10 + ['medium long'] * 30 + ['medium'] * 20 + ['medium short'] * 20 + ['short'] * 20

#define probabilities for feet characteristica
feet_type = ['Feet Type'] + ['hooves'] * 30 + ['tentacle'] * 10 + ['paw'] * 15 + ['bird'] * 45
toe_amount = ['Toe Amount'] + ['2'] * 40 + ['3'] * 30 + ['4'] * 15 + ['5'] * 10 + ['6'] * 5

#define probabilities for horn characteristica
horn_choice = ['Horns'] + ['Yes'] * 40 + ['No'] * 60
horn_type = ['Horn Type'] + ['bull'] * 30 + ['ram'] * 20 + ['deer/moose'] * 25 + ['unicorn'] * 15 + ['giraffe'] * 10
horn_symetry = ['Symetry'] + ['yes'] * 73 + ['no'] * 27
horn_size = ['Horn Size'] + ['large'] * 10 + ['medium large'] * 15 + ['medium'] * 20 + ['medium small'] * 25 + ['small'] * 30
horn_amount = ['Horn Amount'] + ['1'] * 5 + ['2'] * 60 + ['3'] * 20 + ['4'] * 7 + ['5'] * 3 + ['6'] * 3 + ['lots'] * 2

#define probabilities for body characteristica
chest_size = ['Chest Size'] + ['large'] * 10 + ['medium large'] * 15 + ['medium'] * 50  + ['medium small'] * 15 + ['small'] * 10
torso_length = ['Torso Length'] + ['long'] * 20 + ['medium long'] * 20 + ['medium'] * 20 + ['medium short'] * 20 + ['short'] * 20

#define probabilities for tail characteristica
tail_choice = ['Tail'] + ['Yes'] * 67 + ['No'] * 33
tail_amount = ['Tail Amount'] + ['1'] * 65 + ['2'] * 20 +['3'] * 10 + ['4'] * 1 +['5'] * 1 + ['6'] * 1 + ['lots'] * 2
tail_type = ['Tail Type'] + ['thin'] * 25 + ['thick'] * 25 + ['medium thickness'] * 25 + ['skinny with lots of hair'] * 25
tail_length = ['Tail Length'] + ['long'] * 15 + ['medium long'] * 25 + ['medium'] * 40 + ['medium short'] * 20 + ['short'] * 10
tail_end = ['Tail End'] + ['nothing'] * 60 + ['stinger'] * 8 + ['single spike'] * 8 + ['many spikes'] * 8 + ['smashing tool'] * 8 +['fan']  * 8

#define probabilities for fur and feather characteristica
hair_choice = ['Hair/feather'] + ['Yes'] * 65 + ['No'] * 35
hair_length = ['Hair Length'] + ['short'] * 60 + ['medium length'] * 25 + ['long'] * 15
hair_amount = ['Hair Amount'] + ['almost none'] * 5 + ['some'] * 5 + ['decent amount'] * 10 + ['a lot'] * 30 + ['completly covered'] * 50

#define probabilities for skin characteristica
skin_type = ['Skin Type'] + ['soft skin'] * 40 + ['hard shell'] * 15 + ['plates'] * 10 + ['scales'] * 35

#define probabilities for wing characteristica
wing_choice = ['Wings'] + ['Yes'] * 15 + ['No'] * 85
wing_amount = ['Wing Amount'] + ['1'] * 10 + ['2'] * 46 + ['4'] * 24 + ['6'] * 20
wing_type = ['Wing Type'] + ['feather'] * 45 + ['webbed'] * 30 + ['chitin'] * 25
wing_size = ['Wing Size'] + ['large'] * 20 + ['medium large'] * 20 + ['medium'] * 20 + ['medium small'] * 20 + ['small'] * 20
wing_function = ['Wing Function'] + ['decoration'] * 41 + ['gliding'] * 17 + ['flying'] * 10 + ['swimming'] * 12 + ['running'] * 20

verify = ''

numcounter = 0

def createPart(part):
    chance = random.randint(1,100)
    print(part[0]+':', part[chance])
    global verify
    verify = part[chance]
    return verify

def head():
    createPart(head_choice)
    global verify
    if verify == 'Yes':
        createPart(head_shape)
        createPart(head_size)
        verify = ''
        print('')
        neck()
    else:
        verify = ''
        neck()
        print('')

def eyes():
    createPart(eye_choice)
    global verify
    if verify == 'Yes':
        createPart(eye_amount)
        verify = ''
        print('')
    else:
        verify = ''
        print('')

def nose():
    createPart(nose_choice)
    global verify
    if verify == 'Yes':
        createPart(nose_type)
        verify =''
        print('')
    else:
        verify = ''
        print('')

def mouth():
    createPart(mouth_choice)
    global verify
    if verify == 'Yes':
        createPart(mouth_type)
        createPart(mouth_amount)
        createPart(mouth_size)
        print('')
        createPart(teeth_choice)
        if verify == 'Yes':
            createPart(teeth_type)
            verify = ''
            print('')
        else:
            verify =''
            print('')
    else:
        verify = ''
        print('')

def neck(): 
    createPart(neck_choice)
    global verify
    if verify == 'Yes':
        createPart(neck_length)
        verify =''
        print('')
    else:
        verify = ''
        print('')

def arm():
    createPart(arm_choice)
    global verify
    if verify == 'Yes':
        createPart(arm_amount)
        createPart(arm_joints)
        createPart(arm_length)
        verify =''
        print('')
        createPart(fingers_amount)
        createPart(claw_type)
        createPart(claw_length)
        print('')
    else:
        verify = ''
        print('')

def leg():
    createPart(leg_choice)
    global verify
    if verify == 'Yes':
        createPart(leg_amount)
        createPart(leg_joints)
        createPart(leg_length)
        verify =''
        print('')
        createPart(feet_type)
        createPart(toe_amount)
        createPart(claw_type)
        createPart(claw_length)
        print('')
    else:
        verify = ''
        print('')

def horn():
    createPart(horn_choice)
    global verify
    if verify == 'Yes':
        createPart(horn_type)
        createPart(horn_amount)
        createPart(horn_size)
        createPart(horn_symetry)
        verify =''
        print('')
    else:
        verify = ''
        print('')

def chest():
    createPart(chest_size)
    createPart(torso_length)
    print('')

def skin():
    createPart(skin_type)
    print('')

def tail():
    createPart(tail_choice)
    global verify
    if verify == 'Yes':
        createPart(tail_type)
        createPart(tail_amount)
        createPart(tail_length)
        createPart(tail_end)
        verify =''
        print('')
    else:
        verify = ''
        print('')

def hair():
    createPart(hair_choice)
    global verify
    if verify == 'Yes':
        createPart(hair_amount)
        createPart(hair_length)
        verify =''
        print('')
    else:
        verify = ''
        print('')

def wing():
    createPart(wing_choice)
    global verify
    if verify == 'Yes':
        createPart(wing_type)
        createPart(wing_amount)
        createPart(wing_size)
        createPart(wing_function)
        verify =''
        print('')
    else:
        verify = ''
        print('')

def createCreature():
    head()
    eyes()
    nose()
    mouth()
    arm()
    leg()
    horn()
    chest()
    tail()
    skin()
    hair()
    wing()

def get():
    innieS = input('Creature Amount: ')
    innieI = int(innieS)
    innieR = range(innieI)
    print('\n------------------------------\n')
    global numcounter
    while numcounter < innieI:
        print('creature number: ' + str(numcounter + 1) + '\n')
        createCreature()
        numcounter = numcounter+1
        innieI == innieI - 1
        print('------------------------------\n')
    numcounter = 0
print('\n')

frank = 0

while frank == 0:
    get()