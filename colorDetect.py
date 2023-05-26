import pandas as pd
import cv2

img_path='colorUmb.jpeg'
csv_path='colors.csv'

index=["color","color_name","hex","R","G","B"]
data_frame=pd.read_csv(csv_path, names=index, header=None)

img=cv2.imread(img_path)
img=cv2.resize(img,(750,550))

clicked=False
r=g=b=xpos=ypos=0

def get_color_name(R,G,B):
    minimun=1000
    for i in range(len(data_frame)):
        d=abs(R-int(data_frame.loc[i,'R']))+abs(G-int(data_frame.loc[i,'G']))+abs(B-int(data_frame.loc[i,'B']))
        if d<=minimun:
            minimun = d
            cname= data_frame.loc[i,'color_name']

    return cname
    

def draw_function(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global clicked, r, g, b, xpos,ypos
        clicked=True
        xpos=x
        ypos=y
        
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while True:
    cv2.imshow('image',img)
    if clicked:
        cv2.rectangle(img,(22,22),(600,63),(b,g,r),-1)
        text=get_color_name(r,g,b)+' R='+str(r)+', G='+str(g)+', B='+str(b)
        cv2.putText(img,text,(40,50),5,1,(255,255,255),1,cv2.LINE_AA)
        if r+g+b>=550:
            cv2.putText(img,text,(40,50),5,1,(0,0,0),1,cv2.LINE_AA)
        clicked = False

    if cv2.waitKey(20)& 0xFF == 27:
        break

cv2.destroyAllWindows()