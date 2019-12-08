# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:00:55 2019

@author: Jerry
"""
import cv2
import numpy as np
import pandas as pd
# load selected image

def image_output(directory, image):
    """
    test
    """
    # dir = "userData/"
    # imge = "user1.jpg"
    image_loc = directory + image
    csv_loc = directory + 'selected_image.csv'
    img = cv2.imread(image_loc, 0)
    img2 = np.asarray(img).reshape(-1)
    num = 400
    img_data = []
    for i in range(0, num):
        j = i * 100 + 1
        sum_img = sum(img2[j:100 + j])
        avg_img = sum_img / 100
        img_data.append(avg_img)
    df_img = pd.DataFrame(img_data, columns=['CatID'])
    df_img.to_csv(csv_loc)