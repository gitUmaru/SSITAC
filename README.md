# SSITAC
## **S**kin **S**egmentation and **I**ndividual **T**ypology **A**ngle **C**omputation

## About
This code repository is an attempt of an implementation of semantic skin segmentation using a convolutional-deconvolutional approach. This appraoch is inspired by the paper [Semantic Fire Segmentation Model Based on Convolutional Neural Network for Outdoor Image](https://link.springer.com/article/10.1007/s10694-020-01080-z#Sec6). The network architecture is borrowed from that paper, with changes made to the loss function. The dataset that I used is a composite dataset of ISIC 2018 validation data and ISIC 2016 training data.

## Packages
- Tensor Flow
- Keras
- Scikit Learn

## Installation
There are two ways that one could run this repository: using the python notebook or running the python files locally. I recommend using the python notebook with Google Colab (or something similar) or using a cloud instance to run the files locally.

### File Structure
```
SSITAC/
├─ data/
│  ├─ dataset/
│  │  ├─ test_im/
│  │  ├─ test_ma/
│  │  ├─ train_im/
│  │  ├─ train_ma/
│  ├─ images/
│  ├─ masks/
│  ├─ split.py
├─ README_assets/
│  ├─ results.jpeg
├─ ssitac.ipynb
├─ README.md
├─ requirements.txt
├─ ssitac_model.h5
├─ test.py
├─ train.py
├─ utils.py

```

### Local Python Installation
```bash
pip install virtualenv

virtualenv ssitac

ssitac\Scripts\activate

pip install -r requirements.txt

python train.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
