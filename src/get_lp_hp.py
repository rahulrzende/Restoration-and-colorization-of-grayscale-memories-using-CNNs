#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_lp_hp(im, sigma=10):
    """
    Short Summary
    -------------
    This function uses a Fourier Transform to transform our black and white images into frequency domain,
    apply low pass and high pass filter actions, and return resulting images post filtering.
    
    Extended Summary
    -------------
    This function computes the Fourier transformation using the following steps:
    1 - Capture the original image's dimensions
    2 - Resize image to a 512*512 size (in pixels)
    3 - Initialize low and high pass filters based on sigma value
    4 - Compute the 2-dimensional Fast Fourier Transform
    5 - Shift the zero-frequency component to the center of the spectrum
    6 - Inverse of Step 2. Shift the zero-frequency component back to original location
    7 - Inverse of Step 1. Compute the 2-dimensional inverse Fast Fourier Transform
    8 - Resize resultant images (post-filtering) back to original dimensions
    9 - Return results of high-pass and low-pass filtering
    
    Parameters
    ----------
    im = image of which the high-pass and low-pass filtered results are required
    sigma = control the high-pass and low-pass filters' cut-off frequency (Default value is 10)
    
    Returns
    --------
    The function returns the grey scaled image's transformed results after high-pass and low-pass filtering.
    
    Examples
    --------
    Example 1:
    get_lp_hp(im) - In this case the fourier transform is applied using a gaussian low/high pass filter with 
    the default value of sigma i.e. 10, and resultant filtered images are returned.
    
    Example 2:
    get_lp_hp(im,sigma=5) - In this case the fourier transform is applied using a gaussian low/high pass filter with 
    the value of sigma as 5, and resultant filtered images are returned.
    """
    
    # capture original dimensions
    a = im.shape[0]
    b = im.shape[1]
    
    # resize image for ease of applying transform
    im = resize(im, (512,512), anti_aliasing=True)
    
    # initialize our filter
    xi = np.linspace(0, 511, 512)
    x, y = np.meshgrid(xi, xi)
    mu = 256
    low_pass = np.exp(-((x-mu)**2 + (y-mu)**2)/(2*sigma**2))
    high_pass = 1 - np.exp(-((x-mu)**2 + (y-mu)**2)/(2*sigma**2))
    
    # essentially a low-pass filter action
    fim = np.fft.fft2(im)                 # Perform fourier transform of image
    fim2 = np.fft.fftshift(fim)           # Center the transform
    fim3 = np.multiply(fim2, low_pass)    # Multiply centered transform by filter function
    fim4 = np.fft.ifftshift(fim3)         # Un-center the filtered transform
    im_low = np.real(np.fft.ifft2(fim4))  # Perform inverse fourier transform to get back image
    
    # essentially a high-pass filter action
    fim = np.fft.fft2(im)                  # Perform fourier transform of image
    fim2 = np.fft.fftshift(fim)            # Center the transform
    fim3 = np.multiply(fim2, high_pass)    # Multiply centered transform by filter function
    fim4 = np.fft.ifftshift(fim3)          # Un-center the filtered transform
    im_high = np.real(np.fft.ifft2(fim4))  # Perform inverse fourier transform to get back image
    
    # resize image back to original shape before returning results
    im_low = resize(im_low, (a,b), anti_aliasing=True)
    im_high = resize(im_high, (a,b), anti_aliasing=True)
    
    return(im_low, im_sharp)

def test_function():
    """
    This is a test function created to test the ability to define multiple functions within a module and call them by importing accordingly
    """
    print("Hello")


