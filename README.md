# 북극 해빙 면적 예측 프로젝트 (Arctic Glacier Prediction)

본 프로젝트는 기후변화가 북극 해빙에 미치는 영향을 CO₂ 배출량, 기온, 오존 파괴 물질을 기반으로 분석하고,  
이를 통해 빙하 면적(glacial volume)을 예측하는 머신러닝 기반 환경 데이터 분석 프로젝트입니다.

---

## 프로젝트 개요

- 주제: 기후 요인이 북극 해빙에 미치는 영향 분석 및 미래 해빙 면적 예측
- 목표: 선형 회귀모델을 활용하여 빙하 면적 예측 모델 구축
- 사용 언어: Python  
- 사용 라이브러리: pandas, numpy, matplotlib, scikit-learn, statsmodels

---

## 모델 설명

### 선형 회귀 모델 (Linear Regression)

해빙 면적(glacial volume)을 다음 세 가지 변수로 예측합니다:

- CO₂ emissions (이산화탄소 배출량)
- temperature (1월 평균 기온)
- ozone (오존층 파괴 물질 배출량)

**예측 수식 (텍스트 형식):**

빙하 면적 = β₀ + β₁ * CO₂ + β₂ * 기온 + β₃ * 오존 + ε

---

## 데이터 수집 및 분석

### 데이터셋 개요

- 분석 기간: 1990년 ~ 2023년
- 주요 컬럼:
  - date: 연도
  - CO₂ emissions: 이산화탄소 배출량
  - temperature: 기온
  - ozone: 오존 파괴 물질 배출량
  - glacial volume: 실제 빙하량

### 주요 분석 결과

- CO₂, 기온, 오존 물질 모두 전반적으로 증가
- 반면, 빙하 면적은 지속적으로 감소
- 기후 변화가 해빙 감소를 가속화함을 시사

---

## 회귀 분석 및 시각화 결과

### 변수 간 상관관계 시각화

예: ozone vs glacial volume

```python
import seaborn as sns
sns.regplot(x='ozone', y='glacial volume', data=data)
