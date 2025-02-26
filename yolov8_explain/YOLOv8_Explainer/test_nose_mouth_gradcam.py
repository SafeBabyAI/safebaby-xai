import os
from .core import display_images
from .yolov8_heatmap_nose_mouth import yolov8_heatmap_nose_mouth

def main():
    # 1) Heatmap 객체 생성
    model = yolov8_heatmap_nose_mouth(
        weight=r"C:\Users\USER\Desktop\my_git\safebaby-xai\yolov8_explain\runs\detect\train2\weights\best.pt",
        method="GradCAM",  # GradCAM, EigenGradCAM, etc.
        conf_threshold=0.2,
        ratio=0.02,
        show_box=True,
        renormalize=False
    )

    # 2) 이미지 경로
    img_path = r"C:\Users\USER\Downloads\processed_front_03\f0358_dark_sr.jpeg"

    # 3) Grad-CAM 실행
    results = model(img_path)  # returns list of PIL Images
    # 4) 결과 시각화
    display_images(results)

if __name__ == "__main__":
    main()
