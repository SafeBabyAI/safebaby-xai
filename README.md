# safebaby-xai
SafeBabyAI Vision 모델 분석 레포지토리.

# ResNet50 분석

## SHAP의 Deep Explainer, Partition Explainer

### About SHAP
SHAP(Shapley Additive Explainations)는 모델의 예측을 설명하기 위한 XAI 기법 중 하나로, 특정 feature가 예측 결과에 얼마나 기여하는지를 정량적으로 분석하는 방법이다.</br>

#### Deep Explainer -> Gradient Explainer로 변경
- Deep Explainer는 구버전의 TensorFlow 1.x와 호환되도록 설계되었으며 지원이 제한적 유사한 원리의 Gradient Explainer로 변경(Torchvision과 호환)

- 신경망 모델의 그래디언트를 기반으로 SHAP 값을 계산하는 방법으로, 입력 이미지의 각 픽셀이 모델의 예측에 얼마나 기여하는지를 분석할 수 있다.

#### 분석 방법
- Summary Plot: 데이터셋 전체에서 어떤 픽셀이 분류에 가장 영향을 미치는지 시각화
- Force Plot: 개별 이미지에서 특정 예측이 나온 이유를 시각적으로 표현
- SHAP Heatmap: 모델이 보고 있는 중요한 영역을 원본 이미지 위에 시각화

#### 활용 인사이트
- ResNet50이 잘못된 특징(배경, 옷 등)에 의존하여 예측하는 경우를 식별 가능

#### Partition Explainer

입력 이미지를 여러 개의 그룹으로 분할하여, 픽셀 그룹이 모델 예측에 미치는 영향을 분석하는 기법으로, 픽셀들을 독립적인 변수로 다루기 어려운 경우에 적합합

1. 입력 이미지를 작은 블록 단위로 나누어 마스킹(masking)
2. 각 블록을 제거하거나 유지했을 때 모델 예측이 어떻게 변하는지 분석
3. 모델이 어떤 부분을 중점적으로 보고 있는지 확인

#### 활용 인사이트
- 모델이 일관되게 특정 영역을 참고하는지 분석
- 예측이 불안정한 경우, 특정 픽셀 그룹의 기여도를 낮추기 위해 학습 데이터 보강 가능


---
</br>

# YOLOv8 분석

#### YOLO의 객체 감지 동작 과정
1. 입력 이미지를 S x S 그리드로 분할
2. 각 그리드에서 B개의 바운딩 박스와 신뢰도(confidence)점수 예측
3. 신뢰도가 높은 박스를 선택하여 최종 감지된 객체 결정 
4. NMS(Non-Maximum Suppresssion)을 적용하여 중복복 감지 제거

#### Grad-CAM 분석

모델의 마지막 Convolution Layer의 활성화 맵(Activation Map)을 이용용하여 모델이 어디를 중요하게 보는지 시각화 하는 기법이다.
1. YOLO의 마지막 Convolution Layer에서 활성화 맵(Activation Map) 저장
2. 역전파를 통해 예측된 클래스와 관련된 그레디언트 계산
3. 그레디언트와 활성화 맵을 곱하여 중요한 영역 강조
4. 입력 이미지 위에 Grad-CAM 히트맵을 통해 픽셀 중요도를 확인 가능

-> 코,입이 있는 영역을 무시하는 이유를 분석

#### Confidence Score 분석
- Confidence 점수가 낮아서 감지가 안 되는 경우 threshold 조정 혹은 데이터 증강 고려

#### IOU (Intersection over Union) 분석
- 예측한 바운딩 박스와 실제 바운딩 박스의 겹치는 비율 분석
- 값이 0~1 사이에 있으며, 1에 가까울수록 정확한 감지를 의미
- IOU가 낮다면 학습데이터의 보완이 필요 (더 다양한 코와 입의 형태, 다양한 각도, 객체가 작은 데이터)

