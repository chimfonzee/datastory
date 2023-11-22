# Install:
```
pip install -r requirements.txt
```

# Create Lexer:
Generate Python code using ANTLR for usage in `main.py`
```
antlr4 DataStory.g4 -Dlanguage=Python3
```

# Running Code:
Make sure to have code within `test.txt` then run:
```
python main.py
```
