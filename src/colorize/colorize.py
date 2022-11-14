import random

COLOR_LIST = {
  'black': '0',
  'red': '1',
  'green': '2',
  'yellow': '3',
  'blue': '4',
  'magenta': '5',
  'cyan': '6',
  'white': '7',
  'lightred': '9',
  'lightgreen': '10',
  'lightyellow': '11',
  'lightblue': '12',
  'lightmagenta': '13',
  'lightcyan': '14',
  'grey0': '16',
  'navyblue': '17',
  'darkblue': '18',
  'blue3': '19',
  'blue3': '20',
  'blue1': '21',
  'darkgreen': '22',
  'deepskyblue4': '23',
  'deepskyblue4': '24',
  'deepskyblue4': '25',
  'dodgerblue3': '26',
  'dodgerblue2': '27',
  'green4': '28',
  'springgreen4': '29',
  'turquoise4': '30',
  'deepskyblue3': '31',
  'deepskyblue3': '32',
  'dodgerblue1': '33',
  'green3': '34',
  'springgreen3': '35',
  'darkcyan': '36',
  'lightseagreen': '37',
  'deepskyblue2': '38',
  'deepskyblue1': '39',
  'green3': '4',
  'springgreen3': '41',
  'springgreen2': '42',
  'cyan3': '43',
  'darkturquoise': '44',
  'turquoise2': '45',
  'green1': '46',
  'springgreen2': '47',
  'springgreen1': '48',
  'mediumspringgreen': '49',
  'cyan2': '5',
  'cyan1': '51',
  'darkred': '52',
  'deeppink4': '53',
  'purple4': '54',
  'purple4': '55',
  'purple3': '56',
  'blueviolet': '57',
  'orange4': '58',
  'grey37': '59',
  'mediumpurple4': '6',
  'slateblue3': '61',
  'slateblue3': '62',
  'royalblue1': '63',
  'chartreuse4': '64',
  'darkseagreen4': '65',
  'paleturquoise4': '66',
  'steelblue': '67',
  'steelblue3': '68',
  'cornflowerblue': '69',
  'chartreuse3': '7',
  'darkseagreen4': '71',
  'cadetblue': '72',
  'cadetblue': '73',
  'skyblue3': '74',
  'steelblue1': '75',
  'chartreuse3': '76',
  'palegreen3': '77',
  'seagreen3': '78',
  'aquamarine3': '79',
  'mediumturquoise': '80',
  'steelblue1': '81',
  'chartreuse2': '82',
  'seagreen2': '83',
  'seagreen1': '84',
  'seagreen1': '85',
  'aquamarine1': '86',
  'darkslategray2': '87',
  'darkred': '88',
  'deeppink4': '89',
  'darkmagenta': '90',
  'darkmagenta': '91',
  'darkviolet': '92',
  'purple': '93',
  'orange4': '94',
  'lightpink4': '95',
  'plum4': '96',
  'mediumpurple3': '97',
  'mediumpurple3': '98',
  'slateblue1': '99',
  'yellow4': '100',
  'wheat4': '101',
  'grey53': '102',
  'lightslategrey': '103',
  'mediumpurple': '104',
  'lightslateblue': '105',
  'yellow4': '106',
  'darkolivegreen3': '107',
  'darkseagreen': '108',
  'lightskyblue3': '109',
  'lightskyblue3': '110',
  'skyblue2': '111',
  'chartreuse2': '112',
  'darkolivegreen3': '113',
  'palegreen3': '114',
  'darkseagreen3': '115',
  'darkslategray3': '116',
  'skyblue1': '117',
  'chartreuse1': '118',
  'lightgreen': '119',
  'lightgreen': '120',
  'palegreen1': '121',
  'aquamarine1': '122',
  'darkslategray1': '123',
  'red3': '124',
  'deeppink4': '125',
  'mediumvioletred': '126',
  'magenta3': '127',
  'darkviolet': '128',
  'purple': '129',
  'darkorange3': '130',
  'indianred': '131',
  'hotpink3': '132',
  'mediumorchid3': '133',
  'mediumorchid': '134',
  'mediumpurple2': '135',
  'darkgoldenrod': '136',
  'lightsalmon3': '137',
  'rosybrown': '138',
  'grey63': '139',
  'mediumpurple2': '140',
  'mediumpurple1': '141',
  'gold3': '142',
  'darkkhaki': '143',
  'navajowhite3': '144',
  'grey69': '145',
  'lightsteelblue3': '146',
  'lightsteelblue': '147',
  'yellow3': '148',
  'darkolivegreen3': '149',
  'darkseagreen3': '150',
  'darkseagreen2': '151',
  'lightcyan3': '152',
  'lightskyblue1': '153',
  'greenyellow': '154',
  'darkolivegreen2': '155',
  'palegreen1': '156',
  'darkseagreen2': '157',
  'darkseagreen1': '158',
  'paleturquoise1': '159',
  'red3': '160',
  'deeppink3': '161',
  'deeppink3': '162',
  'magenta3': '163',
  'magenta3': '164',
  'magenta2': '165',
  'darkorange3': '166',
  'indianred': '167',
  'hotpink3': '168',
  'hotpink2': '169',
  'orchid': '170',
  'mediumorchid1': '171',
  'orange3': '172',
  'lightsalmon3': '173',
  'lightpink3': '174',
  'pink3': '175',
  'plum3': '176',
  'violet': '177',
  'gold3': '178',
  'lightgoldenrod3': '179',
  'tan': '180',
  'mistyrose3': '181',
  'thistle3': '182',
  'plum2': '183',
  'yellow3': '184',
  'khaki3': '185',
  'lightgoldenrod2': '186',
  'lightyellow3': '187',
  'grey84': '188',
  'lightsteelblue1': '189',
  'yellow2': '190',
  'darkolivegreen1': '191',
  'darkolivegreen1': '192',
  'darkseagreen1': '193',
  'honeydew2': '194',
  'lightcyan1': '195',
  'red1': '196',
  'deeppink2': '197',
  'deeppink1': '198',
  'deeppink1': '199',
  'magenta2': '200',
  'magenta1': '201',
  'orangered1': '202',
  'indianred1': '203',
  'indianred1': '204',
  'hotpink': '205',
  'hotpink': '206',
  'mediumorchid1': '207',
  'darkorange': '208',
  'salmon1': '209',
  'lightcoral': '210',
  'palevioletred1': '211',
  'orchid2': '212',
  'orchid1': '213',
  'orange1': '214',
  'sandybrown': '215',
  'lightsalmon1': '216',
  'lightpink1': '217',
  'pink1': '218',
  'plum1': '219',
  'gold1': '220',
  'lightgoldenrod2': '221',
  'lightgoldenrod2': '222',
  'navajowhite1': '223',
  'mistyrose1': '224',
  'thistle1': '225',
  'yellow1': '226',
  'lightgoldenrod1': '227',
  'khaki1': '228',
  'wheat1': '229',
  'cornsilk1': '230',
  'grey100': '231',
  'grey3': '232',
  'grey7': '233',
  'grey11': '234',
  'grey15': '235',
  'grey19': '236',
  'grey23': '237',
  'grey27': '238',
  'grey30': '239',
  'grey35': '240',
  'grey39': '241',
  'grey42': '242',
  'grey46': '243',
  'grey50': '244',
  'grey54': '245',
  'grey58': '246',
  'grey62': '247',
  'grey66': '248',
  'grey70': '249',
  'grey74': '250',
  'grey78': '251',
  'grey82': '252',
  'grey85': '253',
  'grey89': '254',
  'grey93': '255'
}

RAINBOW_COLORS = [196, 202, 208, 214, 220, 226, 190, 154, 118, 82, 46, 47, 48, 49, 50, 51, 45, 39, 33, 27, 21, 57, 93, 129, 165, 201, 129, 21, 33, 45, 50, 47, 82, 154, 226, 208]

COLOR_BASE = '\033['
END = '\033[0m'

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