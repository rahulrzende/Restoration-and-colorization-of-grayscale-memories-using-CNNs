#!/usr/bin/env python
# coding: utf-8

# In[1]:


def image_blur(im, rad=100):
    """
    Short Summary
    -------------
    This function blurs the image
    
    Extended Summary
    -------------
    This function blurs the image using a radius based filter. The radius is set to a default value of 100
    since this is the recommended value for radius filters. However the user can also set their own 
    value for the radius of the filter.
    
    Parameters
    ----------
    im = image which needs to be blurred
    rad = radius over which the filter can be applied
    
    Returns
    --------
    The function returns a blurred image with the disk filter applied.
    
    Examples
    --------
    Example 1:
    image_blur(im) - In this case the default value of 100 will be used for the radius of the disk filter
    
    Example 2:
    image_blur(im,50)
    """
    im_mask = mop.disk(rad)
    cp = np.copy(im)
    blurred = rank.median(cp, im_mask)
    return blurred


# In[ ]:




