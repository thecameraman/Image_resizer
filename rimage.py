from __future__ import annotations

from dataclasses import dataclass, astuple
from itertools import cycle
from typing import List

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


@dataclass
class Pixel:
  red: int
  green: int
  blue: int
  # alpha: float = 1


pixel = Pixel(255,0,0)
pixel

marigold: Pixel = Pixel(234,162,33)
red: Pixel = Pixel(255,0,0)

Image = List[List[Pixel]]


def create_image(*colors: Pixel, blocksize: int = 10, squaresize: int = 9) -> Image:
  """ Make a square image (same width and height) from blocks of a configurable number of pixels.
  Args:
      colors (Pixel): Iterable of colors to render in order of arguments.
      blocksize (int, optional): [description]. Defaults to 10.
      squaresize (int, optional): [description]. Defaults to 9.
  Returns:
      Image: A beautiful picture of squares!
  """
  img: list = []
  colors = cycle(colors)
  for row in range(squaresize):
    row: list = []
    for col in range(squaresize):
      color = next(colors) # set color
      for _ in range(blocksize):
        values: list[int] = list(astuple(color))
        row.append(values)
    [img.append(row) for _ in range(squaresize)] # creates row height
  return img


if __name__ == '__main__':
  image = create_image(marigold, red)
  plt.imshow(image)
