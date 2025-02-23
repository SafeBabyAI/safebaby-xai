# ResNet50 explain

- 가장 높은 성능을 보이는 V5 모델의 오분류 원인 분석

# Partition Explainer

## 마스커 선택
- blur(3,3) : 작은 블러 효과, 국소적 특징 확인
- inpaint_telea : 픽셀 제거 후 모델 반응 확인
- inpaint_ns : telea보다 부드러운 복원



> inpaint_telea - SHAP value가 매우 낮게 측정되어 변별력이 떨어지는 현상
![alt text](ex_images\image-1.png)

> inpaint_ns - inpaint_telea보다 특징 반영
![alt text](image-1.png)

> blur(3, 3) - 국소적인 특징 확인 가능
![alt text](image-2.png)