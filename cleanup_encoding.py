import os
import re

directory = '.'

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                # Read with utf-8, but might fail if already corrupted
                # So we read as utf-8, ignore errors? Better, let's read with cp1252 or utf-8 and replace the corrupted sequences.
                # Actually, reading as utf-8 should work since it's an HTML file.
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Common corruption patterns:
                # Ã‚Â (which is Â in windows-1252 but corrupted in utf-8) -> non-breaking space
                content = content.replace("Ã‚Â", "")
                content = content.replace("Â", "")
                content = content.replace("â€\"", "–") # en dash
                content = content.replace("â€'", "—") # em dash
                content = content.replace("â€™", "’") # right single quote
                content = content.replace("â€œ", "“") # left double quote
                content = content.replace("â€\x9d", "”") # right double quote
                
                # In previous steps, it was specifically mentioned that "A" or "?\"" might be there.
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
print("HTML encoding cleanup complete.")
