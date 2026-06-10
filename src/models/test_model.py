from src.models import get_model

# Faster R-CNN
model = get_model("faster_rcnn", num_classes=6)
print(model)

# DETR
model = get_model("detr", num_classes=6)
print(model)