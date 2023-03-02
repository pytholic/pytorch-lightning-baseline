import albumentations as A
import pytorch_lightning as pl
import torch
from albumentations.pytorch import ToTensorV2
from matplotlib import pyplot as plt

from model import Classifier

# Load the model
classifier = Classifier()
model = classifier.load_from_checkpoint("./models/checkpoint.ckpt")
