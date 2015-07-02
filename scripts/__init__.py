import numpy
import cairo
import math
import mcpi


def circle(diameter):
    format = cairo.FORMAT_RGB16_565
    stride = cairo.ImageSurface.format_stride_for_width(format, diameter)
    data = numpy.zeros((diameter, diameter, stride), dtype=numpy.uint8)
    surface = cairo.ImageSurface.create_for_data(data, format, diameter, diameter)
    context = cairo.Context(surface)

    context.set_antialias(cairo.ANTIALIAS_NONE)
    context.arc(diameter/2, diameter/2, diameter/2, 0, 2*math.pi)
    context.set_line_width(1)
    context.set_source_rgb(1,1,1)
    context.stroke()

    surface.write_to_png("circle.png")

    return data
