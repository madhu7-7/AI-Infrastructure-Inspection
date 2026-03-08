import os
import shutil
import random

random.seed(42)

original_dataset = "dataset_original"  # original images folder
target_dataset = "dataset"             # organized dataset folder
splits = ["train", "valid", "test"]
classes = ["positive", "negative"]
num_images = 10

# Create folder structure
for split in splits:
    for cls in classes:
        path = os.path.join(target_dataset, split, cls)
        os.makedirs(path, exist_ok=True)

# Copy images
for cls in classes:
    cls_path = os.path.join(original_dataset, cls)
    images = os.listdir(cls_path)
    random.shuffle(images)
    selected_images = images[:num_images*len(splits)]

    for i, split in enumerate(splits):
        split_images = selected_images[i*num_images:(i+1)*num_images]
        for img in split_images:
            src = os.path.join(cls_path, img)
            dst = os.path.join(target_dataset, split, cls, img)
            shutil.copyfile(src, dst)

print("Dataset organized successfully!")