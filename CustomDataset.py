import os
import torch
import sys
import yolov5
import numpy as np
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from torchvision.transforms import functional as F
from yolov5.utils.augmentations import LetterBox  # Adjust import based on your YOLOv5 installation

class yolov5Dataset(Dataset):
    def __init__(self, directory):
        self.directory = directory
        self.images = [file for file in os.listdir(directory) if file.endswith('.jpg') or file.endswith('.png')]

        self.transform = transforms.Compose([
            LetterBox(size=(640,640), stride=32),  # Use the custom Letterbox transform
            transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor()  # Convert to tensor
        ])

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_path = os.path.join(self.directory, self.images[idx])
        image = Image.open(img_path).convert('RGB')  # Convert to RGB for consistency
        return self.transform(image)
