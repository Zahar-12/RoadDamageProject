import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--model",
    type=str,
    required=True
)

args = parser.parse_args()

if args.model == "yolov8n":
    print("Running YOLOv8n")

elif args.model == "yolo11n":
    print("Running YOLO11n")

elif args.model == "yolo26n":
    print("Running YOLO26")

elif args.model == "faster_rcnn":
    print("Running Faster R-CNN")

elif args.model == "ssd":
    print("Running SSD")

elif args.model == "detr":
    print("Running DETR")

else:
    print("Unknown model")