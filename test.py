import albumentations as A
import pytorch_lightning as pl
import torch
from albumentations.pytorch import ToTensorV2
from matplotlib import pyplot as plt
from model import Classifier

# Load the model
model = MyLightningModule.load_from_checkpoint("model = MyLightningModule.load_from_checkpoint/pytorch-lightning-baseline-epoch=03-val_loss=0.00.ckpt 
checkpoint.ckpt")


def preprocess(img):
    