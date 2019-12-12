from pygame import mixer
import os
def play():
    global i
    mixer.init()
    if(len(l)>i):
      path=l[0]+l[i]
      mixer.music.load(path)
      mixer.music.play()
      i+=1
    else:
        print("Oops no more song left to play")
def playprev():
    global i
    mixer.init()
    i-=2
    if(i>0):
      path=l[0]+l[i]
      mixer.music.load(path)
      mixer.music.play()
    else:
        print("Oops no more song left to play")
def stop():
    mixer.music.stop()
    print("Thanks for using this player")
    return 0
def pause():
    mixer.music.pause()
def resume():
    mixer.music.unpause()
l=[]
i=1
a="D:\\Music shuffle\\"
l=os.listdir("D:\Music shuffle")
l=[a]+l
x=1
while(x):
    print("what do you wanna do?")
    print("0.Play a song")
    print("1.Play next song")
    print("2.Play previous song")
    print("3.Stop")
    print("4.Pause")
    print("5.Resume")
    y=int(input())
    if(y==0):
        play()   
    elif(y==1):
        play()
    elif(y==2):
        playprev()
    elif(y==3):
        x=stop()
    elif(y==4):
        pause()
    else:
        resume()
        
