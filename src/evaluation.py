import numpy as np
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio, structural_similarity

def evaluate_fusion(img_ref, img_fused):
    """
    Evaluate fused image against a reference image 
    using MSE, PSNR, and SSIM.
    """
    mse = mean_squared_error(img_ref, img_fused)
    psnr = peak_signal_noise_ratio(img_ref, img_fused, data_range=1.0)
    ssim = structural_similarity(img_ref, img_fused, data_range=1.0)
    
    return {"MSE": mse, "PSNR": psnr, "SSIM": ssim}
