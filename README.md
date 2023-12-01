RCMF-for-image-caption
====
### Implementation of Regular Constrained Multimodal Fusion Model for Image (RCMF).
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
Remember to unzip the ***.rar files in the coco-caption.
## Data preparation
The necessary files in training and evaluation are saved in `mscoco` folder, which is organized as follows:

mscoco/  
  &nbsp;&nbsp;&nbsp;&nbsp;|--feature/  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--coco2014/  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--train2014/  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--val2014/  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--test2014/  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--annotations/  
  &nbsp;&nbsp;&nbsp;&nbsp;|--misc/  
  &nbsp;&nbsp;&nbsp;&nbsp;|--sent/  
  &nbsp;&nbsp;&nbsp;&nbsp;|--txt/  

where the mscoco/feature/coco2014 folder contains the raw image and annotation files of [MSCOCO 2014](https://cocodataset.org/#download) dataset.  
You can download other files from the following links.
* 1.[Baidu cloud](https://pan.baidu.com/s/1zaeKHy7J1CIehebkdVKmhA). Extract code: wgcq
* Place in the root directory.
* 2.[Baidu cloud](https://pan.baidu.com/s/1-wyeEjJqHP1o-vStYh1nOg). Extract code: e4ys

NOTE: You can also extract image features of MSCOCO 2014 using [Swin-Transformer](https://github.com/microsoft/Swin-Transformer) or others and save them as ***.npz files into mscoco/feature for training speed up, refer to `coco_dataset.py` and `data_loader.py` in code repository for how to read and prepare features. In this case, you need to make some modifications to `RCMF_Model.py` (delete the backbone module) in code repository.

# Training
Note: our repository is mainly based on [PureT](https://github.com/232525/PureT#readme), and we directly reused their `config.yml` files, so there are many useless parameter in our model. （waiting for further sorting）
## Training for the first stage (XE)
Make sure you have already downloaded pre-trained Backbone model (Swin-Transformer) from Baidu cloud in "Data preparation" and save it in the root directory.

Before training, you may need check and modify the parameters in `config.yml` and `train.sh` files. Then run the script:
    `# for XE training  
    bash experiments_RCMF/RCMF_XE/train.sh`
## Training for the SCST
Copy the pre-trained model under XE loss into folder of experiments_RCMF/RCMF_SCST/snapshot/ and modify `config.yml` and `train.sh` files. Then run the script:
    `# for SCST training
    bash experiments_RCMF/RCMF_SCST/train.sh`  
# Evaluation or Testing 
Before testing, you may need check and modify the parameters in `config.yml` and `***test.sh` files. Then run the script:
    `# for XE training  
    bash experiments_RCMF/RCMF_XE/***test.sh`
### XE
| #BLEU-1	 | #BLEU-2	 | #BLEU-3	 | #BLEU-4	 | #METEOR | #ROUGE-L	| #CIDEr	| #SPICE | 
| --- | --- | --- |--- |--- |--- |--- |--- |
| 77.3 | 61.1 | 47.3 | 36.4 | 28.9 | 57.5 | 121.1 | 22.0 |
### SCST
| #BLEU-1	 | #BLEU-2	 | #BLEU-3	 | #BLEU-4	 | #METEOR | #ROUGE-L	| #CIDEr	| #SPICE | 
| --- | --- | --- |--- |--- |--- |--- |--- |
| 81.5 | 66.3 | 51.9 | 39.8 | 29.8 | 59.6 | 135.2 | 23.9 |

You can download the pre-trained model from [Baidu cloud](https://pan.baidu.com/s/1iMllCZAPEl1TSOy6yU-ukg). Extract code: kpmh

# Reference

# Acknowledgements
This repository is based on [PureT](https://github.com/232525/PureT#readme), [ruotianluo/self-critical.pytorch](https://github.com/ruotianluo/self-critical.pytorch) and [microsoft/Swin-Transformer](https://github.com/microsoft/Swin-Transformer).
