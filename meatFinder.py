import PyPDF2


class MeatFinder:

    def extract_text_from_pdf(pdf_path: str):
        with open(pdf_path, 'rb') as pdf:
            reader = PyPDF2.PdfReader(pdf, strict=False)
            text = []

            for page in reader.pages:
                context = page.extract_text()
                text.append(context)

        length_of_text = len(text)
        full_text = ''
        for x in range(length_of_text):
            full_text += text[x]

        new_list = full_text.split('\n')

        indexes_found = []
        for s in new_list:
            if "kjøttdeig" in s.lower():
                print()
                print(new_list.index(s))
                indexes_found.append(new_list.index(s))
                print()
        elements_of_interest = []
        for x in indexes_found:
            for i in range(x, x+5):
                elements_of_interest.append(new_list[i])
        return elements_of_interest


if __name__ == '__main__':
    pdf_path = 'dagens_pdf.pdf'

    text = MeatFinder.extract_text_from_pdf(pdf_path)
    print(text)
