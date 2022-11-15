# Colorize.py

<div>
  <img src="https://media.discordapp.net/attachments/887158781832749086/1041802474782199818/Colorize_logo.png" width="500px" height="100px">
</div>

## What is it and what is it for

[Colorize.py](https://pypi.org/project/colorizelib/) is a very simple to use and understand python library. It allows you to color text in the terminal.
This library is inspired by the **[pycolor](https://github.com/wdrach/pycolor)** library

## instalation

```bash
pip install colorizelib
```

## Functions

| Function | Description |
| --- | --- |
| `colorize(text, foreground, style, background)` | Colorize the text with the foreground, style and background |
| `colorize_foreground(text, foreground)` | Colorize the text with the foreground |
| `colorize_style(text, style)` | Colorize the text with the style |
| `colorize_background(text, background)` | Colorize the text with the background |
| `colorize_rainbow(text, mode_type)` | Colorize the text with a rainbow |
| `get_color_list()` | Get the list of all colors |
| `get_color_name(color)` | Get the name of the color by number |
| `get_color_number(color)` | Get the number of the color by name |

## Exemples

```python
from colorize import colorize

print(colorize.colorize("Hello World", foreground="red", style="bold", background="blue"))
```
![result](https://media.discordapp.net/attachments/887158781832749086/1041831858494775396/image.png)

```python
from colorize import colorize

print(colorize.colorize("Hello World", foreground="blue"))
```
![result](https://media.discordapp.net/attachments/887158781832749086/1041832028854820974/image.png)

```python
from colorize import colorize

print(colorize.colorize_style("Hello World", "bold"))
```
![result](https://media.discordapp.net/attachments/887158781832749086/1041832167161991199/image.png)

```python
from colorize import colorize

print(colorize.colorize_rainbow("Hello World", "foreground"))
```
![result](https://media.discordapp.net/attachments/887158781832749086/1041833768442396733/image.png)

# Contributors

<a href="https://github.com/Bielgomes/Colorize.py/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Bielgomes/Colorize.py"/>
</a>

## How to Contributing

Open pull request 😎