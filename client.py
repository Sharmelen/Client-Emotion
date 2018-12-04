import requests
import json
import cv2
import urllib
import numpy as np

import configparser

config = configparser.ConfigParser()
config.read("myConfig.ini")
var_a = config.get("myVars", "globalFilepath") #file local and internet
var_b = config.get("myVars", "ip_address") #

#addr = 'http://0.0.0.0:5000' #check for size
addr = var_b
test_url = addr + '/api/test'

#location = input("Please input the source image :")
location = var_a

name_identifier = location.split("/")

if "https" in location:
    #print("hi")
    url = location
    filename = url.split('/')
    count = len(filename)
    lastname = filename[-count + (count-1)]
    ##print(count)
    ##print(lastname)
    urllib.request.urlretrieve(url,lastname)

    content_type = 'image/jpeg'
    headers = {'content-type': content_type}

    img = cv2.imread(lastname)
    # encode image as jpeg
    _, img_encoded = cv2.imencode('.jpeg', img)
    # send http request with image and receive response
    response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
    # decode response
    message = json.loads(response.text)
    for i in range(len(message)):

        new_message = message[i]
        #print(new_message['emotion'])
        top = int(new_message['faceRectangle']['top'])
        left = int(new_message['faceRectangle']['left'])
        width = int(new_message['faceRectangle']['width'])
        height = int(new_message['faceRectangle']['height'])

        cv2.rectangle(img, (top, left), (top+width, left+height), (255,0,0),2)
        cv2.putText(img, new_message['emotion'], (top, left), cv2.FONT_HERSHEY_SIMPLEX, 4.0, (0, 255, 0),thickness=4, lineType=2)
        cv2.putText(img, new_message['gender'], (top, left+height+50), cv2.FONT_HERSHEY_SIMPLEX, 4.0, (0, 255, 0),thickness=4, lineType=2)
    cv2.imwrite("my.jpeg",img)
    
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    new_image = cv2.imread("my.jpeg")
    image_size = cv2.resize(new_image,(960,540))
    cv2.imshow("image",image_size)
    cv2.waitKey(0)

else:
    # prepare headers for http request
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}

    img = cv2.imread(location)
    # encode image as jpeg
    _, img_encoded = cv2.imencode('.jpeg', img)
    # send http request with image and receive response
    response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
    # decode response
    message = json.loads(response.text)
    for i in range(len(message)):

        new_message = message[i]
        #print(new_message['emotion'])
        top = int(new_message['faceRectangle']['top'])
        left = int(new_message['faceRectangle']['left'])
        width = int(new_message['faceRectangle']['width'])
        height = int(new_message['faceRectangle']['height'])

        cv2.rectangle(img, (top, left), (top+width, left+height), (255,0,0),2)
        cv2.putText(img, new_message['emotion'], (top, left), cv2.FONT_HERSHEY_SIMPLEX, 4.0, (0, 255, 0),thickness=4, lineType=2)
        cv2.putText(img, new_message['gender'], (top, left+height+50), cv2.FONT_HERSHEY_SIMPLEX, 4.0, (0, 255, 0),thickness=4, lineType=2)
    cv2.imwrite("my.jpeg",img)

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    new_image = cv2.imread("my.jpeg")
    image_size = cv2.resize(new_image,(960,540))
    cv2.imshow("image",image_size)
    cv2.waitKey(0)
