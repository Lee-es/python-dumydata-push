@echo off
REM ============================================
REM  run_dummy_uv.bat
REM  - uv 기반 비개발자용 실행 스크립트
REM  - 1) uv sync 로 환경 및 패키지 준비
REM  - 2) uv run main.py 실행
REM ============================================

SET SCRIPT=main.py

echo.
echo  헬스 더미데이터 전송 도구를 실행합니다.
echo  uv를 사용해 가상환경과 패키지를 준비합니다.

REM 1) 의존성 설치 및 .venv 생성
uv sync
IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo  uv sync 실패. uv 설치 여부와 인터넷 연결을 확인하세요.
    pause
    exit /b 1
)

REM 2) 스크립트 실행
echo.
echo 스크립트를 실행합니다...
uv run %SCRIPT%
IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo  실행 중 오류가 발생했습니다. 위 로그를 확인하세요.
    pause
    exit /b 1
)

echo.
echo  작업이 완료되었습니다.
pause