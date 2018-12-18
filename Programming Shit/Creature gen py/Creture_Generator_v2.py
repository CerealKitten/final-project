from random import randint

verify = ''


location_choice = ['Location'] + ['land']*33 + ['sea']*33 + ['sky']*34


def createPart(part):
    chance = randint(1,100)
    print(part[0]+':', part[chance])
    global verify
    verify = part[chance]
    return verify

def location():
    createPart(location_choice)
    if verify == 'land':
        landCreature()
    elif verify == 'sea':
        seaCreature()
    elif verify == 'sky':
        skyCreature()

def endline():
    verify = ''
    print('--------------------------------')

def landCreature():
    #head parameters
    head_choice = ['Head'] + ['yes'] * 90 + ['no'] * 10
    head_size = ['Size Percent'] + [str(randint(1,100))] * 100
    head_shape = ['Shape'] + ['round']*25 + ['boxy']*25 + ['sharp']*25 + ['flat']*25
    #nose parameters
    nose_choice = ['Nose'] + ['yes']*75 + ['no']*25
    nose_type = ['Type'] + ['wet']*25 + ['lizard']*25 + ['beak']*25 + ['snout']*25
    nose_flare = ['Flare Percent'] + [str(randint(1,100))]*100
    nose_size = ['Size Percent'] + [str(randint(1,100))]*100
    #eye parameters
    eye_choice = ['Eyes'] + ['yes']*80 + ['no']*29
    eye_amount = ['Amount'] + ['1']*17 + ['2']*36 + ['3']*12 + ['4']*28 + ['5']*7
    eye_shape = ['Eye Slant Percent'] + [str(randint(1,100))]*100
    eye_size = ['Size Percent'] + [str(randint(1,100))]*100
    #mouth Parameters
    mouth_choice = ['Mouth'] + ['yes']*96 + ['no']*4
    mouth_shape = ['Type'] + ['slit']*45 + ['crossed']*20 + ['gaping']*35
    #teeth parameters
    teeth_type = ['Teeth Type'] + ['carnivore']*15 + ['herbivore']*40 + ['omnivore']*45
    #ear parameters
    ears_choice = ['Ears'] + ['yes']*74 + ['no']*26
    ears_type = ['Type'] + ['rounded']*30 + ['pointed']*35 + ['nubs']*20 + ['antenae']*15
    #Genos parameters
    genos_choice = ['Genos'] + ['scales']*30 + ['fur']*30 + ['feathers']*15 + ['chitin']*25
    genos_length = ['Length Percentage'] + [str(randint(1,100))]*100
    genos_density = ['Density Percentage'] + [str(randint(1,100))]*100
    #legs parameters
    leg_choice = ['Legs'] + ['yes']*95 + ['no']*5
    leg_amount = ['Amount'] + ['2'] * 36 + ['4'] * 50 + ['6'] * 14
    leg_joints = ['Joints'] + ['2']*40 + ['3']*50 + ['4']*10
    #tail parameters
    tail_choice = ['Tail'] + ['yes']*31 + ['no']*69

    endline()
    createPart(head_choice)
    if verify == 'yes':
        createPart(head_size)
        createPart(head_shape)
        endline()
    else:
        endline()

    createPart(nose_choice)
    if verify == 'yes':
        createPart(nose_type)
        createPart(nose_flare)
        createPart(nose_size)
        endline()
    else:
        endline()

    createPart(eye_choice)
    if verify == 'yes':
        createPart(eye_amount)
        createPart(eye_shape)
        createPart(eye_size)
        endline()
    else:
        endline()

    createPart(mouth_choice)
    if verify == 'yes':
        createPart(mouth_shape)
        createPart(teeth_type)
        endline()
    else:
        endline()

    createPart(ears_choice)
    if verify == 'yes':
        createPart(ears_type)
        endline()
    else:
        endline()

    createPart(genos_choice)
    if verify == 'chitin':
        endline()
    else:
        createPart(genos_length)
        createPart(genos_density)
        endline()

    createPart(leg_choice)
    if verify == 'yes':
        createPart(leg_amount)
        createPart(leg_joints)
        endline()
    else:
        endline()

    createPart(tail_choice)

    
def seaCreature():
    #head parameters
    head_choice = ['Head'] + ['yes'] * 90 + ['no'] * 10
    head_size = ['Size Percent'] + [str(randint(1,100))] * 100
    head_shape = ['Shape'] + ['round']*25 + ['boxy']*25 + ['sharp']*25 + ['flat']*25
    #nose parameters
    nose_choice = ['Nose'] + ['yes']*40 + ['no']*60
    nose_flare = ['Flare Percent'] + [str(randint(1,100))]*100
    nose_size = ['Size Percent'] + [str(randint(1,100))]*100
    #gills parameters
    gill_choice = ['Gills'] + ['yes']*90 + ['no']*10
    gill_flare = ['Flare Percent'] + [str(randint(1,100))]*100
    gill_size = ['Size Percent'] + [str(randint(1,100))]*100
    #eye parameters
    eye_choice = ['Eyes'] + ['yes']*60 + ['no']*49
    eye_amount = ['Amount'] + ['1']*22 + ['2']*22 + ['3']*22 + ['4']*22 + ['5']*12
    eye_shape = ['Eye Slant Percent'] + [str(randint(1,100))]*100
    eye_size = ['Size Percent'] + [str(randint(1,100))]*100
    #mouth Parameters
    mouth_choice = ['Mouth'] + ['yes']*96 + ['no']*4
    mouth_shape = ['Type'] + ['slit']*45 + ['crossed']*20 + ['gaping']*35
    #teeth parameters
    teeth_type = ['Teeth Type'] + ['carnivore']*15 + ['herbivore']*40 + ['omnivore']*45
    #Genos parameters
    genos_choice = ['Genos'] + ['scales']*55 + ['skin']*30 + ['fur']*15
    genos_density = ['Density Percentage'] + [str(randint(1,100))]*100
    #fin parameters
    fin_choice = ['Fins'] + ['yes']*95 + ['no']*5
    fin_amount = ['Amount'] + ['2'] * 36 + ['4'] * 50 + ['6'] * 14
    fin_flare = ['Flare'] + [str(randint(1,100))] * 100
    #tail parametes
    tail_orientation = ['Tail Orientation'] + ['vertical']*65 + ['horizontal']*30 + ['crossed']*5
    tail_size = ['Size'] + [str(randint(1,100))]*100
    tail_flare = ['Flare'] + [str(randint(1,100))]*100
    #legs parameter
    leg_choice = ['Legs'] + ['yes']*5 + ['no']*95

    endline()
    createPart(head_choice)
    if verify == 'yes':
        createPart(head_size)
        createPart(head_shape)
        endline()
    else:
        endline()

    createPart(nose_choice)
    if verify == 'yes':
        createPart(nose_flare)
        createPart(nose_size)
        endline()
    else:
        endline()

    createPart(gill_choice)
    if verify == 'yes':
        createPart(gill_flare)
        createPart(gill_size)
        endline()
    else:
        endline()

    createPart(eye_choice)
    if verify == 'yes':
        createPart(eye_amount)
        createPart(eye_shape)
        createPart(eye_size)
        endline()
    else:
        endline()

    createPart(mouth_choice)
    if verify == 'yes':
        createPart(mouth_shape)
        createPart(teeth_type)
        endline()
    else:
        endline()

    createPart(genos_choice)
    if verify == 'chitin':
        endline()
    else:
        createPart(genos_density)
        endline()

    createPart(fin_choice)
    if verify == 'yes':
        createPart(fin_amount)
        createPart(fin_flare)
        endline()
    else:
        endline()
    
    createPart(tail_orientation)
    createPart(tail_size)
    createPart(tail_flare)
    endline()
    createPart(leg_choice)


def skyCreature():
    #head parameters
    head_choice = ['Head'] + ['yes']*90 + ['no']*10
    head_size = ['Size Percent'] + [str(randint(1,100))] * 100
    head_shape = ['Shape'] + ['round']*25 + ['boxy']*25 + ['sharp']*25 + ['flat']*25
    #nose parameters
    nose_choice = ['Nose'] + ['yes']*75 + ['no']*25
    nose_type = ['Type'] + ['wet']*20 + ['lizard']*45 + ['snout']*35
    nose_flare = ['Flare Percent'] + [str(randint(1,100))]*100
    nose_size = ['Size Percent'] + [str(randint(1,100))]*100
    #eye parameters
    eye_choice = ['Eyes'] + ['yes']*80 + ['no']*29
    eye_amount = ['Amount'] + ['1']*17 + ['2']*36 + ['3']*12 + ['4']*28 + ['5']*7
    eye_shape = ['Eye Slant Percent'] + [str(randint(1,100))]*100
    eye_size = ['Size Percent'] + [str(randint(1,100))]*100
    #mouth Parameters
    mouth_choice = ['Mouth'] + ['yes']*96 + ['no']*4
    mouth_shape = ['Type'] + ['slit']*30 + ['crossed']*6 + ['gaping']*4 + ['beak']*70
    #teeth parameters
    teeth_type = ['Teeth Type'] + ['carnivore']*15 + ['herbivore']*40 + ['omnivore']*45
    #ear parameters
    ears_choice = ['Ears'] + ['yes']*74 + ['no']*26
    ears_type = ['Type'] + ['rounded']*30 + ['pointed']*35 + ['nubs']*20 + ['antenae']*15
    #Genos parameters
    genos_choice = ['Genos'] + ['scales']*30 + ['fur']*30 + ['feathers']*15 + ['chitin']*25
    genos_length = ['Length Percentage'] + [str(randint(1,100))]*100
    genos_density = ['Density Percentage'] + [str(randint(1,100))]*100
    #legs parameters
    leg_choice = ['Legs'] + ['yes']*95 + ['no']*5
    leg_amount = ['Amount'] + ['2']*56 + ['4']*30 + ['6']*14
    leg_joints = ['Joints'] + ['2']*40 + ['3']*50 + ['4']*10
    #wing parameters
    wing_choice = ['Wings'] + ['yes']*85 + ['no']*15
    wing_size = ['Size'] + [str(randint(1,100))]*100

    global verify

    endline()
    createPart(head_choice)
    if verify == 'yes':
        createPart(head_size)
        createPart(head_shape)
        endline()
    else:
        endline()

    createPart(nose_choice)
    if verify == 'yes':
        createPart(nose_type)
        createPart(nose_flare)
        createPart(nose_size)
        endline()
    else:
        endline()

    createPart(eye_choice)
    if verify == 'yes':
        createPart(eye_amount)
        createPart(eye_shape)
        createPart(eye_size)
        endline()
    else:
        endline()

    createPart(mouth_choice)
    if verify == 'yes':
        createPart(mouth_shape)
        createPart(teeth_type)
        endline()
    else:
        endline()

    createPart(ears_choice)
    if verify == 'yes':
        createPart(ears_type)
        endline()
    else:
        endline()

    createPart(genos_choice)
    if verify == 'chitin':
        endline()
    else:
        createPart(genos_length)
        createPart(genos_density)
        endline()

    createPart(leg_choice)
    if verify == 'yes':
        createPart(leg_amount)
        createPart(leg_joints)
        endline()
    else:
        endline()

    createPart(wing_choice)
    if verify == 'yes':
        createPart(wing_size)
        verify = ''
    else:
        verify = ''
    
numcounter = 0

def get():
    innieS = input('Creature Amount: ')
    try:
        int(innieS)
    except ValueError:
        endline()
        print('The input was not an integer and is therefore unexecutable\n\nending program')
        endline()
        exit()
    innieI = int(innieS)
    innieR = range(innieI)
    endline()
    global numcounter
    while numcounter < innieI:
        print('creature number: ' + str(numcounter + 1) + '\n')
        location()
        endline()
        numcounter = numcounter+1
        innieI == innieI - 1
        print('********************************')
        endline()
    numcounter = 0

endline()

frank = 0

while frank == 0:
    get()
    asking = input('Continue?\ny/n: ')       
    endline()
    if asking == 'y':
        endline
        continue
    elif asking == 'n':
        frank = 1
        print('Thank you')
        endline()
    else:
        print('Not an acceptable input\nRestart application')
        endline()
        frank = 111