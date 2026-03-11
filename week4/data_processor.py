def clean_data(data):
    """
    입력된 문자열 데이터의 공백을 제거하고 정제합니다.
    [리뷰 반영] 숫자형 데이터 입력 시 예외 처리 추가
    """
    if data is None:
        return ""
    
    # 데이터가 문자열이 아닐 경우 문자열로 변환
    if not isinstance(data, str):
        data = str(data)
        
    return data.strip()