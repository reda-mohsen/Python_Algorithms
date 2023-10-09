"""
The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt's image should be centered horizontally.
The user's name should be on top of the shirt, in white text.
"""

# wget https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png

from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def shirtificate(self):
        self.add_page(orientation="P", format="A4")
        self.set_font("Times", "B", 48)
        self.cell(
            w=0,
            h=60,
            txt=f"CS50 Shirtificate",
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=False,
            )
        self.image("shirtificate.png", w=self.epw)
        self.set_font("helvetica", "", 48)
        self.set_font_size(24)
        self.set_text_color(255, 255, 255)
        self.cell(
            w=0,
            h=-245,
            txt=f"{self.name.capitalize()} took CS50",
            align="C"
            )
        self.output("shirtificate.pdf")

    @classmethod
    def get(cls):
        name = input("Name: ")
        return cls(name)


def main():
    pdf = PDF.get()
    pdf.shirtificate()


if __name__ == "__main__":
    main()