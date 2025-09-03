#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** Aug 2025 **********************************
#*******************************************************************************
import tkinter
import random

#-------------------- Basic Info --------------------
Tile_Size = 20 #px
Num_of_Rows = 30 #Number of Tiles
Num_of_Columns = 50 #Number of Tiles
Window_Width = Tile_Size * Num_of_Columns #px
Window_Height = Tile_Size * Num_of_Rows #px
Score = -1 #Number of Foods
Game_Over = False

#-------------------- Creates Window --------------------
window = tkinter.Tk()
window.title( "Snake Game" )
window.resizable( False , False )
window.geometry( "+0+0" )

#-------------------- Creates Canvas for Game --------------------
canvas = tkinter.Canvas( window ,
                         bg = "black" ,
                         width = Window_Width ,
                         height = Window_Height
                         )
canvas.pack()
window.update()

#-------------------- Creates Wall --------------------
canvas.create_rectangle( 0 , 0 ,
                         Window_Width , Window_Height ,
                         outline = "blue" ,
                         width = Tile_Size
                         )

#-------------------- Snake Properties --------------------
Snake_Segments = []
Snake_Velocity = [Tile_Size,0]

#-------------------- Snake Controls --------------------
def Draw_Segment(x,y,color):
    canvas.create_rectangle( x , y ,
                             x + Tile_Size , y + Tile_Size ,
                             fill = color
                             )

def Add_Segment(x,y):
    global Snake_Segments
    Snake_Segments.append( [x,y] )
    Draw_Segment( x , y , "green" )

def Delete_Tail():
    global Snake_Segments
    Draw_Segment( Snake_Segments[0][0] ,
                  Snake_Segments[0][1] ,
                  "black" )
    Snake_Segments.pop(0)

def Move_Snake():
    Head = len(Snake_Segments) - 1
    x = Snake_Segments[Head][0] + Snake_Velocity[0]
    y = Snake_Segments[Head][1] + Snake_Velocity[1]
    Add_Segment(x,y)
    Delete_Tail()

def Change_Direction(evt):
    global Snake_Velocity
    
    if ( evt.keysym == "Up" and Snake_Velocity[1] != Tile_Size ):
        Snake_Velocity[0] = 0
        Snake_Velocity[1] = -Tile_Size
    
    elif ( evt.keysym == "Down" and Snake_Velocity[1] != -Tile_Size ):
        Snake_Velocity[0] = 0
        Snake_Velocity[1] = Tile_Size
    
    elif ( evt.keysym == "Left" and Snake_Velocity[0] != Tile_Size ):
        Snake_Velocity[0] = -Tile_Size
        Snake_Velocity[1] = 0
    
    elif ( evt.keysym == "Right" and Snake_Velocity[0] != -Tile_Size ):
        Snake_Velocity[0] = Tile_Size
        Snake_Velocity[1] = 0

window.bind( "<KeyRelease>" , Change_Direction )

Add_Segment( Window_Width/2 - Tile_Size/2 ,
             Window_Height/2 - Tile_Size/2
             )

#-------------------- Food Controls --------------------
def Random_Tile():
    x = Tile_Size * random.randint( 5 , Num_of_Columns - 5 ) - Tile_Size/2
    y = Tile_Size * random.randint( 5 , Num_of_Rows - 5 ) - Tile_Size/2
    return [x,y]

def Move_Food():
    global Food
    
    #Make Sure Food Doesn't Appear Inside Body
    FoodCheck = 1
    while FoodCheck > 0:
        Food = Random_Tile()
        FoodCheck = 0
        for Segment in Snake_Segments:
            if( Food == Segment ):
                FoodCheck += 1
    
    #Display Food
    canvas.create_oval( Food[0] , Food[1] ,
                        Food[0] + Tile_Size , Food[1] + Tile_Size ,
                        fill = "red"
                        )

def Increase_Score():
    global Score
    
    #Increase Score Value
    Score += 1
    
    #Erase Old Score
    canvas.create_rectangle( Window_Width - 7*Tile_Size , Tile_Size ,
                             Window_Width - 2*Tile_Size , 2*Tile_Size ,
                             fill = "black"
                             )
    
    #Display New Score
    canvas.create_text( Window_Width - 5*Tile_Size , 1.5*Tile_Size ,
                        text = "Score: " + str(Score) ,
                        font = ('Times New Roman', 15, 'bold') ,
                        fill = "white"
                        )
    
    #Move Food to New Random Location
    Move_Food()

Increase_Score()

#-------------------- Game Over Message --------------------
def Game_Over_Text():
    canvas.create_text( Window_Width/2 , Window_Height/2 ,
                        text = "You lost, but that's okay. Everyone's a loser sometimes." ,
                        fill = "white"
                        )

#-------------------- Time Passes --------------------
def Play_Game():
    global Game_Over
    
    #Location of Head
    Head = len(Snake_Segments) - 1
        
    #Check If Hit Wall
    if( Snake_Segments[Head][0] <= 0 ):
        Game_Over = True
    if( Snake_Segments[Head][0] >= Window_Width - Tile_Size ):
        Game_Over = True
    if( Snake_Segments[Head][1] <= 0 ):
        Game_Over = True
    if( Snake_Segments[Head][1] >= Window_Height - Tile_Size ):
        Game_Over = True
    
    #Check If Hit Body
    if( Head > 3 ):
        for Segment in Snake_Segments[0:Head-3]:
            if( Snake_Segments[Head] == Segment ):
                Game_Over = True
    
    #Check for Game Over Condition
    if( Game_Over == True ):
        Game_Over_Text()
    else:
        #Normal Snake Movement
        Move_Snake()
        
        #Check for Food Eaten
        if( Snake_Segments[Head] == Food ):
            x = Snake_Segments[Head][0] + Snake_Velocity[0]
            y = Snake_Segments[Head][1] + Snake_Velocity[1]
            Add_Segment(x,y)
            Increase_Score()
    
        #Loops Play_Game After Time in Milliseconds
        window.after( 100 , Play_Game )

Play_Game()
window.mainloop()