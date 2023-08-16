# Image Captioning with Enhanced Semantic Attention
<img src="model arch.png" width="700">

Catalog:
- [x] Inference and Training our model on kaggle.
- [x] To eval our model locally using our checkpoints.


### Inference and training our model on kaggle:
You can inference, evaluate or train our model using kaggle gpu to implement [Our Kaggle notebook](https://www.kaggle.com/code/uwelcomem/image-captioning-with-enhanced-semantic-attention) which contains all needed datasets and checkpoints.

### To eval and inference locally using our pre-trained checkpoints:
You Can run main.ipynb file by installing requirements.txt

To inference our model, you will need to download our checkpoint from [model checkpoint](https://www.kaggle.com/datasets/uwelcomem/image-captioing-checkpoint) and place it to the folder which you choose it on config.json file in "checkpoint" field and set "load_checkpoint" to true.

To eval our model you will need to download the following:
- [Coco 2014 Dataset](https://www.kaggle.com/datasets/nadaibrahim/coco2014) and place it to the folder choosen in config.json in "image_root" field.
- [Karpathy Split Dataset](https://www.kaggle.com/datasets/shtvkumar/karpathy-splits) and place it to the folder choosen in config "karpathy_annot_path" field.

  Then you will need to set "evaluate" in args.json to true. After that you can run the evaluation part by run our_trainer.py file.

To train our model you can use the last eval steps except "evaluate" field you must set it to false.
