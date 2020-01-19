# Sketch2Color-anime-translation:
Given a plain anime sketch the model outputs a random colored anime image using Generative Adversarial Networks (GANs).

Implemented the anime sketch colorization using the reference(s) paper-1 below.

* Dataset: [Anime sketch colorization pair](https://www.kaggle.com/ktaebum/anime-sketch-colorization-pair)
* Blog on: [Towards Data Science](https://towardsdatascience.com/sketch-to-color-anime-translation-using-generative-adversarial-networks-gans-8f4f69594aeb)

References:

[1] https://arxiv.org/abs/1705.01908

[2] https://machinelearningmastery.com

[3] https://github.com/soumith/ganhacks

# GAN Architecture:
![GAN](./Images/GAN.PNG)

# Tensorboard logs:
![Tensorboard](./Images/TensorboardLogs.png)

# In progress training results:
**At epoch 30,**

![result_epoch_30](./Images/Epoch30.PNG)

**At epoch 40,**

![result_epoch_40](./Images/Epoch40.PNG)

**At epoch 43,**

![result_epoch_43](./Images/Epoch43.PNG)

# Prediction on test sketches:
![Sample_1](./Images/Combined_1.png)
![Sample_2](./Images/Combined_2.png)
