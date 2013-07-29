import ImageDraw as _ImageDraw
from math import ceil


class ImageDraw(_ImageDraw.ImageDraw):
    def text(
        self, (x, y), text, halign='left', width=None, height=None, font=None,
        **kwargs
    ):
        if halign == 'center':
            assert(width is not None)
            x += int(round((width / 2.) - self.textsize(text, font)[0] / 2.))
        elif halign == 'right':
            assert(width is not None)
            x += width - self.textsize(text, font)[0]
        _ImageDraw.ImageDraw.text(self, (x, y), text, font=font, **kwargs)

    def textbox(self, pos, lines, font, fill, halign='left'):
        x, y, bx, by = pos
        width = bx - x
        if isinstance(lines, basestring):
            lines = lines.split('\n')
        if font is None:
            font = self.getfont()
        wrapped = []
        for line in lines:
            wrapped += self._wrapline(line, font, width)
        line_space = ceil(self.textsize('M', font)[1] * 1.1)
        for i, line in enumerate(wrapped):
            self.text(
                (x, y + line_space * i), line, font=font, fill=fill,
                halign=halign, width=width
            )

    def _wrapline(self, line, font, width):
        if self.textsize(line, font)[0] < width:
            return [line]
        lines = ['']
        for w in line.split():
            if lines[-1]:
                new_line = lines[-1] + ' ' + w
            else:
                new_line = w
            if self.textsize(new_line, font)[0] < width:
                lines[-1] = new_line
            else:
                lines.append(w)
        return lines

    @classmethod
    def Draw(cls, im, mode=None):
        try:
            return im.getdraw(mode)
        except:
            return cls(im, mode)
