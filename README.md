 <img align="right" src="https://github.com/kareem1925/Classical-and-quantum-regression-analysis-for-the-optoelectronic-performance-of-NTCDA/blob/master/fig/material.png" width=450px>   

# Classical and quantum regression analysis for the optoelectronic performance of NTCDA


## Dataset Visualization
<img align="center" src="https://github.com/kareem1925/Classical-and-quantum-regression-analysis-for-the-optoelectronic-performance-of-NTCDA/blob/master/fig/3d.jpg" width=650px>  
<br/> 

<img align="center" src="https://github.com/kareem1925/Classical-and-quantum-regression-analysis-for-the-optoelectronic-performance-of-NTCDA/blob/master/fig/semi-log.png" width=400px>  

The optical absorbance of NTCDA thin film on a quartz substrate was measured at normal incidence of the light at room temperature in the spectral range of 190–2500 nm using a double beam spectrophotometer (JASCO model V-570 UV-VIS-NIR). The Photoelectrical properties – of the fabricated Au/NTCDA/p-Si/Al photodiode – were investigated by measuring the I-V characteristic curve at room temperature from +3.5 to -3.4, using Keithley electrometer model 6517B under the influence of UV light of wavelength 194 nm. The intensity of incident light was measured using Radiometer/Photometer model IL1400A.

<br/> 

## Environment Setup  

These are the packages used in the code development

```
pip install pennylane==0.10.0 strawberryfields==0.14.0 pennylane-sf==0.9.0 tensorflow==2.2.0 tpot==0.11.5 xgboost==0.90 keras
```

## Notebooks
1. [ANN](https://github.com/kareem1925/Classical-and-quantum-regression-analysis-for-the-optoelectronic-performance-of-NTCDA/blob/master/ANN.ipynb)
2. [KNN](https://github.com/kareem1925/Classical-and-quantum-regression-analysis-for-the-optoelectronic-performance-of-NTCDA/blob/master/KNN%20regressor.ipynb)
3. [TPOT](https://github.com/kareem1925/Classical-and-quantum-regression-analysis-for-the-optoelectronic-performance-of-NTCDA/blob/master/TPOT%20regressor.ipynb)
4. [QNN](https://github.com/kareem1925/Classical-and-quantum-regression-analysis-for-the-optoelectronic-performance-of-NTCDA/blob/master/QNN_regressor.ipynb)

## Authors
Ahmed M. El-Mahalawy, Kareem H. El-Safty

## How to Cite
If you extend or use this work, please cite the [paper][paper] where it was introduced:

```
@article{el2020classical,
  title={Classical and quantum regression analysis for the optoelectronic performance of NTCDA/p-Si UV photodiode},
  author={El-Mahalawy, Ahmed M and El-Safty, Kareem H},
  journal={arXiv preprint arXiv:2004.01257},
  year={2020}
}
```

[paper]: https://arxiv.org/abs/2004.01257

## License
This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
