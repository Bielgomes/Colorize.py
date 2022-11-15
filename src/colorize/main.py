import random
from colorize.constants import COLOR_BASE, COLOR_LIST, RAINBOW_COLORS, END

def get_foreground(foreground):
  colors = ''

  if foreground in ["random", "rand"]:
    colors += f"{COLOR_BASE}38;5;{random.randint(1,256)}m"
  elif type(foreground) is str:
    try:
      colors += f"{COLOR_BASE}38;5;{COLOR_LIST[foreground.lower()]}m"
    except:
      raise ValueError('Invalid foreground color')
  elif type(foreground) is int:
    if foreground < 0 or foreground > 255:
      raise ValueError('Invalid foreground color')
    colors += f"{COLOR_BASE}38;5;{foreground}m"

  return colors

def get_background(background):
  colors = ''

  if background in ["random", "rand"]:
    colors += f"{COLOR_BASE}48;5;{random.randint(1,256)}m"
  elif type(background) is str:
    try:
      colors += f"{COLOR_BASE}48;5;{COLOR_LIST[background.lower()]}m"
    except:
      raise ValueError('Invalid background color')
  elif type(background) is int:
    if background < 0 or background > 255:
      raise ValueError('Invalid background color')
    colors += f"{COLOR_BASE}48;5;{background}m"

  return colors

def get_style(style):
  colors = ''

  match style:
    case 'bold': colors = f"{COLOR_BASE}1m"
    case 'dim': colors =  f"{COLOR_BASE}2m"
    case 'italic': colors = f"{COLOR_BASE}3m"
    case 'underline': colors = f"{COLOR_BASE}4m"
    case 'blink': colors =  f"{COLOR_BASE}6m"
    case 'neative': colors = f"{COLOR_BASE}2m"

  return colors

def get_color_number(color: str):
  if type(color) is not str:
    raise ValueError('Invalid color')
  try:
    return COLOR_LIST[color.lower()]
  except:
    raise ValueError('Invalid color')

def get_color_name(color: int):
  if type(color) is not int:
    raise ValueError('Invalid color number')
  if color < 0 or color > 255:
    raise ValueError('Invalid color number')

  for value in COLOR_LIST:
    if COLOR_LIST[value] == str(color):
      return value

  return None

def get_color_list():
  return COLOR_LIST

def colorize_rainbow(text, mode_type):
  rainbowned = ""
  count = 0
  mode = 38

  if mode_type == "background":
    mode = 48
  elif mode_type == "foreground":
    mode = 38
  else:
    raise ValueError('Invalid mode type')
  
  for i in text:
    rainbowned += f"{COLOR_BASE}{mode};5;{RAINBOW_COLORS[count]}m{i}"

    count += 1
    if count == len(RAINBOW_COLORS):
      count = 0

  return f"{rainbowned}{COLOR_BASE}{END}"

def colorize_foreground(text, foreground):
  colors = ''

  if foreground == "rainbow":
    return colorize_rainbow(text, "foreground")
  else:
    colors += get_foreground(foreground)

  return f"{colors}{text}{END}"

def colorize_style(text, style):
  styles = ''

  styles += get_style(style)

  return f"{styles}{text}{END}"

def colorize_background(text, background):
  colors = ''

  if background == "rainbow":
    return colorize_rainbow(text, "background")
  else:
    colors += get_background(background)

  return f"{colors}{text}{END}"

def colorize(text, foreground=None, style=None, background=None):
  colors = ''
  styles = ''

  if foreground == "rainbow":
    return colorize_rainbow(text, "foreground")
  else:
    colors += get_foreground(foreground)

  if background == "rainbow":
    return colorize_rainbow(text, "background")
  else:
    colors += get_background(background)

  styles += get_style(style)

  return f"{colors}{styles}{text}{END}"