def fourier_transformLP(im):
    """
    Short Summary
    -------------
    This function uses Fourier Transformation to transform our image information gray scaled pixels into frequencies and do further process

    Extended Summary
    -------------
    This function computes the Fourier transformation using the following steps:
    1 - Compute the 2-dimensional Fast Fourier Transform
    2 - Shift the zero-frequency component to the center of the spectrum
    3 - Inverse of Step 2. Shift the zero-frequency component back to original location
    4 - Inverse of Step 1. Compute the 2-dimensional inverse Fast Fourier Transform

    Parameters
    ----------
    im = image to which the foureir transform needs to be applied

    Returns
    --------
    The function returns a grey scaled image after the inverse Fourier transformation process.

    Examples
    --------
    Example 1:
    fourier_transform(im) - In this case the fourier transform is applied using a gaussian low pass filter with
    the value of constant as 100


    """
    def fourier_transformLP(im):
    fim = np.fft.fft2(im) # Perform transform
    fim2 = np.fft.fftshift(fim) # Center
    fim3 = fim2 * gaussianLP(100, im.shape) # Multiply by filter function
    fim4 = np.fft.ifftshift(fim3) # Un-center
    imLP = np.real(np.fft.ifft2(fim4))
    return imLP # Perform inverse transform
