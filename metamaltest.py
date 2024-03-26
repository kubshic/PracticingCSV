import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('metamalaysia.csv')

# 전체 데이터프레임 출력
pd.set_option('display.max_columns', None)  # 모든 열 보여주기
pd.set_option('display.expand_frame_repr', False)  # 줄바꿈 없이 출력
pd.set_option('display.max_colwidth', None)  # 모든 열의 길이 제한 해제

# 'UTM' 열에서 '_________'가 포함된 행 선택 (contains 다음에 작은 따옴표 안에 입력)
filtered_rows = df[df['UTM'].str.contains('Dangle', na=False)]

# 선택된 행에서 'UTM' 열과 'ROAS' 열의 데이터만 추출
result = filtered_rows[['UTM','매출','지출 금액 (KRW)','ROAS']]

print("요청하신 UTM, 매출, 지출 금액, ROAS입니다:")
print(result)

# '매출' 열의 달러 기호(￦) 제거
df['매출'] = df['매출'].str.replace('￦', '')

# '매출' 열의 값을 숫자로 변환
df['매출'] = pd.to_numeric(df['매출'], errors='coerce')

# NaN 값을 제외하고 매출액 평균 계산
average_sales = df['매출'].dropna().mean()

print(f"매출 평균: {average_sales:.2f}")