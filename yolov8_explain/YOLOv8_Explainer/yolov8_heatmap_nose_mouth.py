import os
import cv2
import torch
import numpy as np
from PIL import Image
from ultralytics.nn.tasks import attempt_load_weights
from pytorch_grad_cam import GradCAM
from .utils import letterbox
from .core import ActivationsAndGradients  # from your original code
from .core import yolov8_heatmap  # base heatmap class
from .yolov8_target_nose_mouth import yolov8_target_nose_mouth  # import the custom target

class yolov8_heatmap_nose_mouth(yolov8_heatmap):
    """
    Subclassing the original yolov8_heatmap to inject our custom target 
    that only focuses on classes 3,4 (mouth, nose).
    """
    def __init__(self,
                 weight: str,
                 device=torch.device("cuda" if torch.cuda.is_available() else "cpu"),
                 method="GradCAM",
                 layer=[12, 17, 21],
                 conf_threshold=0.2,
                 ratio=0.02,
                 show_box=True,
                 renormalize=False) -> None:
        super().__init__(weight, device, method, layer, conf_threshold, ratio, show_box, renormalize)

        # Overwrite the default target with our custom one
        self.target = yolov8_target_nose_mouth(conf=conf_threshold, ratio=ratio)

    # The rest of the methods (post_process, draw_detections, etc.) 
    # remain the same as parent class
