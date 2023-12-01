RCMF-for-image-caption
====
# RCMF
Implementation of Regular Constrained Multimodal Fusion Model for Image[](URL link)
<div align="center">
  <img src="https://github.com/200084/RCMF-for-image-caption/blob/main/imgs/Framework.jpg">
</div>

# Requirements (Our Experimental Enviroment)
## Running on 3090 GPU 
* Python 3.7.16
* Pytorch 1.10.0+cu111
* TorchVision 0.11.0+cu111
* coco-caption
* numpy 1.21.5
* tqdm 4.64.1

# Preparation
## coco-caption preparation
Refer [coco-caption](https://github.com/232525/PureT/blob/main/coco_caption/README.md), you will first need to download and install the [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/index.html) environment for use by SPICE. 
## Data preparation
