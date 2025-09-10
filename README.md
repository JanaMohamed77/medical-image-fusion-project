
#  Medical Imaging Fusion using Wavelet Transform

This project focuses on **fusing multimodal brain MRI images** (T1ce, T2, FLAIR) 
from the **BraTS2020 dataset** using wavelet-based methods (Haar & Daubechies).  
The main goal is to enhance diagnostic quality by combining complementary features from different modalities.

##  Features
- Preprocessing of brain MRI scans
- Image fusion using Haar and Daubechies wavelets
- Evaluation with quantitative metrics:
  - Mean Squared Error (MSE)
  - Peak Signal-to-Noise Ratio (PSNR)
  - Structural Similarity Index (SSIM)

##  Project Structuresrc/ 
→ main Python scripts (preprocessing, fusion, evaluation)
notebooks/ → Jupyter demo for reproducibility
results/ → sample outputs (before/after fusion)
requirements.txt → dependencies

---

##  Tools & Libraries
- Python 3.9+
- NumPy, SciPy, OpenCV
- PyWavelets
- Matplotlib
- Torch (optional for future deep learning experiments)

---

##  How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/JanaMohamed77/medical-imaging-fusion.git
   cd medical-imaging-fusion
pip install -r requirements.txt
jupyter notebook notebooks/demo.ipynb
