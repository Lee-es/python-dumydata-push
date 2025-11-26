UV := uv
SCRIPT := main.py

# 1) 의존성 설치 및 가상환경(.venv) 준비
install:
	$(UV) sync

run: install
	$(UV) run $(SCRIPT)

clean:
	rm -rf .venv .uv __pycache__ .pytest_cache
	@echo "✔ 정리 완료"