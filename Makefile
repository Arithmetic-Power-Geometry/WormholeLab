.PHONY: test run check

test:
	pytest -q

check:
	python SELF_CHECK.py

run:
	streamlit run app.py
