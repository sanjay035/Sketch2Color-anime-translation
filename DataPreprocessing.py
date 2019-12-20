#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Importing the required libraries.
"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import glob
from tqdm import tqdm


# In[10]:


"""
Displaying the sample sketch and color images.
"""
for file in glob.glob('train\*.png')[:5]:
    f, a = plt.subplots(1,2, figsize=(10,5))
    a = a.flatten()
    
    img = Image.open(file).convert('RGB')
    a[0].imshow(img.crop((0, 0, 512,512))); a[0].axis('off');
    a[1].imshow(img.crop((512, 0, 1024, 512))); a[1].axis('off');
    
    plt.show()
    print(file)


# In[ ]:


"""
Creating a directory for training data. 
"""
get_ipython().system('mkdir trainData')


# In[ ]:


"""
Preprocessing and saving the training data to corresponding directory. 
"""
for idx, file in tqdm(enumerate(glob.glob('train\*.png')[:23])):
    img = Image.open(file).convert('RGB')
    
    img.crop((0, 0, 512,512)).save('./trainData/Images/{}.png'.format(idx))
    img.crop((512, 0, 1024, 512)).save('./trainData/Sketches/{}.png'.format(idx))


# In[ ]:


"""
Creating a directory for validation/test data. 
"""
get_ipython().system('mkdir valData')


# In[ ]:


"""
Preprocessing and saving the validation/test data to corresponding directory. 
"""
for idx, file in tqdm(enumerate(glob.glob('val\*.png')[:23])):
    img = Image.open(file).convert('RGB')
    
    img.crop((0, 0, 512,512)).save('./valData/Images/{}.png'.format(idx))
    img.crop((512, 0, 1024, 512)).save('./valData/Sketches/{}.png'.format(idx))

