


import sys
if 'google.colab' in sys.modules:
    import subprocess 
    subprocess.call('apt-get install subversion'.split())
    subprocess.call('svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_04b_hough_transform/ex4b/coins.png'.split())


from matplotlib import pyplot as plt
import cv2

figsize = (10, 10)


im3 = cv2.imread("coins.png")
im3 = cv2.cvtColor(im3, cv2.COLOR_BGR2RGB)
im = cv2.cvtColor(im3, cv2.COLOR_RGB2GRAY)
res = im3.copy()


acc_ratio = 1.2
min_dist = 40
canny_upper_th = 150
acc_th = 55

circles = cv2.HoughCircles(im, cv2.HOUGH_GRADIENT, acc_ratio,
                           min_dist, param1=canny_upper_th,
                           param2=acc_th, minRadius=40, maxRadius=70).astype(int)

#=== font vars
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale = 0.8
fontColor = (0,0,0)
lineType = 2
def dist_to_coin(dist):
    if  dist <= 67 and dist >= 61:
        return "Quarter"
    elif  dist <= 52 and dist >=43:
        return "Dime"
    elif dist <= 61 and dist >=52:
        return "Nickel"
    elif dist <=73 and dist >= 67:
        return "Dollar"
    elif dist <=52 and dist >= 50:
        return "Penny"
    elif dist <= 84 and dist >= 77:
        return "Half Dollar"
    else:   
        return dist.astype(str)
# ==== for each detected circle
for xyr in circles[0, :]:
    # draw the outer circle
    res = cv2.circle(res, (xyr[0], xyr[1]), xyr[2], (0, 255, 0), 3)
    cv2.putText(res, dist_to_coin((xyr[2])), (xyr[0], xyr[1]), font, fontScale, fontColor, lineType)  
    
    
    pass



plt.figure(figsize=figsize)
plt.imshow(res)
plt.title("final result- coins detection")
plt.show()

# %%