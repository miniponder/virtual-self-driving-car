# virtual-self-driving-car

this is an applied deep learning project where a convolutional neural network (cnn) was developed to predict the steering angle of a car in real time. computer vision techniques such as data augmentation, image preprocessing, and batch generation were employed to improve the model's performance and robustness.  

the model is based on the **nvidia architecture**, consisting of five convolutional layers followed by fully connected layers.

---

## data augmentation techniques

to increase data variability and simulate different driving scenarios, the following augmentation methods were applied:

### 1. image flipping   
![flipped image](images/flipped-image.png)

### 2. image panning   
![panned image](images/panned-image.png)

### 3. altering brightness  
![brightness altered image](images/brightness-altered-image.png)

### 4. image zooming   
![zoomed image](images/zoomed-image.png)

---

## image preprocessing

the input images were preprocessed by cropping irrelevant parts (e.g., sky and car hood), resizing, and normalizing pixel values.

![preprocessed image](images/preprocessed-image.png)

---

## training results

the model was trained using a custom batch generator to efficiently feed augmented data into the network. a clear distinction between training and validation loss indicates effective learning and minimal overfitting.

![training and validation loss](images/loss.png)

---

## technologies used:

- python
- keras / tensorflow
- opencv
- numpy
- matplotlib
- google colab

---

the training data was obtained from udacity's [self-driving-car-sim](https://github.com/udacity/self-driving-car-sim.git). it was then tested in autonomous mode on two different terrains. in this repo the are two data folders. the first one is a bit biased to the left side, while the second one is unbiased. feel free to use my data or generate your own data in the training mode and use it to build a new model.

---

## demo

my training data has been a bit biased, as you can see. i suggest you train your own data, and hopefully you can build a model that matches your driving style.

![terrain 1](images/terrain-1-sim.GIF)

---
