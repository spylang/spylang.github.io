build:
	uv run build.py

clean:
	rm -rf public

serve:
	uv run python -m http.server -d public
