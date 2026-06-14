import streamlit as st
import requests

# 페이지 기본 설정
st.set_page_config(page_title="베이스 연습 루틴 추천기", page_icon="🎸", layout="centered")

st.title("🎸 베이스 맞춤형 연습 루틴 메이커")
st.write("오늘 어떻게 연습해야 할지 막막하신가요? 실력과 시간을 입력하면 최적의 루틴을 짜드립니다!")
st.divider()

# 1. 사용자 입력 받기 (화면을 반으로 나누어 배치)
col1, col2 = st.columns(2)

with col1:
    level = st.selectbox("자신의 현재 실력은?", ["초급 (입문자)", "중급 (합주 가능)", "고급 (자유로운 연주)"])
    time = st.radio("오늘 확보한 연습 시간은?", ["30분 (빠른 연습)", "1시간 (표준)", "2시간 이상 (하드코어)"])

with col2:
    technique = st.selectbox("오늘 집중적으로 파고 싶은 테크닉은?", ["핑거링", "슬랩", "피킹", "워킹 베이스"])

# FastAPI 서버 주소 (docker-compose 환경의 서비스명 'back')
FASTAPI_URL = "http://back:8000/recommend"

st.write("") # 빈 줄 띄우기

# 2. 추천 요청 버튼
if st.button("🔥 오늘의 연습 루틴 생성하기", use_container_width=True):
    # FastAPI에 보낼 데이터 형태
    payload = {
        "level": level,
        "time": time,
        "technique": technique
    }
    
    with st.spinner("최적의 연습 루틴을 계산하는 중..."):
        try:
            # 3. FastAPI에 요청 보내기
            response = requests.post(FASTAPI_URL, json=payload)
            response.raise_for_status()
            
            # 4. 결과 받아 화면에 표시하기
            result = response.json()
            
            st.success("루틴이 완성되었습니다! 앰프를 켜세요!")
            
            # 결과 카드 UI로 깔끔하게 출력
            with st.container():
                st.subheader(result["title"])
                st.write(f"🏃 **워밍업:** {result['warmup']}")
                st.write(f"🎸 **메인 연습:** {result['main']}")
                st.write(f"🎧 **마무리 잼:** {result['jam']}")
                
                st.info(f"💡 **꿀팁:** {result['tip']}")
                
        except Exception as e:
            st.error(f"서버에 연결할 수 없습니다. Docker 컨테이너가 잘 띄워져 있는지 확인하세요. (에러: {e})")