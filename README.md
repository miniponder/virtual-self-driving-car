# virtual-self-driving-car

this is an applied deep learning project, where a model was developed which can predict the steering angle of the car in real time. computer vision medthods such as data augmentation, batch generation, image preprocessing, were used. the model developed was based on the nvidia model architecture with 5 convolution layers.

### data augmentation techniques used:

#### 1. image flipping
![a comparison between original image and flipped image](images/flipped-image.png)
#### 2. image panning
![a comparison between original image and panned image](images/panned-image.png)
#### 3. altering brightness
![a comparison between original image and brightness altered image](images/brightness-altered-image.png)
#### 4. image zooming
![a comparison between original image and zoomed image](images/zoomed-image.png)

### image preprocessing:
![a comparison between original image and preprocessed image](images/preprocessed-image.png)

after training the model with batch generation techniques a clear difference between training and validation loss was acheived.

![comparison between training and validation loss](images/loss.png)
