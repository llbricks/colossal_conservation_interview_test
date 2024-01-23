import CustomDataset
import torch
import numpy as np
import cv2
from torch.utils.data import Dataset, DataLoader

image_dir = './imgs'
output_dir = './output'
if not os.path.exists(output_dir): os.makedirs(output_dir)

dataset = CustomDataset.yolov5Dataset(image_dir)
dataloader = DataLoader(dataset, batch_size=1, shuffle=True)

for batch in dataloader:

    # Get the first image from the batch and permute the dimensions
    image = batch[0]

    # Convert the tensor to a numpy array and change it from (C, H, W) to (H, W, C)
    image_np = image.permute(1, 2, 0).numpy()

    # If your images are normalized (e.g., to a range [0, 1] or mean subtracted), you should denormalize them here
    # Example for rescaling [0, 1] range back to [0, 255] (adjust according to your specific case):
    if image_np.max() <= 1:
        image_np = (image_np * 255).astype(np.uint8)

    # OpenCV uses BGR format by default, but the image is likely in RGB format.
    # Convert it from RGB to BGR
    image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Save the image
    cv2.imwrite('output/{}.jpg'.format(1), image_np)

