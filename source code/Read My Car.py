# -*- coding: cp949 -*-

# --- 설정 (여기서 수정하세요) ---

# 1. 읽어올 로그 파일의 전체 경로와 이름
log_file_path = r"C:\Users\ASUS\Downloads\Read My Car\candump-2024-04-19_143417.log"

# 2. 저장할 텍스트 파일의 이름 (이 부분을 원하시는 이름으로 수정하세요)
output_file_path = "Read My Car_ascii.txt"

# --- 코드 시작 (여기는 수정할 필요 없어요) ---
print(f"'{log_file_path}' 파일을 읽고 있습니다...")

# 변환된 아스키 데이터를 저장할 리스트
ascii_results = []
converted_count = 0

try:
    # 로그 파일을 한 줄씩 읽습니다.
    with open(log_file_path, 'r') as f:
        for line in f:
            # '#' 문자를 기준으로 뒷부분(데이터)만 잘라냅니다.
            if '#' in line:
                parts = line.split('#')
                hex_data = parts[1].strip() # 16진수 데이터 부분

                try:
                    # 16진수 문자열을 바이트로 변환합니다.
                    byte_data = bytes.fromhex(hex_data)
                    # 바이트를 아스키 문자열로 변환합니다. (오류나는 문자는 '?'로 표시)
                    ascii_string = byte_data.decode('ascii', errors='replace')
                    
                    # 변환된 결과를 리스트에 추가합니다.
                    ascii_results.append(ascii_string)
                    converted_count += 1
                    
                except (ValueError, TypeError):
                    # 16진수 변환이 불가능한 데이터(빈 데이터 등)는 건너뜁니다.
                    continue

    # --- 변환된 결과를 파일에 저장 ---
    print(f"변환된 데이터를 '{output_file_path}' 파일에 저장하는 중...")
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for result in ascii_results:
            f.write(result + '\n') # 한 줄씩 파일에 씁니다.

    print("------------------------")
    print(f"성공! 총 {converted_count}개의 데이터 라인을 '{output_file_path}' 파일에 저장했습니다.")

except FileNotFoundError:
    print(f"오류: '{log_file_path}' 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
except Exception as e:
    print(f"알 수 없는 오류가 발생했습니다: {e}")

# --- 사용자가 Enter를 누를 때까지 대기 ---
input("\n작업이 완료되었습니다. Enter 키를 눌러주세요...")



