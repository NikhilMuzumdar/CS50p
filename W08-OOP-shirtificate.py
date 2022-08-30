from fpdf import FPDF
from PIL import Image

def main():
    name = input("Name: ")
    image = get_processed_image()
    pdf = render_image(image)
    render_text(pdf, name=name)
    pdf.output("shirtificate.pdf")


def get_processed_image(shrink=0.95):
    im = Image.open("shirtificate.png")
    height, width = (int(im.height * shrink), int(im.width * shrink))
    return im.resize((height, width), resample=Image.Resampling.NEAREST)

def render_image(image, x_margin=5, y_margin=60):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.set_margin(0)
    pdf.add_page()
    pdf.image(image, x=x_margin, y=y_margin)
    return pdf

def render_text(pdf, name="Donald Trump"):
    pdf.set_font("Times", size=32)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(30,120) # x is 30 (210/2 = 105 minus (150/2) = 75)
    pdf.cell(150, 20, txt=f"{name} took CS50!", align="C", border=0)

if __name__ == "__main__":
    main()