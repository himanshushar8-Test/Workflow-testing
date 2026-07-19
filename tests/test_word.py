from pathlib import Path

from docx import Document

from tests.word import create_word_document


def test_create_word_document(tmp_path: Path) -> None:
    output_path = create_word_document("hello from test", filename="demo.docx", save_dir=tmp_path)

    assert output_path.exists()

    document = Document(output_path)
    paragraphs = [paragraph.text for paragraph in document.paragraphs]
    assert paragraphs == ["hello from test"]
