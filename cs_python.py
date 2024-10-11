from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 불러오기
df = pd.read_csv('data.csv')

# 습도(inHd)데이터 전처리
# 숫자 0으로 표기된 데이터를 결측치로 만들기 위해 nan으로 바꾸는 작업
df['inHd'].replace(0, np.nan)

# inHd 열의 결측치를 해당 열의 평균값으로 대체
df['inHd'].fillna(df['inTp'].mean())


# 처리된 데이터를 출력 (선택사항)
print(df.head())  # 처음 몇 개 행 출력


# 습도 데이터만 추출 (가정: 'inHd'라는 이름의 컬럼에 습도 데이터가 있음)
humidity_data = df[['inHd']]

# 결측치를 평균값으로 대체
imputer = SimpleImputer(strategy='mean')
humidity_data_imputed = imputer.fit_transform(humidity_data)

# Isolation Forest 모델 초기화 및 학습
# contamination 파라미터는 이상치 비율을 설정 예를 들어, 0.01은 이상치가 전체 데이터의 1%라는 가정
iso_forest = IsolationForest(contamination=0.01)
iso_forest.fit(humidity_data_imputed)


# 이상치 판별
# predict 메서드를 호출하여 각 데이터 포인트가 정상인지 이상치인지 판별합니다.
# 출력값이 1이면 정상, -1이면 이상치입니다.
labels = iso_forest.predict(humidity_data_imputed)

# 결과를 데이터프레임에 추가
df['anomaly'] = labels

# anomaly 컬럼을 업데이트하여 inHd가 60 이하인 경우는 정상(1)으로 표시
# 이상치의 판정은 우리가 원하는 부분만 따로 설정할수 없으므로 습도가 낮은 부분(60이하)은 이상치에서 제거
df.loc[(df['anomaly'] == -1) & (df['inHd'] <= 60), 'anomaly'] = 1

# 이상치와 정상치를 구분하여 그래프로 그리기
plt.scatter(df.index, df['inHd'], c=df['anomaly'])
plt.xlabel('Index')
plt.ylabel('inHd (Humidity)')
plt.title('Anomaly Detection for inHd (Humidity)')
plt.show()

# 이상치 데이터만 필터링하여 출력
# 'anomaly'에는 이상치에 대한 값이 저장되어 있음 -1은 이상치를 의미
anomalies = df[df['anomaly'] == -1]
print("Anomalies in inHd (Humidity):")
print(anomalies)

# 앞서 만든 'anomaly' 컬럼이 있는 데이터프레임 df를 새로운 CSV 파일로 저장
df.to_csv('data_anomaly_InHd.csv', index=False)