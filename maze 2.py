import numpy as np
import random as rand
import matplotlib.pyplot as plt
import math as m
import matplotlib.image as img

filename=input("Please input name of the picture file (with file ending): ")
pics=img.imread(filename) #takes in row, column, colour
print("Maze name: "+filename)
#blue = [0,0,1] = start, red = [1,0,0] = end, white = [1,1,1] = wall,
#black = [0,0,0] = path

#yellow = 0 for start, finish, or path, 1 for wall:
maze=pics[:,:,1];
m1=maze
m0=pics[:,:,0]
m2=pics[:,:,2]

dims=m0.shape

one=np.ones(dims)

T1=one-m1

xcheck=m2+T1

X0=np.argwhere(xcheck==2)
ec=np.argwhere(m0+T1==2)

victory=5 #must be >3

maze[ec[0,0],ec[0,1]]=victory

print(maze)

rounds=int(input("How many tries to optimise should I have? (at least 1, dude): "))+1

step0=200000
fails0=0
d=np.array([-1, 0, 1])
X0=np.flip(X0,1)
percentages=0
print("Optimising %i times for a total of %i runs." %(rounds-1,rounds))
for r in range(rounds):
    X=X0.copy()
    X=np.transpose(X,axes=None)
    p=X.copy()
    Xfails=X.copy()
    
    J=1

    steps=0

    V=np.array([[0,0]])
    V=np.transpose(V)

    #--------initial velocity definition
    if maze[X0[0,1]+1,X0[0,0]]==0:
        v0=np.array([[0,1]])
    elif maze[X0[0,1]-1,X0[0,0]]==0:
        v0=np.array([[0,-1]])
    elif maze[X0[0,1],X0[0,0]+1]==0:
        v0=np.array([[1,0]])
    elif maze[X0[0,1],X0[0,0]-1]==0:
        v0=np.array([[-1,0]])

    fails=0

    percentages=percentages+1
    print(str(m.floor(percentages))+" out of %i done" %(rounds))

    v0=np.transpose(v0)
    #----Some loop should start here
    while J==1 and steps<step0:

        vt=np.flipud(v0)
        Xp=X+v0
        Xt1=X+vt
        Xt2=X-vt

        K=maze[Xp[1],Xp[0]]+maze[Xt1[1],Xt1[0]]+maze[Xt2[1],Xt2[0]]
        #Corners/straight lines:
        if K==2:
            if maze[Xp[1],Xp[0]]==0: #primary direction
                X=X+v0
                p=np.append(p,X,axis=1)
            elif maze[Xt1[1],Xt1[0]]==0:
                v0=vt.copy()
                X=X+v0
                p=np.append(p,X,axis=1)
            elif maze[Xt2[1],Xt2[0]]==0:
                v0=-vt.copy()
                X=X+v0
                p=np.append(p,X,axis=1)

        #Branches/T-sections/open wall:
        elif K==1:
            if maze[Xt1[1],Xt1[0]]==0 and maze[Xt2[1],Xt2[0]]==0:#1,2
                vrand=np.array([np.transpose(vt),np.transpose(-vt)])
                a=rand.randint(0,1)
                v0=vrand[a]
                v0=np.transpose(v0)
                X=X+v0
                p=np.append(p,X,axis=1)
            elif maze[Xt1[1],Xt1[0]]==0 and maze[Xp[1],Xp[0]]==0:#0,1
                vrand=np.array([np.transpose(vt),np.transpose(v0)])
                a=rand.randint(0,1)
                v0=vrand[a]
                v0=np.transpose(v0)
                X=X+v0
                p=np.append(p,X,axis=1)

            elif maze[Xt2[1],Xt2[0]]==0 and maze[Xp[1],Xp[0]]==0: #0,2
                vrand=np.array([np.transpose(-vt),np.transpose(v0)])
                a=rand.randint(0,1)
                v0=vrand[a]
                v0=np.transpose(v0)
                X=X+v0
                p=np.append(p,X,axis=1)
                

        #Victory:
        elif K>=victory:
            if maze[Xp[1],Xp[0]]==victory: #primary direction
                X=X+v0
                p=np.append(p,X,axis=1)
                J=0
            elif maze[Xt1[1],Xt1[0]]==victory:
                v0=vt.copy()
                X=X+v0
                p=np.append(p,X,axis=1)
                J=0
            elif maze[Xt2[1],Xt2[0]]==victory:
                v0=-vt.copy()
                X=X+v0
                p=np.append(p,X,axis=1)
                J=0
        #empty spaces:
        elif K==0: #open, 0,1,2
            vrand=np.array([np.transpose(vt),np.transpose(-vt),np.transpose(v0)])
            a=rand.randint(0,2)
            v0=vrand[a]
            v0=np.transpose(v0)
            X=X+v0
            p=np.append(p,X,axis=1)
        #Dead ends
        elif K==3:
            fails+=1
            Xfails=np.append(Xfails,X,axis=1)
            v0=-v0
            X=X+v0
            p=np.append(p,X,axis=1)
        steps+=1
    if steps<step0:
        step0=steps
        p0=p.copy()
        Xfails0=Xfails.copy()
        fails0=fails
        runnr=r





mazecords=np.argwhere(maze==0)

        
            



p0[1,:]=-p0[1,:]
print("done")
print("Steps=%i after %i optimisation rounds" %(step0, runnr))
print("Fails = %i" %(fails0))
plt.plot(mazecords[:,1],-mazecords[:,0],'k.')
plt.plot(p0[0,:],p0[1,:],'-')
plt.plot(Xfails0[0,1:],-Xfails0[1,1:],'.')
plt.plot(X0[0,0],-X0[0,1],'g*')
plt.plot(ec[0,1],-ec[0,0],'r*')
plt.title("Shortest found path on "+filename+", best out of %i optimisation rounds,\n found at op.rnd. %i." %(rounds-1,runnr))
plt.show()
