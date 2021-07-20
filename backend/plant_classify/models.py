from django.db import models
from django.conf import settings
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image
import cv2
import numpy as np
import os

classnames=['Apple Scab',
 'Apple Black Rot',
 'Apple Cedar Rust',
 'Apple Healthy',
 'Blueberry Healthy',
 'Cherry Powdery Mildew',
 'Cherry Healthy',
 'Corn(maize) Gray Leaf Spot',
 'Corn(maize) Common Rust',
 'Corn(maize) Northern Leaf Blight',
 'Corn(maize) Healthy',
 'Grape Black Rot',
 'Grape Esca',
 'Grape Leaf blight',
 'Grape healthy',
 'Orange Citrus Greening',
 'Peach Bacterial Spot',
 'Peach Healthy',
 'Pepper Bell Bacterial Spot',
 'Pepper Bell Healthy',
 'Potato Early Blight',
 'Potato Late Blight',
 'Potato Healthy',
 'Raspberry Healthy',
 'Soybean Healthy',
 'Squash Powdery Mildew',
 'Strawberry Leaf Scorch',
 'Strawberry Healthy',
 'Tomato Bacterial Spot',
 'Tomato Early Blight',
 'Tomato Late Blight',
 'Tomato Leaf Mold',
 'Tomato Septoria Leaf Spot',
 'Tomato Spider Mites',
 'Tomato Target Spot',
 'Tomato Yellow Leaf Curl Virus',
 'Tomato Mosaic Virus',
 'Tomato Healthy']
# Create your models here.
class Plant(models.Model):
    image = models.ImageField(upload_to='post_images')
    result=models.CharField(max_length=20,blank=True)
    
    def __str__(self):
        return str(self.image)
    def save(self,*args,**kwargs):
        img = Image.open(self.image)
        img_array=image.img_to_array(img)
        dim = (50,50)
        resized = cv2.resize(img_array,dim,interpolation=cv2.INTER_AREA)
        ready=np.expand_dims(resized,axis=0)
        try:
            file_model=os.path.join(settings.BASE_DIR,'model_using_keras_epoch_25.h5')
            graph = tf.compat.v1.get_default_graph()
            with graph.as_default():
                model=tf.keras.models.load_model(file_model)
                pred = np.argmax(model.predict(ready))
                self.result=str(classnames[pred])
                print("Classified as ",classnames[pred])
        except:
            print('Failed to Classify')
            self.result = 'failed to classify' 
        return super().save(*args,**kwargs)