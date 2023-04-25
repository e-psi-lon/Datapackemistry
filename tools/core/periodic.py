from .elements import elements, Image

BLANK_PERIOD = (181, 159, 119, 255)
SIZE = (288, 148)
RESCALED_SIZE = (1440, 740)

class PeriodicTableBuilder:
    def __init__(self):
        self.image = Image.new("RGBA", SIZE, BLANK_PERIOD)
        self.draw()
    
    def draw(self):
        for i in  elements:
            img, coords = i.getDrawStruct()
            self.image.paste(img, coords.pos, img)
    
    def show(self):
        tmp = self.image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
        tmp.show()
    
    def save(self, path: str):
        tmp = self.image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
        tmp.save(fp=path+"/000_TableauPNG.png",format="png")
