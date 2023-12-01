RCMF-for-image-caption
====
### Implementation of Regular Constrained Multimodal Fusion Model for Image (RCMF) [](URL link)
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
Remember to unzip the .rar archive in the coco-caption.
## Data preparation
The necessary files in training and evaluation are saved in `mscoco` folder, which is organized as follows:
    mscoco/
    |--feature/
        |--coco2014/
           |--train2014/
           |--val2014/
           |--test2014/
           |--annotations/
    |--misc/
    |--sent/
    |--txt/  
where the mscoco/feature/coco2014 folder contains the raw image and annotation files of [MSCOCO 2014](https://cocodataset.org/#download) dataset.  
You can download other files from the following links.
* 1.[Baidu cloud](https://pan.baidu.com/s/1zaeKHy7J1CIehebkdVKmhA) Extract code: wgcq
* Place in the main file structure.
* 2.[Baidu cloud](https://pan.baidu.com/s/1-wyeEjJqHP1o-vStYh1nOg) Extract code: e4ys  
