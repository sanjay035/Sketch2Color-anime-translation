#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import glob
from tqdm import tqdm


# In[10]:


for file in glob.glob('train\*.png')[:5]:
    f, a = plt.subplots(1,2, figsize=(10,5))
    a = a.flatten()
    
    img = Image.open(file).convert('RGB')
    a[0].imshow(img.crop((0, 0, 512,512))); a[0].axis('off');
    a[1].imshow(img.crop((512, 0, 1024, 512))); a[1].axis('off');
    
    plt.show()
    print(file)


# In[27]:


get_ipython().system('mkdir trainData')


# In[3]:


for idx, file in tqdm(enumerate(glob.glob('val\*.png')[:23])):
    img = Image.open(file).convert('RGB')
    
    img.crop((0, 0, 512,512)).save('./valData/Images/{}.png'.format(idx))
    img.crop((512, 0, 1024, 512)).save('./valData/Sketches/{}.png'.format(idx))

