from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Streamlit에서 넘어올 입력 데이터 구조 정의
class PracticeInput(BaseModel):
    level: str
    time: str
    technique: str

@app.post("/recommend")
def get_routine(data: PracticeInput):
    # 1. 기본 루틴 틀 생성
    routine = {
        "title": f"[{data.level}] 맞춤형 {data.technique} 집중 훈련 ({data.time})",
        "warmup": "크로매틱 스케일 및 양손 싱크로나이제이션",
        "main": "",
        "jam": "메트로놈 또는 드럼 비트에 맞춰 배운 내용 응용 잼",
        "tip": ""
    }

    # 2. 테크닉에 따른 메인 연습 내용 분기 (Rule-based)
    if data.technique == "슬랩":
        routine["main"] = "옥타브 썸핑(Thumping) 및 플러킹(Plucking) 패턴 반복"
        routine["tip"] = "엄지손가락의 타격 지점을 넥 끝부분에 일정하게 유지하세요!"
    elif data.technique == "핑거링":
        routine["main"] = "16분음표 얼터네이트 피킹(검지/중지 교차) 지구력 훈련"
        routine["tip"] = "두 손가락의 톤과 볼륨이 균일하게 나도록 앰프 소리에 집중하세요."
    elif data.technique == "피킹":
        routine["main"] = "다운 피킹 및 얼터네이트 피킹을 활용한 8비트 루트 연주"
        routine["tip"] = "손목의 스냅을 활용하고 피크 각도를 조절하여 어택감을 살려보세요."
    elif data.technique == "워킹 베이스":
        routine["main"] = "2-5-1 코드 진행에 맞춘 코드 톤(1, 3, 5, 7음) 분산 연주"
        routine["tip"] = "마디의 첫 박자에는 무조건 루트(Root) 음을 정확히 짚어주세요."

    # 3. 시간에 따른 훈련 시간 분기
    if data.time == "30분 (빠른 연습)":
        routine["warmup"] += " [5분]"
        routine["main"] += " [20분]"
        routine["jam"] += " [5분]"
    elif data.time == "1시간 (표준)":
        routine["warmup"] += " [10분]"
        routine["main"] += " [40분]"
        routine["jam"] += " [10분]"
    else: # 2시간 이상
        routine["warmup"] += " [15분]"
        routine["main"] += " [1시간 15분]"
        routine["jam"] += " [30분 자유 잼]"

    # 추천 결과를 JSON 형태로 반환
    return routine