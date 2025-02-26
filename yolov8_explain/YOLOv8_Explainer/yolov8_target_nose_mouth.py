import torch
import torch.nn as nn

class yolov8_target_nose_mouth(nn.Module):
    """
    YOLOv8 Target class that only uses class 3 (mouth) and class 4 (nose)
    for Grad-CAM scoring.
    """
    def __init__(self, conf=0.2, ratio=0.02):
        super().__init__()
        self.target_classes = [3, 4]  # nose=4, mouth=3
        self.conf = conf
        self.ratio = ratio

    def forward(self, data):
        """
        data = [post_result, pre_post_boxes]
        post_result: (n, num_classes)  - class scores
        pre_post_boxes: (n, 4)
        We'll sum up only class 3 or 4 scores if they exceed self.conf
        """
        post_result, pre_post_boxes = data
        result_scores = []

        for i in range(post_result.size(0)):
            for cls_id in self.target_classes:
                score = float(post_result[i, cls_id])
                if score >= self.conf:
                    result_scores.append(score)

        if len(result_scores) == 0:
            # If no nose/mouth detection >= conf, return 0.0 tensor
            return torch.tensor(0.0, requires_grad=True, device=post_result.device)

        return torch.tensor(sum(result_scores), requires_grad=True, device=post_result.device)
