import random
import cisc106
import math
import matplotlib.pyplot as plt
import json
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PUMPKIN_X=100
PUMPKIN_Y_MIN=0
PUMPKIN_Y_MAX=SCREEN_HEIGHT//4
PUMPKIN_ANGLE_MIN=0
PUMPKIN_ANGLE_MAX=80
PUMPKIN_v0_MIN=10
PUMPKIN_v0_MAX=100
GRAVITY=9.81

def get_valid_integer(minimum,maximum):
    '''
    Repeatedly asks user for an input until their input is an integer
    that falls within the range give by minimum and maximum values
    Parameters: 
        minimum: (int) - the lower bound of the range (inclusive)
        maximum: (int) - the upper bound of the range (inclusive)
    Returns:
        integer: (int)
    '''
    test=True
    while test==True:
        integer=input('Enter a value between ' + str(minimum) + ' and ' + str(maximum) + ': ')
        if integer.isdigit()==True:
            x=int(integer)
            if minimum<=x<=maximum:
                return x
                test=False
    
def set_up_target():
    '''
    Computes the x and y coordinates of the target
    No Parameters
    Returns:
    x_target: (int)- x coordinate of target
    y_target: (int)- y coordinate of target
    '''
    x_target=650 #designats the x coordinate of the target
    y_target=90 #designates the y coordinate of the target
    print('X coordinate of target:'+ str(x_target))
    print('Y coordinate of target:'+ str(y_target))
    return(x_target,y_target) 

def get_init_pumpkin_height():
    '''
    Calls upon the get_valid_integer() function to reveive a pumpkin height value from the user
    that is within the range of [PUMPKIN_Y_MIN,PUMPKIN_Y_MAX]
    No Parameters
    Returns:
        x: (int)
    '''
    x=get_valid_integer(PUMPKIN_Y_MIN,PUMPKIN_Y_MAX) #runs the function get_valid_integer() with arguments PUMPKIN_Y_MIN,PUMPKIN_Y_MAX to get an integer from the user within this range
    return(x)

def get_pumpkin_angle():
    '''
    Calls upon the get_valid_integer() function to reveive a pumpkin angle value from the user
    that is within the range of [PUMPKIN_ANGLE_MIN,PUMPKIN_ANGLE_MAX]
    No Parameters
    Returns:
        x: (int)
    '''
    x=get_valid_integer(PUMPKIN_ANGLE_MIN,PUMPKIN_ANGLE_MAX) #runs the function get_valid_integer() with arguments PUMPKIN_ANGLE_MIN,PUMPKIN_ANGLE_MAX to get an integer from the user within this range
    return(x)
    return(x)

def get_pumpkin_v0():
    '''
    Calls upon the get_valid_integer() function to reveive a pumpkin initial velocity value from the user
    that is within the range of [PUMPKIN_V0_MIN,PUMPKIN_V0_MAX]
    No Parameters
    Returns:
        x: (int)
    '''
    x=get_valid_integer(PUMPKIN_v0_MIN,PUMPKIN_v0_MAX) #runs the function get_valid_integer() with arguments PUMPKIN_v0_MIN,PUMPKIN_v0_MAX to get an integer from the user within this range
    return(x)
    
def compute_vx_vy(v_pumpkin,angle_pumpkin):
    '''
    Computes the initial x and y velocity of the pumpkin given the initial velocity and angle
    Parameters:
        v_pumpkin: (int)- The initial velocity of the pumpkin
        angle_pumpkin: (int)- The initial angle of the pumpkin
    Returns:
        vx: (int)- the initial x velocity
        vy: (int)- the initial y velocity
    '''
    vx = round(v_pumpkin * math.cos(math.radians(angle_pumpkin)),2) #finds the x velocity 
    vy = round(v_pumpkin * math.sin(math.radians(angle_pumpkin)),2) #finds the y velocity
    return (vx,vy)
cisc106.assert_equal(compute_vx_vy (30, 25),  (27.19, 12.68))
cisc106.assert_equal(compute_vx_vy (80, 60),  (40.00, 69.28))
cisc106.assert_equal(compute_vx_vy (45, 20),  (42.29, 15.39))
cisc106.assert_equal(compute_vx_vy (10, 90),  (0.00, 10.0))
cisc106.assert_equal(compute_vx_vy (6, 45),  (4.24, 4.24))

def move_pumpkin(x_pumpkin,y_pumpkin,vx,vy):
    '''
    Computes the new x and y location as well as the new y velocity of the 
    pumpkin after 1 second of movement
    Parameters:
        x_pumpkin: (int)- the initial x coordinate of the pumpkin
        y_pumpkin: (int)- the initial y coordinate of the pumpkin
        vx: (int)- the initial x velocity of the pumpkin
        vy: (int)- the initial y velocity of the pumpkin
    Returns:
        x_pumpkin: (int)- the updated x coordinate of the pumpkin
        y_pumpkin: (int)- the updated y coordinate of the pumpkin
        vy: (int)- the updated y velocity of the pumpkin
    '''
    t=1
    xdistance=vx*t #equation for distance traveled in the x direction
    ydistance=(vy*t)-(GRAVITY*((t**2)/2)) #equation for distance traveled in the y direction
    x_pumpkin=round(x_pumpkin+xdistance,2) #equates the new position of the x coordinate
    y_pumpkin=round(y_pumpkin+ydistance,2)
    vy=round(vy-(GRAVITY*t),2)
    return(x_pumpkin,y_pumpkin,vy)
cisc106.assert_equal(move_pumpkin(100, 150, 20, 25), (120, 170.09, 15.19))
cisc106.assert_equal(move_pumpkin(300, 10, 50, -15), (350,-9.91, -24.81))
cisc106.assert_equal(move_pumpkin(200, 175, 10, 10), (210, 180.09, 0.19))
cisc106.assert_equal(move_pumpkin(150, 100, 50, 40), (200, 135.09, 30.19))
cisc106.assert_equal(move_pumpkin(50, 50, 50, 50), (100, 95.09, 40.19))

def is_target_hit(x_pumpkin,y_pumpkin,x_target,y_target):
    '''
    Computes whether the pumpkin hits the target
    Parameters:
        x_pumpkin: (int)- the x coordinate of the pumpkin
        y_pumpkin: (int)- the y coordinate of the pumpkin
        x_target: (int)- the x coordinate of the target
        y_target: (int)- the y coordinate of the target
    Returns:
        True: (bool)- returned if the pumpkin hits the target
        False: (bool)- returned if the pumpkin misses the target
    '''
    if (x_pumpkin-15)<=(x_target)<=(x_pumpkin+15) and (y_pumpkin-15)<=(y_target)<=(y_pumpkin+15):
        return True
    else:
        return False
cisc106.assert_equal(is_target_hit(450, 100, 460, 105), True)
cisc106.assert_equal(is_target_hit(450, 100, 460, 125), False)
cisc106.assert_equal(is_target_hit(110, 200, 30, 200), False)
cisc106.assert_equal(is_target_hit(500, 300, 510, 275), False)
cisc106.assert_equal(is_target_hit(400, 400, 400, 400), True)

def is_off_screen(x_pumpkin,y_pumpkin):
    '''
    Computes whether the final location of the pumpkin is off the screen
    Parameters:
        x_pumpkin: (int)- the final x coordinate of the pumpkin
        y_pumpkin: (int)- the final y coordinate of the pumpkin
    Returns:
        True: (bool)- returned if the pumpkin is off the screen
        False: (bool)- returned if the pumpkin is on the screen
    '''
    if x_pumpkin>SCREEN_WIDTH or y_pumpkin>SCREEN_HEIGHT or y_pumpkin<0:
        return True
    else:
        return False
cisc106.assert_equal(is_off_screen(100,-100), True)
cisc106.assert_equal(is_off_screen(800, 100),False)
cisc106.assert_equal(is_off_screen(440,440), False)
cisc106.assert_equal(is_off_screen(40, 600),False)
cisc106.assert_equal(is_off_screen(900, 100),True) 


def compute_trajectory(x_target,y_target,x_pumpkin,y_pumpkin,angle_pumpkin,v_pumpkin):
    vx,vy=compute_vx_vy(v_pumpkin,angle_pumpkin)
    listx=[]
    listy=[]
    listx.append(x_pumpkin)
    listy.append(y_pumpkin)
    t=1
    while is_off_screen(x_pumpkin,y_pumpkin)==False and is_target_hit(x_pumpkin,y_pumpkin,x_target,y_target)==False:
        x_pumpkin,y_pumpkin,vy=move_pumpkin(x_pumpkin,y_pumpkin,vx,vy)
        listx.append(x_pumpkin)
        listy.append(y_pumpkin)
    if is_target_hit(x_pumpkin,y_pumpkin,x_target,y_target)==True:
        print("Target hit!")
    if is_off_screen(x_pumpkin,y_pumpkin)==True:
        print("You Missed!")
    return(listx,listy)

def play_punkin_chunkin(x_target,y_target):
    '''
    Gives a brief description of the game, then asks the user for a height, angle, and velocity
    for the pumpkin, and then computes the trajectory of the pumpkin to see if it hits the target.
    Parameters:
        x_target-(int) x coordinate for the target
        y_target-(int) y coordinate for the target
    Returns:
        x_list-(list) list of all x values for the pumpkin
        y_list-(list) list of all y values for the pumpkin
        y_initial-(int) the initial height of the pumpkin
        angle_pumpkin-(int) the initial launch angle
        v_pumpkin-(int) the initial launch velocity
    '''
    #describes the game to the user
    print('Welcome to Punkin Chunkin! In this game, your goal is to launch a pumpkin and hit the target. In order to do so, choose a starting height, angle of launch, and initial speed. Good luck!')
    #sets up the target location
    #x_target,y_target=set_up_target()
    #gets the user's selection for the pumpkin's initial height
    print("Start by setting a starting height for your pumpkin:")
    y_pumpkin=get_init_pumpkin_height()
    y_initial=y_pumpkin
    #gets the user's selection for the pumpkin's initial angle
    print("Now an angle of trajectory for your pumpkin:")
    angle_pumpkin=get_pumpkin_angle()
    #gets the user's selection for the pumpkin's initial velocity
    print("Finally, choose an initial velocity for your pumpkin:")
    v_pumpkin=get_pumpkin_v0()
    x_pumpkin=PUMPKIN_X
    x_list,y_list=(compute_trajectory(x_target,y_target,x_pumpkin,y_pumpkin,angle_pumpkin,v_pumpkin))
    return(x_list,y_list,y_initial,angle_pumpkin,v_pumpkin)

def store_trial_data(x_list,y_list,y_initial,angle_pumpkin,v_pumpkin):
    '''
    Creates a dictionary assigning all essential values to a string name
    Parameters:
        x_list-(list) list of all x values for the pumpkin
        y_list-(list) list of all y values for the pumpkin
        y_initial-(int) the initial height of the pumpkin
        angle_pumpkin-(int) the initial launch angle
        v_pumpkin-(int) the initial launch velocity
    Returns:
        data_dict- (dict)
    '''
    data_dict={'x_vals':x_list,'y_vals':y_list,'init_height':y_initial,'angle':angle_pumpkin,'v0':v_pumpkin}
    return data_dict

def plot_trajectories(data_list,x_target,y_target):
    '''
    Takes a list of dictionaries containing all essential information for the pumpkin's
    trajectory, as well as the position of the target. Then plots the trajectory of the pumpkin
    and it's final spot, as well as the position of the target.
    Parameters:
        data_list: (list)- the list of dictionaries created in play_trial_rounds
        x_target: (int)- x position of the target
        y_target: (int)- y position of the target
    returns:
        fig: (tuple)
        ax: (tuple)
    '''
    fig,ax = plt.subplots()
    plt.xlim([0, SCREEN_WIDTH])
    plt.ylim([-100, SCREEN_HEIGHT])
    ax.grid()
    plt.title("Punkin Chunkin Trajectory")
    plt.xlabel("Distance")
    plt.ylabel("Height")
    target = plt.Circle((x_target,y_target), 25, color='g')
    ax.add_artist(target)
    colors=['y','m','c']
    for i in range(len(data_list)):
        
        x_values = data_list[i]['x_vals']
        y_values = data_list[i]['y_vals']
        ax.plot(x_values, y_values, color=colors[i], label= 'Height: ' + str(data_list[i]['y_vals'][0]) + "  Angle: " + str(data_list[i]['angle']) + '  Speed: ' + str(data_list[i]['v0']))
        pumpkin = plt.Circle((data_list[i]['x_vals'][-1],data_list[i]['y_vals'][-1]), 15, color=colors[i])
        ax.legend()
        ax.add_artist(pumpkin)

    
    plt.show()
    return(fig,ax)

def play_trial_rounds(x_target,y_target):
    '''
    Creates a list of dictionaries containing the returned values from play_punkin_chunkin,
    then passes these variables to plot_trajectories to make a graph
    Parameters:
        x_target: (int)- x value of the target
        y_target: (int)- y value of the target
    No Returns
    '''
    
    count=0
    data_list=[]
    while count<3:
        x_list,y_list,y_initial,angle_pumpkin,v_pumpkin=play_punkin_chunkin(x_target,y_target)
        data_dict=store_trial_data(x_list,y_list,y_initial,angle_pumpkin,v_pumpkin)
        data_list.append(data_dict)
        count+=1
        plot_trajectories(data_list,x_target,y_target)


def get_global_values(global_file):
    '''
    Converts the contents of a json file into dictionary
    Parameters:
        global_file: (file)- a json file
    No Returns
    '''
    file=open(global_file,'r')
    data=file.read()
    json_data=json.loads(data)
    file.close()
    return json_data

def set_global_values(dictionary):
    '''
    Takes a dictionary from get_global_values and assigns the values in the dictionary
    to the global variables
    Parameters:
        dictionary: (dict)- a dictionary
    No Returns
    '''
    global PUMPKIN_X
    global PUMPKIN_Y_MIN
    global PUMPKIN_Y_MAX
    global PUMPKIN_ANGLE_MIN
    global PUMPKIN_ANGLE_MAX
    global PUMPKIN_v0_MIN
    global PUMPKIN_v0_MAX
    
    PUMPKIN_X=dictionary["PUMPKIN_X"]
    PUMPKIN_Y_MIN=dictionary["PUMPKIN_Y_MIN"]
    PUMPKIN_Y_MAX=dictionary["PUMPKIN_Y_MAX"]
    PUMPKIN_ANGLE_MIN=dictionary["PUMPKIN_ANGLE_MIN"]
    PUMPKIN_ANGLE_MAX=dictionary["PUMPKIN_ANGLE_MAX"]
    PUMPKIN_v0_MIN=dictionary["PUMPKIN_v0_MIN"]
    PUMPKIN_v0_MAX=dictionary["PUMPKIN_v0_MAX"]

def play_game(global_file):
    print('Welcome to Punkin Chunkin! In this game, your goal is to launch a pumpkin and hit the target. In order to do so, choose a starting height, angle of launch, and initial speed. Good luck!')
    set_global_values(get_global_values(global_file))
    x_target,y_target=set_up_target()
    print('Now you will have three practice attempts to hit the target')
    play_trial_rounds(x_target,y_target)
play_game('initial_values.json')

