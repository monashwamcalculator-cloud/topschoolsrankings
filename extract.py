import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_docx(docx_path):
    text = []
    try:
        with zipfile.ZipFile(docx_path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.XML(xml_content)
            
            # The XML namespace for Word
            WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
            PARA = WORD_NAMESPACE + 'p'
            TEXT = WORD_NAMESPACE + 't'
            
            for paragraph in tree.iter(PARA):
                texts = [node.text for node in paragraph.iter(TEXT) if node.text]
                if texts:
                    text.append(''.join(texts))
    except Exception as e:
        print(f"Error: {e}")
    return '\n\n'.join(text)

content = extract_text_from_docx(r'C:\Users\Hp\Downloads\Top_100_Finance_Schools_US_Guide.docx')
with open('temp_content.txt', 'w', encoding='utf-8') as f:
    f.write(content)
print("Extracted successfully.")