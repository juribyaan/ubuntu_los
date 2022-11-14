import cv2 , numpy as np , matplotlib.pyplot as plt , matplotlib.animation as animation

class Video(animation.FuncAnimation):
    def __init__(self , device = 0 , fig = None , frames =None, interval = 80 , repeat_delay = 5 , blit = False, **kwargs):
        if fig is None:
            self.fig, self.ax = plt.subplots( 1, 2, figsize = (10 , 5))
            self.fig.canvas.manager.set_window_title('Video Capture')
            self.ax[0].set_position([ 0, 0 , 0.5 ,1 ])
            self.ax[0].axis('off')
            
            self.ax[1].set_position([ 0.5 , 0 , 0.5 , 1])
            self.ax[1].axis('off')
                
            # plt.subplots_adjust(left = 0, bottom = 0, 
            #                       tright =1 , op = 1 , 
            #                       wspace = 0.05, hspace = 0.05)
        super(Video ,self).__init__(self.fig , self.updateFrame, init_func = self.videoInit, frames= frames, interval = interval , blit = blit , repeat_delay = repeat_delay, **kwargs)
        self.cap = cv2.VideoCapture(device)
        print('시작 ...')
        
    def videoInit(self):
        retval,self.frame = self.cap.read()
        if retval:
            self.im0 = self.ax[0].imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB), aspect = 'auto')
            self.im1 = self.ax[1].imshow(np.zeros(self.frame, self.frame.dtype), aspect = 'auto')
            
    def updateFrame(self, k ):
        retval, self.frame = self.cap.read()
        if retval:
            self.im0.set_array(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.im1.set_array(cv2.merge((gray,gray,gray)))
    
    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print('캡쳐 끝.')
        
camera = Video()
plt.show()
camera.close()