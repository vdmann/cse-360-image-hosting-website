from imagekit import ImageSpec
from imagekit.processors import ResizeToFill

class Thumbnail(ImageSpec):
    processors = [ResizeToFill(100, 50)]
    format = 'JPEG'
    options = {'quality': 60}
    source_file = open('/path/to/myimage.jpg')
	image_generator = Thumbnail(source=source_file)
	result = image_generator.generate()