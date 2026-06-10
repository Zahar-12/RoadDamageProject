import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.ssd import SSDClassificationHead
from transformers import DetrForObjectDetection
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor


def load_faster_rcnn(num_classes):
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights="DEFAULT")

    in_features = model.roi_heads.box_predictor.cls_score.in_features

    model.roi_heads.box_predictor = FastRCNNPredictor(
        in_features,
        num_classes
    )

    return model


def get_model(name, num_classes):
    if name == "faster_rcnn":
        return load_faster_rcnn(num_classes)

    raise ValueError(f"Unknown model: {name}")

def load_yolo(model_path):
    from ultralytics import YOLO
    return YOLO(model_path)

def load_faster_rcnn(num_classes):
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights="COCO_V1")

    in_features = model.roi_heads.box_predictor.cls_score.in_features

    model.roi_heads.box_predictor = FastRCNNPredictor(
        in_features,
        num_classes
    )

    return model

def load_ssd(num_classes):
    model = torchvision.models.detection.ssd300_vgg16(weights="COCO_V1")

    in_channels = [512, 1024, 512, 256, 256, 256]
    num_anchors = model.anchor_generator.num_anchors_per_location()

    model.head.classification_head = SSDClassificationHead(
        in_channels=in_channels,
        num_anchors=num_anchors,
        num_classes=num_classes
    )

    return model

def load_detr(num_classes):
    model = DetrForObjectDetection.from_pretrained(
        "facebook/detr-resnet-50",
        num_labels=num_classes,
        ignore_mismatched_sizes=True
    )

    return model

def get_model(name, num_classes=None, model_path=None):

    name = name.lower()

    if name == "yolov8n":
        return load_yolo(model_path)

    if name == "yolo11n":
        return load_yolo(model_path)

    if name == "yolo26n":
        return load_yolo(model_path)

    if name == "faster_rcnn":
        return load_faster_rcnn(num_classes)

    if name == "ssd":
        return load_ssd(num_classes)

    if name == "detr":
        return load_detr(num_classes)

    raise ValueError(f"Unknown model: {name}")