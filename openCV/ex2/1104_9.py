import cv2 ,pafy
# import youtube_dl
# import yt_dlp
# url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
url = 'https://www.youtube.com/watch?v=qVK16wH0isA'
video = pafy.new(url)
print('title =' , video.title)
print('video.rating =' , video.rating)
print('video.duration =' , video.duration)
best = video.getbest() #video.getbest(preftype = 'mp4')



print('best.resolution', best.resolution)

cap = cv2.VideoCapture(best.url)
# cap = cv2.VideoCapture('https://www.youtube.com/shorts/S4c-SEv2W8A')
# frame_size = (
#     int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
#     int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
# )
while True:
    retval, frame = cap.read()
    if not retval:
        break
    cv2.imshow('frame',frame)
    
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # edges = cv2.Canny(gray,100,200)
    # cv2.imshow('edges',edges)
    key = cv2.waitKey(25)
    if key == 27:  #ESC
        break
if cap.isOpened():
    cap.release()
# cv2.destroyAllWindows()
