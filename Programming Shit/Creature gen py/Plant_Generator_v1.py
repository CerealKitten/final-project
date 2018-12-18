import random #calls in the random library so i can use the randint function

verify = ''

numcounter = 0

def createPart(part):
    chance = random.randint(1,100)
    print(part[0]+':', part[chance])
    global verify
    verify = part[chance]
    return verify

def endline():
    verify = ''
    print('--------------------------------')

def typeChoose():
    #decides which kind of plant is goin to be made
    type_choice = ['Type'] + ['Tree'] * 10 + ['Flower'] * 30 + ['Fern'] * 8 + ['Succulents'] * 26 + ['Grass'] * 3 + ['Vines'] * 18 + ['Fruit'] * 10

    createPart(type_choice)
    global verify
    if verify == 'Tree':
        verify = ''
        tree()
    elif verify == 'Flower':
        verify = ''
        flower()
    elif verify == 'Fern':
        verify = ''
        fern()
    elif verify == 'Succulents':
        verify = ''
        succulents()
    elif verify == 'Grass':
        verify = ''
        grass()
    elif verify == 'Vines':
        verify = ''
        vines()
    elif verify == 'Fruit':
        verify = ''
        fruit()

def tree():
    #Tree variables
    tree_size = ['Tree Size'] + ['giant'] * 7 + ['semi giant'] * 17 + ['big'] * 10 + ['big medium'] * 14 + ['medium'] * 15 + ['medium small'] * 13 + ['small'] * 11 + ['tiny'] * 13

    trunk_height = ['Trunk Height'] + ['tall'] * 10 + ['meidium tall'] * 30 + ['medium'] * 25 + ['short'] * 20 + ['none'] * 15
    trunk_thickness = ['Trunk Thickness'] + ['thick'] * 5 + ['medum thick'] * 10 + ['medium'] * 45 + ['medium thin'] * 30 + ['thin'] * 10

    branches_length = ['Branch Length'] + ['long'] * 13 + ['medium long'] * 27 + ['medium length'] * 30 + ['medium short'] * 20 + ['short'] * 10
    branches_amount = ['Branch Density'] + ['heavy'] * 11 + ['medium heavy'] * 16 + ['medium weight'] * 30 + ['medium light'] * 21 + ['light'] * 13 + ['extra light'] * 9
    branches_thickness = ['Branch Thickness'] + ['thick'] * 23 + ['medium '] * 46 + ['thin'] * 31

    bark_thickness = ['Bark Thickness'] + ['thick'] * 13 + ['medium thick'] * 17 + ['medium'] * 21 + ['medium thin'] * 23 + ['thin'] * 26
    bark_shagginess = ['Bark Shagginess'] + ['shaggy'] * 7 + ['semi shaggy'] * 18 + ['medium'] * 21 + ['semi smooth'] * 24 + ['smooth'] * 30
    bark_pattern = ['Bark Texture'] + ['striped'] * 18 + ['vertical spiral'] * 15 + ['lumpy'] * 19 + ['none'] * 38 + ['spiny'] * 10

    tree_roots_length = ['Root Length'] + ['long'] * 18 + ['medium long'] * 29 + ['medium length'] * 27 + ['medium short'] * 17 + ['short'] * 9
    tree_roots_exposure = ['Root Exposure'] + ['exposed'] * 33 + ['partly exposed'] * 1335 + ['hidden'] * 34

    leaves_shape = ['Leaf Shape'] + ['thin'] * 20 + ['round'] * 20 + ['wide'] * 20 + ['sharp'] * 20 + ['wavy'] * 20
    leaves_pattern = ['Leaf Pattern'] + ['spotted'] * 15 + ['striped'] * 19 + ['zagged'] * 14 + ['v-striped'] * 17 + ['plain'] * 35

    bush_size = ['Bush Size'] + ['large'] * 17 + ['medium large'] * 27 + ['medium'] * 26 + ['medium small'] * 19 + ['small'] * 11
    bush_shape = ['Bush Shape'] + ['round'] * 33 + ['flat'] * 27 + ['pointed'] * 23 + ['squared'] * 17
    bush_density = ['Bush Density'] + ['very dense'] * 10 + ['dense'] * 15 + ['semi-dense'] * 35 + ['slightly dense'] * 25 + ['sparse'] * 15

    fruit_bearing = ['Bears Fruit'] + ['yes'] * 33 + ['no'] * 67 

    endline()
    createPart(tree_size)
    endline()
    createPart(trunk_height)
    createPart(trunk_thickness)
    endline()
    createPart(branches_length)
    createPart(branches_amount)
    createPart(branches_thickness)
    endline()
    createPart(bark_thickness)
    createPart(bark_shagginess)
    createPart(bark_pattern)
    endline()
    createPart(tree_roots_length)
    createPart(tree_roots_exposure)
    endline()
    createPart(leaves_shape)
    createPart(leaves_pattern)
    endline()
    createPart(bush_shape)
    createPart(bush_size)
    createPart(bush_density)
    endline()
    createPart(fruit_bearing)
    global verify
    if verify == 'yes':
        fruit()
    else:
        endline()
        verify = ''

def flower():
    #flower variables
    bud_type = ['Bud Type'] + ['bulbous'] * 28 + ['inverted'] * 18 + ['open'] * 32 + ['wide'] * 19 + ['swirled'] * 7
    bud_size = ['Bud Size'] + ['large'] * 12 + ['medium large'] * 23 + ['medium'] * 31 + ['medium small'] * 24 + ['small'] * 10

    petal_shape = ['Petal Shape'] + ['round'] * 22 + ['short'] * 22 + ['pointed'] * 22 + ['wavy'] * 22 + [ 'squared'] * 12
    petal_pattern = ['Petal Pattern'] + ['burst'] * 30 + ['spotted'] * 15 + ['striped'] * 30 + ['insane'] * 25

    stem_length = ['Stem Length'] + ['long'] * 10 + ['medium long'] * 25 + ['medium length'] * 35 + ['medium short'] * 15 + ['short'] * 15

    leaves_shape = ['Leaf Shape'] + ['wide'] * 30 + ['round'] * 30 + ['wavy'] * 10 + ['thin'] * 30
    leaves_pattern = ['Leaf Pattern'] + ['striped'] * 30 + ['spotted'] * 10 + ['plain'] * 50 + ['bubbly'] * 10 

    flower_roots_length = ['Root Length'] + ['long'] * 4 + ['semi long'] * 20 + ['medium length'] * 24 + ['semi short'] * 28 + ['short'] * 24
    flower_roots_exposure = ['Root Exposure'] + ['hidden'] * 50 + ['semi exposed'] * 20 + ['exposed'] * 30
    flower_size = ['Flower Size'] + ['large'] * 5 + ['semi large'] * 10 + ['medium'] * 15 + ['semi small'] * 50 + ['small'] * 20

    endline()
    createPart(bud_type)
    createPart(bud_size)
    endline()
    createPart(petal_shape)
    createPart(petal_pattern)
    endline()
    createPart(stem_length)
    endline()
    createPart(leaves_shape)
    createPart(leaves_pattern)
    endline()
    createPart(flower_roots_length)
    createPart(flower_roots_exposure)
    endline()
    createPart(flower_size)
    endline()

def fern():
    #Fern variables
    stalk_height = ['Stalk Height'] + ['tall'] * 20 + ['meidium tall'] * 20 + ['medium height'] * 20 + ['short'] * 20 + ['none'] * 20

    blade_shape = ['Blade Shape'] + ['flat'] * 20 + ['rounded'] * 20 + ['spiked'] * 20 + ['wavey'] * 20 + ['wide'] * 20
    blade_density = ['Blade Density'] + ['very dense'] * 20 + ['dense'] * 20 + ['semi-dense'] * 20 + ['slightly dense'] * 20 + ['sparse'] * 20
    blade_size = ['Blade Size'] + ['large'] * 20 + ['semi large'] * 20 + ['medium length'] * 20 + ['semi small'] * 20 + ['small'] * 20
    blade_length = ['Blade Length'] + ['long'] * 20 + ['semi ling'] * 20 + ['medium length'] * 20 + ['semi short'] * 20 + ['short'] * 20

    pinna_density = ['Pinna Density'] + ['very dense'] * 20 + ['dense'] * 20 + ['semi-dense'] * 20 + ['slightly dense'] * 20 + ['sparse'] * 20
    pinnule_shape = ['Pinnule Shape '] + ['serrated'] * 20 + ['round'] * 20 + ['thin'] * 20 + ['flared'] * 20 + ['soft'] * 20

    endline()
    createPart(stalk_height)
    endline()
    createPart(blade_shape)
    createPart(blade_density)
    createPart(blade_size)
    createPart(blade_length)
    createPart(blade_length)
    endline()
    createPart(pinna_density)
    createPart(pinnule_shape)
    endline()

def succulents():
    #Cactus variables
    cac_or_suc = ['Succulent or Cactus'] + ['cactus'] * 30 + ['succulent'] * 70
    c_stem_choice = ['Stem'] + ['yes'] * 10 + ['no'] * 90 
    c_stem_length = ['Stem Length'] + ['long'] * 5 + ['medium long'] * 25 + ['medium'] * 35 + ['medium short'] * 20 + ['short'] * 15
    c_stem_girth = ['Stem Girth'] + ['thick'] * 5 + ['medium thick'] * 25 + ['medium'] * 35 + ['medium thin'] * 20 + ['thin'] * 15
    flower_choice = ['Flowers'] + ['yes'] * 16 + ['no'] * 84
    full_choice = ['Flower or Bud'] + ['full flower'] * 20 + ['only bud'] * 80

    cac_type = ['Cactus Type'] + ['round'] * 16 + ['twins'] * 16 + ['swarm'] * 17 + ['long'] * 17 + ['arms'] * 17 + ['petals'] *17
    cac_size = ['Size'] + ['large'] * 5 + ['medium large'] * 10 + ['medium'] * 15 + ['medium small'] * 25 + ['small'] * 45
    spike_pattern = ['pattern'] + ['vertical lined'] * 75 + ['swirled'] * 20 + ['horizontal rows'] * 5
    spike_frequency = ['Frequency'] + ['frequent'] * 30 + ['semi frequent'] * 23 + ['average'] * 25 + ['semi infrequent'] * 23 + ['infrequent'] * 19
    Spike_size = ['Spike Size'] + ['large'] * 5 + ['medium large'] * 10 + ['medium'] * 15 + ['medium small'] * 60 + ['rounded small'] * 10

    succ_type = ['Succulent Type'] + ['buds'] * 25 + ['nubs'] * 25 + ['leaves'] * 25 + ['stems'] * 25
    succ_size = ['Size'] + ['large'] * 16 + ['medium large'] * 19 + ['medium'] * 20 + ['medium small'] * 21 + ['small'] * 24
    s_leaf_type = ['Leaf Type'] + ['pointed tip'] * 20 + ['thick'] * 20 + ['rods'] * 20 + ['balls'] * 20 + ['cubes'] * 20
    s_leaf_shape = ['Leaf Shape'] + ['cubed'] * 25 + ['pointed'] * 25 + ['thin'] * 25 + ['sharp'] * 25

    def cactus():
        createPart(cac_type)
        endline()
        createPart(cac_size)
        endline()
        createPart(spike_pattern)
        createPart(spike_frequency)
        createPart(Spike_size)
        endline()
        createPart(c_stem_choice)
        global verify
        if verify == 'yes':
            createPart(c_stem_length)
            createPart(c_stem_girth)
            fchoice()
        else:
            fchoice()

    def fchoice():
        endline()
        createPart(flower_choice)
        global verify
        if verify == 'yes':
            createPart(full_choice)
            if verify == 'yes':
                flower()
            else:
                petal_shape = ['Petal Shape'] + ['round'] * 22 + ['short'] * 22 + ['pointed'] * 22 + ['wavy'] * 22 + [ 'squared'] * 12
                petal_pattern = ['Petal Pattern'] + ['burst'] * 30 + ['spotted'] * 15 + ['striped'] * 30 + ['insane'] * 25
                createPart(petal_shape)
                createPart(petal_pattern)
                verify = ''
        else:
            endline()
            verify = ''

    endline()
    createPart(cac_or_suc)
    endline()
    global verify
    if verify == 'succulent':
        createPart(succ_type)
        createPart(succ_size)
        endline()
        createPart(s_leaf_type)
        createPart(s_leaf_shape)
        endline()
    else:
        cactus()


def grass():
    #Grass variables
    blade_shape = ['Blade Shape'] + ['spade'] * 20 + ['rounded'] * 20 + ['wavy'] * 20 + ['straight'] * 20 + ['tear shape'] * 20
    g_blade_length = ['Blade Length'] + ['long'] * 20 + ['medium long'] * 20 + ['medium'] * 20 + ['medium short'] * 20 + ['short'] * 20
    blade_thickness = ['Blade Thickness'] + ['thick'] * 20 + ['medum thick'] * 20 + ['medium'] * 20 + ['medium thin'] * 20 + ['thin'] * 20
    blade_size = ['Blade Size'] + ['large'] * 20 + ['medium large'] * 20 + ['medium'] * 20 + ['medium small'] * 20 + ['small'] * 20

    grass_height = ['Height'] + ['tall'] * 20 + ['meidium tall'] * 20 + ['medium height'] * 20 + ['short'] * 20 + ['none'] * 20
    grass_size = ['Size'] + ['large'] * 20 + ['medium large'] * 20 + ['medium'] * 20 + ['medium small'] * 20 + ['small'] * 20

    crown_size = ['Crown Size'] + ['large'] * 20 + ['medium large'] * 20 + ['medium'] * 20 + ['medium small'] * 20 + ['small'] * 20

    seed_head = ['Head Type'] + ['seeds'] * 33 + ['flower'] * 33 + ['puffy'] * 34

    endline()
    createPart(blade_shape)
    createPart(g_blade_length)
    createPart(blade_thickness)
    createPart(blade_size)
    endline()
    createPart(grass_height)
    createPart(grass_size)
    endline()
    createPart(crown_size)
    endline()
    createPart(seed_head)
    endline()

def vines():
    #Vines variables
    node_inter = ['Internode Distance'] + ['short'] * 17 + ['medium'] * 66 + ['long'] * 17
    node_dormancy = ['Node Dormancy'] + ['rare'] * 25 + ['uncommon'] * 35 + ['common'] * 26 + ['often'] * 14

    leaf_shape = ['Leaf Shape'] + ['frayed'] * 25 + ['pentagonal symmetry'] * 25 + ['vertical symmetry'] * 25 + ['round'] * 25

    pedicel_fruit = ['Pedicel Fruit'] + ['yes'] * 20 + ['no'] * 80
    pedicel_frequency = ['Pedicel Frequency'] + ['frequent'] * 3 + ['semi frequent'] * 17 + ['average'] * 26 + ['semi non'] * 34 + ['infrequent'] * 20
    pedicel_density = ['Pedicel Density'] + ['dense'] * 25 + ['semi dense'] * 30 + ['average'] * 15 + ['semi sparse'] * 10 + ['sparse'] * 20

    endline()
    createPart(node_inter)
    createPart(node_dormancy)
    endline()
    createPart(leaf_shape)
    endline()
    createPart(pedicel_fruit)
    global verify
    if verify == 'yes':
        fruit()
        createPart(pedicel_frequency)
        createPart(pedicel_density)
        endline()
    else:
        endline()
        verify = ''

def fruit():
    #Fruit and vegetables variables
    veg_fruit = ['Fruit or Vegetable'] + ['fruit'] * 75 + ['vegetable'] * 25
    veg_type = ['Vegetable Type'] + ['root'] * 20 + ['stem'] * 20 + ['bush'] * 20 + ['head'] * 20 + ['hanging'] * 20

    fruit_type = ['Fruit Type'] + ['citrus'] * 25 + ['melon'] * 25 + ['berry'] * 25 + ['other'] * 25

    fruit_growth = ['Growth Pattern'] + ['groups'] * 50 + ['singular'] * 50
    veg_size = ['Size'] + ['large'] * 20 + ['medium large'] * 20 + ['medium'] * 20 + ['medium small'] * 20 + ['small'] * 20
    veg_style = ['Style'] + ['striped'] * 25 + ['spotted'] * 25 + ['plain '] * 25 + ['wavy'] * 25
    veg_tex = ['Texture'] + ['smooth'] * 18 + ['rough'] * 18 + ['bumpy'] * 18 + ['gooey'] * 6 + ['scaled'] * 4 + ['fuzzy'] * 18 + ['hairy'] * 18
    sec_tex = ['Second'] + ['yes'] *17 + ['no'] * 83
    second = ['Second Texture'] + ['smooth'] * 18 + ['rough'] * 18 + ['bumpy'] * 18 + ['gooey'] * 6 + ['scaled'] * 4 + ['fuzzy'] * 18 + ['hairy'] * 18

    endline()
    createPart(veg_fruit)
    global verify
    if verify == 'fruit':
        endline()
        createPart(fruit_type)
        endline()
        createPart(fruit_growth)
        endline()
        createPart(veg_size)
        createPart(veg_style)
        endline()
        createPart(veg_tex)
        createPart(sec_tex)
        if verify == 'yes':
            createPart(second)
            endline()
        else:
            endline()
            verify = ''            
    else:
        endline()
        createPart(veg_type)
        endline()
        createPart(fruit_growth)
        endline()
        createPart(veg_size)
        createPart(veg_style)
        endline()
        createPart(veg_tex)
        createPart(sec_tex)
        if verify == 'yes':
            createPart(second)
            endline()
        else:
            endline()
            verify = ''     

def createPlant():
    typeChoose()


def get():
    innieS = input('Plant Amount: ')
    print()
    endline()
    try:
        int(innieS)
    except ValueError:
        endline()
        print('Input must be an Integer\nRestart Application')
        endline()
        exit()
    innieI = int(innieS)
    innieR = range(int(innieS))
    global numcounter
    while numcounter < innieI:
        print('Plant Number: ' + str(numcounter + 1) + '\n')
        typeChoose()
        numcounter = numcounter+1
        innieI == innieI - 1
        print('********************************')
        endline()
    numcounter = 0

endline()

frank = 0

while frank == 0:
    get()
    asking = input('Continue?\n\ny/n: ')
    endline()        
    if asking == 'y':
        endline()
        continue
    elif asking == 'n':
        print('Thank you')
        endline()
        exit()
    else:
        print('Not an acceptable input\nRestart application')
        endline()
        exit()
