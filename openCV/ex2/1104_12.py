import cv2 , matplotlib.pyplot as plt , matplotlib.animation as ani

cap = cv2.VideoCapture(0);
fig = plt.figure(figsize=(10,6));
fig.canvas.manager.set_window_title("video Capture");
plt.axis('off');

def init():
    global im;
    retval,frame = cap.read();
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB));
    # return im,
def updateFrame(k):
    global im;
    retval,frame = cap.read();
    if retval:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB));

animation = ani.FuncAnimation(fig,updateFrame,init_func = init,interval =50 );
# ani.FuncAnimation(fig,updateFrame,init_func = init,interval =50 );
plt.show();
if cap.isOpened():
    cap.release();    