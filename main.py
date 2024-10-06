import time 
from tkinter import *
import random
from audioplayer import AudioPlayer
import threading
# start = time.time()
# timePassed = time.time() - start
speed = 50
move_snake_number_XY = {
    "x1":50,
    "y1":0,
    "x2":100,
    "y2":50,
}

move_snake_number_wh = 50
timePassed_old = 0

applePositionY = 50 * random.randint(0, 9)
applePositionX = 50 * random.randint(0, 11)
bool_snake = True
check_num_snake = 0

def fun_audio():
    AudioPlayer("8d3b1fa30e92ead.mp3").play(block=True)



def time_fun():
    return time.time() - start
def keyPress(event):
    global move_snake
    # canV.config(bg="black")
    if(event.keysym == "Up" or event.keysym =="Down" or event.keysym =="Left" or event.keysym =="Right"):
        move_snake = event.keysym
    if(event.keysym == "0"):
        global bool_snake
        # global canV
        bool_snake = False
        canV.place(x=-1000,y=-1000)
        start_b.config(text="restart")
        # start_text.config(text="ваш рекорд: "+ str(check_num_snake))
        with open("record.txt",'r') as file:
            fileRead = file.read()
            start_text.config(text="ваш рекорд: "+ str(fileRead))
    # if(event.keysym == "")
    # if (event.keysym == "Left"):
    # if (event.keysym == "Down"):
    #     canV.create_rectangle(0, 0, 600, 500,fill='white', outline='white')
    #     canV.create_rectangle(0  + timePassed * speed, 0, 50  + timePassed * speed, 50,fill='black', outline='green')
def moving_body_snake():
    arr_move_snake_number_copy = arr_move_snake_number.copy()
    for i in range(len(arr_move_snake_number)):
        i = len(arr_move_snake_number) - (i+1)
        if(i!=0):
            arr_move_snake_number[i]["move_snake_number_y"] = arr_move_snake_number_copy[i-1]["move_snake_number_y"]
            arr_move_snake_number[i]["move_snake_number_x"] = arr_move_snake_number_copy[i-1]["move_snake_number_x"]
                        
 
root = Tk()
root.geometry('600x500')

 



def fun_start():
    bool_snake = True
    global start
    global applePositionY
    global applePositionX
    global move_snake_old
    global canV
    global arr_move_snake_number
    global move_snake
    global move_snake_old
    global check_num_snake
    move_snake = "Right"
    move_snake_old = "Right"
    arr_move_snake_number = [
        {
            "move_snake_number_x" :50,
            "move_snake_number_y" : 0,
            "image_snake":None,
        },
        {
            "move_snake_number_x" : 0,
            "move_snake_number_y" : 0,
            "image_snake":None,
        },
    ]
    check_num_snake = 0
    canV = Canvas(width=600, height=500, bg='white')
    text_l = Label(text="ответ:")
    canV.pack()
    
    canV.create_rectangle(arr_move_snake_number[0]["move_snake_number_x"], arr_move_snake_number[0]["move_snake_number_y"], arr_move_snake_number[0]["move_snake_number_x"] + move_snake_number_wh, arr_move_snake_number[0]["move_snake_number_y"] + move_snake_number_wh,fill='green', outline='green')

    canV.create_rectangle(applePositionX, applePositionY, applePositionX + move_snake_number_wh, applePositionY + move_snake_number_wh,fill='green', outline='green')

    
    check_text_snake = Label(text="счёт: " + str(check_num_snake), font="system 16", bg = "#ffffff")
    check_text_snake.place(h=18 , w=66 ,x=520 ,y=10)

    start = time.time()
    timePassed = time.time() - start
    while(timePassed <= 100000 and bool_snake):

        timePassed_old = timePassed
        timePassed = time_fun()
        # print(timePassed , timePassed_old)
        # print(round(timePassed))
        canV.update()
        root.bind("<KeyPress>" , keyPress)
        # print(move_snake)
        if(move_snake == "Right" and round(timePassed_old) != round(timePassed)):
                if(move_snake_old == "Left"):
                    moving_body_snake()
                    arr_move_snake_number[0]["move_snake_number_x"] -= speed
                else: 
                    moving_body_snake()
                    arr_move_snake_number[0]["move_snake_number_x"] += speed
                    move_snake_old = move_snake
        if(move_snake == "Left" and round(timePassed_old) != round(timePassed)):
                if(move_snake_old == "Right"):
                    moving_body_snake()
                    arr_move_snake_number[0]["move_snake_number_x"] += speed
                else: 
                    moving_body_snake()
                    arr_move_snake_number[0]["move_snake_number_x"] -= speed
                    move_snake_old = move_snake
        elif(move_snake == "Down" and round(timePassed_old) != round(timePassed)):
                if(move_snake_old == "Up"):
                    moving_body_snake()
                    arr_move_snake_number[0]["move_snake_number_y"] -= speed
                else: 
                    moving_body_snake()
                    arr_move_snake_number[0]["move_snake_number_y"] += speed
                    move_snake_old = move_snake
        elif(move_snake == "Up" and round(timePassed_old) != round(timePassed)):
                if(move_snake_old == "Down"):
                    moving_body_snake()
                    arr_move_snake_number[0]["move_snake_number_y"] += speed
                else:
                    moving_body_snake()
                    arr_move_snake_number[0]["move_snake_number_y"] -= speed
                    move_snake_old = move_snake
                            
    
        if(arr_move_snake_number[0]["move_snake_number_y"] == applePositionY and arr_move_snake_number[0]["move_snake_number_x"] == applePositionX):
            # canV.create_rectangle(arr_move_snake_number[0]["move_snake_number_x"], arr_move_snake_number[0]["move_snake_number_y"], arr_move_snake_number[0]["move_snake_number_x"] + move_snake_number_wh, arr_move_snake_number[0]["move_snake_number_y"] + move_snake_number_wh,fill='green', outline='green')
            
            # AudioPlayer("8d3b1fa30e92ead.mp3").play(block=True)
            thread_fun = threading.Thread(target=fun_audio)
            thread_fun.start()
            if(move_snake == "Right"):
                arr_move_snake_number.append({
                    "move_snake_number_x" : arr_move_snake_number[len(arr_move_snake_number)-1]["move_snake_number_x"] - speed,
                    "move_snake_number_y" : arr_move_snake_number[len(arr_move_snake_number)-1]["move_snake_number_y"],
                    "image_snake":None,
                })
            elif(move_snake == "Left"):
                arr_move_snake_number.append({
                    "move_snake_number_x" : arr_move_snake_number[len(arr_move_snake_number)-1]["move_snake_number_x"] + speed,
                    "move_snake_number_y" : arr_move_snake_number[len(arr_move_snake_number)-1]["move_snake_number_y"],
                    "image_snake":None,
                })
            elif(move_snake == "Down"):
                arr_move_snake_number.append({
                    "move_snake_number_x" : arr_move_snake_number[len(arr_move_snake_number)-1]["move_snake_number_x"],
                    "move_snake_number_y" : arr_move_snake_number[len(arr_move_snake_number)-1]["move_snake_number_y"] - speed,
                    "image_snake":None,
                })
            elif(move_snake == "Up"):
                arr_move_snake_number.append({
                    "move_snake_number_x" : arr_move_snake_number[len(arr_move_snake_number)-1]["move_snake_number_x"],
                    "move_snake_number_y" : arr_move_snake_number[len(arr_move_snake_number)-1]["move_snake_number_y"] + speed,
                    "image_snake":None,
                })
            check_num_snake += 1
            check_text_snake.config(text="счёт: "+str(check_num_snake))
            fileRead = open("record.txt",'r').read()
            if check_num_snake > int(fileRead):
                # fileRead.close()
                # with open("record.txt",'r') as file:
                #         file.write(str(check_num_snake))
                file = open("record.txt",'w')
                file.write(str(check_num_snake))
                file.close()
            for i in arr_move_snake_number:
                while(i["move_snake_number_y"] == applePositionY and i["move_snake_number_x"] == applePositionX):
                    applePositionY = 50 * random.randint(0, 9)
                    applePositionX = 50 * random.randint(0, 11)
            
        canV.create_rectangle(0, 0, 600, 500,fill='white', outline='white')
        apple_png = PhotoImage(file="assets/яблоко.png")
        canV.create_image(applePositionX + 25, applePositionY + 25,image=apple_png)
        # print(round(timePassed))
        for i in range(len(arr_move_snake_number)):
            string_foto = "assets/"
            if(i == 0):
                string_foto += "голова змеи"
            elif(i == len(arr_move_snake_number) - 1):
                string_foto += "хвост змеи"
            else:
                string_foto += "тело змеи"



            if(i < len(arr_move_snake_number) - 1):
                if(arr_move_snake_number[i+1]["move_snake_number_x"] < arr_move_snake_number[i]["move_snake_number_x"]):
                    string_foto += "RIGHT"
                    # arr_move_snake_number[i]["image_snake"] = PhotoImage(file="assets/голова змеиRIGHT")
                elif(arr_move_snake_number[i+1]["move_snake_number_x"] == arr_move_snake_number[i]["move_snake_number_x"]):
                    if(arr_move_snake_number[i+1]["move_snake_number_y"] < arr_move_snake_number[i]["move_snake_number_y"]):
                        string_foto += "DOWN"
                        # arr_move_snake_number[i]["image_snake"] = PhotoImage(file="assets/голова змеиDOWN.png")
                    else:
                        string_foto += "UP"
                        # arr_move_snake_number[i]["image_snake"] = PhotoImage(file="assets/голова змеиUP.png")
                else:
                    string_foto += "LEFT"
                    # arr_move_snake_number[i]["image_snake"] = PhotoImage(file="assets/голова змеиLEFT.png")
            if(i > 0):
                if(arr_move_snake_number[i-1]["move_snake_number_x"] < arr_move_snake_number[i]["move_snake_number_x"]):
                    string_foto += "RIGHT"
                    # arr_move_snake_number[i]["image_snake"] = PhotoImage(file="assets/голова змеиRIGHT.png")
                elif(arr_move_snake_number[i-1]["move_snake_number_x"] == arr_move_snake_number[i]["move_snake_number_x"]):
                    if(arr_move_snake_number[i-1]["move_snake_number_y"] < arr_move_snake_number[i]["move_snake_number_y"]):
                        string_foto += "DOWN"
                        # arr_move_snake_number[i]["image_snake"] = PhotoImage(file="assets/голова змеиDOWN.png")
                    else:
                        string_foto += "UP"
                        # arr_move_snake_number[i]["image_snake"] = PhotoImage(file="assets/голова змеиUP.png")
                else:
                    string_foto += "LEFT"
                    # arr_move_snake_number[i]["image_snake"] = PhotoImage(file="assets/голова змеиLEFT.png")



            string_foto+= ".png"
            print(string_foto)
            arr_move_snake_number[i]["image_snake"] = PhotoImage(file=string_foto)
            canV.create_image(arr_move_snake_number[i]["move_snake_number_x"] +25, arr_move_snake_number[i]["move_snake_number_y"] + 25,image=arr_move_snake_number[i]["image_snake"])
        if (arr_move_snake_number[0]["move_snake_number_x"]<0 or arr_move_snake_number[0]["move_snake_number_x"]>550 or arr_move_snake_number[0]["move_snake_number_y"]<0 or arr_move_snake_number[0]["move_snake_number_y"]>450):
            bool_snake = False
            canV.place(x=-1000,y=-1000)
            start_b.config(text="restart")
            with open("record.txt",'r') as file:
                fileRead = file.read()
            start_text.config(text="ваш рекорд: "+ str(fileRead))
                    # global bool_snake
        for x in range(len(arr_move_snake_number)):
            for y in range(len(arr_move_snake_number)):
                # print(arr_move_snake_number[y]["move_snake_number_y"])
                if(x!=y and arr_move_snake_number[x]["move_snake_number_x"] == arr_move_snake_number[y]["move_snake_number_x"] and arr_move_snake_number[x]["move_snake_number_y"] == arr_move_snake_number[y]["move_snake_number_y"]):
                    bool_snake = False
                    canV.place(x=-1000,y=-1000)
                    start_b.config(text="restart")
                    with open("record.txt",'r') as file:
                        fileRead = file.read()
                    start_text.config(text="ваш рекорд: "+ str(fileRead))
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        # canV.create_rectangle(0  + round(timePassed) * speed, 0, 50  + round(timePassed) * speed, 50,fill='green', outline='green')


def hover(event): 
    start_b.config(bg = "#641bf8")
def not_hover(event):
    start_b.config(bg = "#925cff")
start_b = Button(text="start", command=fun_start , bg = "#925cff", font="system 16")
start_b.place(h=40 , w=80 ,x=300-40 ,y=250-20)
start_b.bind("<Enter>", hover)
start_b.bind("<Leave>", not_hover)
with open("record.txt",'r') as file:
    fileRead = file.read()
start_text = Label(text="ваш рекорд: "+ str(fileRead), font="system 13", state=["disabled"])
start_text.place(h=40 , w=160 ,x=300-80 ,y=160)



        



root.bind("<KeyPress>" , keyPress)
# root.bind("<KeyRelease>" , keyRelease)

 


 
root.mainloop()