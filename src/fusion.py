import pywt
import numpy as np

def wavelet_fusion(img1, img2, wavelet='haar'):
    """
    Perform wavelet-based fusion of two images.
    """
    # Decompose both images
    coeffs1 = pywt.dwt2(img1, wavelet)
    coeffs2 = pywt.dwt2(img2, wavelet)

    cA1, (cH1, cV1, cD1) = coeffs1
    cA2, (cH2, cV2, cD2) = coeffs2

    # Fusion rule: average approximation + max details
    cA = (cA1 + cA2) / 2
    cH = np.maximum(cH1, cH2)
    cV = np.maximum(cV1, cV2)
    cD = np.maximum(cD1, cD2)

    fused = pywt.idwt2((cA, (cH, cV, cD)), wavelet)
    fused = np.clip(fused, 0, 1)  # Keep values in [0,1]
    return fused
