import os
import torch
import cv2
from torch.utils.data import Dataset

class RoadDamageDataset(Dataset):
    def __init__(self, img_dir, label_dir, img_size=640):
        self.img_dir = img_dir
        self.label_dir = label_dir
        self.images = [
            f for f in os.listdir(img_dir) if f.endswith((".jpg", ".png"))
        ]
        self.img_size = img_size

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_name = self.images[idx]
        img_path = os.path.join(self.img_dir, img_name)
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (self.img_size, self.img_size))

        h, w, _ = img.shape

        label_path = os.path.join(
            self.label_dir,
            img_name.replace(".jpg", ".txt").replace(".png", ".txt")
        )

        boxes = []
        labels = []

        if os.path.exists(label_path) and os.path.getsize(label_path) > 0:
            with open(label_path, "r") as f:
                for line in f:
                    cls, x, y, bw, bh = map(float, line.strip().split())
                    x1 = (x - bw/2) * w
                    y1 = (y - bh/2) * h
                    x2 = (x + bw/2) * w
                    y2 = (y + bh/2) * h
                    boxes.append([x1, y1, x2, y2])
                    labels.append(int(cls))

        boxes = torch.tensor(boxes, dtype=torch.float32) if boxes else torch.zeros((0,4), dtype=torch.float32)
        labels = torch.tensor(labels, dtype=torch.int64) if labels else torch.zeros((0,), dtype=torch.int64)

        img = torch.from_numpy(img).float().permute(2,0,1)/255.0

        target = {"boxes": boxes, "labels": labels, "image_id": torch.tensor([idx])}
        return img, target