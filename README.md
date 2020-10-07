# DeepBiRD
A bibliographic reference detection appraoch

## Pre-processing

Use the provided python script to preprocess the input images. Once paths to input and output image are set, execute the python file:

```bash
python3 pre-process-images.py
```
Following images show different pre-processing stages:

Dilated Example            							| 			 Distance Transform Example 					|  Pre-processed Example
:--------------------------------------------------:|:-----------------------------------------------------:|:-------------------------:
![Dilated](pre-processing-examples/dilated-example.jpg?raw=true)    |  ![Distance Transform](pre-processing-examples/dist-transform-example.jpg?raw=true)     |  ![Pre-processed](pre-processing-examples/preprocessed-example.jpg?raw=true)

## Installation

For this project, we used the MaskRCNN implementation provided by [Detectron](https://github.com/facebookresearch/Detectron).

* Configure Detectron by following [these](https://github.com/facebookresearch/Detectron/blob/master/INSTALL.md) instructions
* Convert the pre-processed dataset to coco format
* Register dataset with Detectron
* Prepare config [file](https://github.com/facebookresearch/Detectron/blob/master/configs/12_2017_baselines/e2e_mask_rcnn_R-50-C4_1x.yaml) for training
* Train and evaluate model

## Fine-tuned Model

The model fine-tuned on [BibX](https://madata.bib.uni-mannheim.de/268/) and [BibLy](https://madata.bib.uni-mannheim.de/283/) dataset can be downloaded [here](https://cloud.dfki.de/owncloud/index.php/s/cRKDXq2eJCMJnY8).

