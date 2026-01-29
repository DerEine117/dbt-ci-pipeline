import re

# Read the file
with open(r'c:\Users\knabe\OneDrive - Hewlett Packard Enterprise\Documents\Semester 5\data management\dbt-ci-pipeline\latex\includes\text.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove LaTeX commands (chapter, section, subsection)
text_only = re.sub(r'\\chapter\{[^}]*\}', '', content)
text_only = re.sub(r'\\section\{[^}]*\}', '', text_only)
text_only = re.sub(r'\\subsection\{[^}]*\}', '', text_only)

# Remove excess whitespace but keep single spaces
text_only = re.sub(r'\n+', ' ', text_only)
text_only = re.sub(r' +', ' ', text_only)
text_only = text_only.strip()

# Count characters
char_count = len(text_only)

print(f"Flowing text character count (without LaTeX headings): {char_count}")
print(f"Target range: 10,000 - 18,000 characters")
print(f"Status: {'✓ PASS' if 10000 <= char_count <= 18000 else '✗ FAIL'}")
