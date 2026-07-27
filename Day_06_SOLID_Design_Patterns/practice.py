"""
Day 06 - Practice Exercises & Challenges
"""
from abc import ABC, abstractmethod

class DocumentParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> str:
        pass


class PDFParser(DocumentParser):
    def parse(self, file_path: str) -> str:
        return f"Parsing PDF file at {file_path}"


class CSVParser(DocumentParser):
    def parse(self, file_path: str) -> str:
        return f"Parsing CSV file at {file_path}"


class JSONParser(DocumentParser):
    def parse(self, file_path: str) -> str:
        return f"Parsing JSON file at {file_path}"


class DocumentParserFactory:
    @staticmethod
    def get_parser(extension: str) -> DocumentParser:
        ext = extension.lower().strip('.')
        if ext == "pdf":
            return PDFParser()
        elif ext == "csv":
            return CSVParser()
        elif ext == "json":
            return JSONParser()
        else:
            raise ValueError(f"No parser available for extension: {extension}")


if __name__ == "__main__":
    parser = DocumentParserFactory.get_parser("pdf")
    print(parser.parse("sample.pdf"))
