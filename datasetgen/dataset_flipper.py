import cv2
import os
import glob
from tqdm import tqdm

DATASET_PATH = 'full_dataset'

def augment_dataset_mirror():
    subfolders = [f.path for f in os.scandir(DATASET_PATH) if f.is_dir()]
    
    total_mirrored = 0
    print(f"Start flipping. The number of directories: {len(subfolders)}")

    for folder in subfolders:
        label = os.path.basename(folder)
        image_paths = glob.glob(os.path.join(folder, "*.*"))
        
        images_to_process = [p for p in image_paths if not os.path.basename(p).startswith('flipped_')]
        
        if not images_to_process:
            continue

        print(f"\nSign processing'{label}':")
        
        for img_path in tqdm(images_to_process, desc=f"Directory {label}"):
            img = cv2.imread(img_path)
            if img is None:
                continue
            
            mirrored_img = cv2.flip(img, 1)
            
            base_name = os.path.basename(img_path)
            new_name = f"flipped_{base_name}"
            new_path = os.path.join(folder, new_name)
            
            cv2.imwrite(new_path, mirrored_img)
            total_mirrored += 1

    print(f"\n Finished ")
    print(f"New images {total_mirrored}")

if __name__ == "__main__":
    augment_dataset_mirror()