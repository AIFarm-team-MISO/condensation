# Isolation Forest를 이용한 습도 데이터 이상치 탐지

## 프로젝트 개요
이 프로젝트는 Isolation Forest 알고리즘을 사용하여  
습도 데이터에서 이상치를 탐지하는 것을 목표로 합니다.  
데이터는 CSV 파일에서 불러오며, 결측치를 처리한 후  
Isolation Forest 모델을 사용하여 이상치를 식별합니다.  
결과는 산점도로 시각화되며, 처리된 데이터는 새로운 CSV 파일로 저장됩니다.  

## 데이터셋
- **입력 CSV**: `data.csv`라는 이름의 CSV 파일로,  
`inHd`라는 열에 습도 데이터가 포함되어 있어야 합니다.  

- **출력 CSV**: 이상치 판별 결과가 추가된 `data_anomaly_InHd.csv`라는  
 이름의 CSV 파일로 저장됩니다.  

## 필요 조건
다음 Python 패키지들이 필요합니다:
- `scikit-learn`
- `pandas`
- `numpy`
- `matplotlib`

## 서버 접속 방법
Jupyter Notebook 서버는 외부에서 접속할 수 있도록 설정되어 있습니다.  
아래 URL을 통해 접속할 수 있습니다:

- **URL**: [http://3.39.6.220:8888](http://3.39.6.220:8888)

### 접속 비밀번호
- **비밀번호**: 보안을 위해 직접 공개하지 않습니다.  
  **비밀번호가 필요하시면 아래 이메일로 요청해 주세요**  

- **Email**: sevenstar15@naver.com  

### 테스트 방법
1. 위 URL을 통해 Jupyter Notebook에 접속합니다.  
2. 비밀번호를 입력한 후, 제공된 `cs_python.py`  
   또는 `cs.ipynb`를 실행하여 데이터를 분석할 수 있습니다.  
3. 분석 결과는 `data_anomaly_InHd.csv` 파일로 저장되며,  
   이상치 탐지 결과를 확인할 수 있습니다.  
