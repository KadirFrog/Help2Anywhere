class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class ColorPalette:
    def __init__(self, color_1: Color, color_2: Color, color_3: Color, color_4: Color,
                 background_color: Color):
        
        self.color_1: Color = color_1
        self.color_2: Color = color_2
        self.color_3: Color = color_3
        self.color_4: Color = color_4
        self.background_color: Color = background_color

class FontPalette:
    def __init__(self, font_1: str, font_2: str, font_3 : str, font_4 : str, font_5: str):
        self.font_1: str = font_1
        self.font_2: str = font_2
        self.font_3: str = font_3
        self.font_4: str = font_4
        self.font_5: str = font_5
class Theme:
    def __init__(self, theme_string: str, color_palette: ColorPalette, font_palette: FontPalette):
        self.theme_string: str = theme_string
        self.color_palette: ColorPalette = color_palette
        self.font_palette: FontPalette = font_palette

    def __init__(self, theme_string: str):
        self.theme_string: str = theme_string
        color_1 = Color(79, 129, 189) # Dark Blue
        color_2 = Color(52, 152, 219) # Blue
        color_3 = Color(0, 102, 204) # Deep Blue
        color_4 = Color(236, 240, 241)  # Light Gray
        background_color = Color(34, 47, 62)  # Dark Blue-Gray
        self.color_palette: ColorPalette = ColorPalette(color_1, color_2, color_3, color_4, background_color)
        font_1 = "Arial, sans-serif"  # Main headings
        font_2 = "Helvetica, sans-serif"  # Subheadings
        font_3 = "Verdana, sans-serif"  # Paragraphs
        font_4 = "Tahoma, sans-serif"  # Captions
        font_5 = "Times New Roman, serif"  # Special emphasis
        self.font_palette = FontPalette(font_1, font_2, font_3, font_4, font_5)
