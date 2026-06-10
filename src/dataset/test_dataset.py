from src.dataset.dataset import RoadDamageDataset

ds = RoadDamageDataset(
    "/Users/zahar/PycharmProjects/RoadDamageProject/data/raw/train/images",
    "/Users/zahar/PycharmProjects/RoadDamageProject/data/raw/train/labels"
)

print(len(ds))
img, target = ds[0]
print(img.shape, target)