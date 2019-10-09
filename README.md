# GNet

Glaucoma is an ocular disease that is the leading cause of irreversible blindness due to an increased Intraocular pressure resulting in damage to the optic nerve of eye. A common method for diagnosing glaucoma progression is through examination of dilated pupil in the eye by expert ophthalmologist. But this approach is laborious and consumes a large amount of time, thus the issue can be resolved using automation by using the concept of machine learning. Convolution neural networks (CNN’s) are well suited to resolve this class of problems as they can infer hierarchical information from the image which helps them to
distinguish between glaucomic and non-glaucomic image patterns for diagnostic decisions. This paper presents an Artificially Intelligent glaucoma expert system based on segmentation of optic disc and optic cup. A Deep Learning architecture is developed with CNN working at its core for automating the detection of glaucoma. The proposed system uses two neural networks working in conjunction to segment optic cup and disc. The model was tested on 50 fundus images and achieved an accuracy of 95.8% for disc and 93% for cup segmentation.

# How to use 

## Setup on local machine.
To use the code on a local machine setup the libraries such as keras.

Use the retinal fundus images of size 512x512 for prediction.

Change the paths of input images and model weights in the script.

Run the script.


## Setup on google colab
Open the jupyter notebook on colab in the Google Colab folder.

Upload the other two zip files onto the colab runtime.

Run the script.
