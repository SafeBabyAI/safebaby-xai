# safebaby-xai
SafeBabyAI Vision 모델 분석 레포지토리.

## About SHAP
SHAP(Shapley Additive Explainations)는 모델의 예측을 설명하기 위한 XAI 기법 중 하나로, 특정 feature가 예측 결과에 얼마나 기여하는지를 정량적으로 분석하는 방법이다.</br>

게임 이론의 "Shapley Value"의 개념을 사용하였다.

### ResNet50 분석

#### Deep SHAP(Deep Explainer)
- 이미지 특징 중요도를 분석
- Summary plot을 이용하여 이미지의 어느 부분이 분류에 기여했는지 확인
- Force plot을 활용하여 개별 이미지에서 특정 예측이 나온 이유를 분석

#### Partition Explainer
- 픽셀들을 그룹화하고, 마스킹하여 모델의 예측에 미치는 영향을 분석
- 모델이 어떤 영역을 중점적으로 보고 분류를 하는지 분석

