DOC_SECTIONS = ["About", "Stack", "Project structure", "Run tests", "Reports", "CI"]

def show_doc_sections() -> None:
    for item in DOC_SECTIONS:
        print(item)

if __name__ == "__main__":
    show_doc_sections()
