#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pywt
from statsmodels.robust import mad
import numpy as np


# In[2]:


def waveletSmooth( x, wavelet="db4", level=1, title=None ):
    coeff = pywt.wavedec( x, wavelet, mode="per")
    sigma = mad( coeff[-level] )
    uthresh = sigma * np.sqrt( 2*np.log( len( x ) ) )
    coeff[1:] = ( pywt.threshold( i, value=uthresh, mode="soft" ) for i in coeff[1:] )
    y = pywt.waverec( coeff, wavelet, mode="per" )
    return y


# In[ ]:




