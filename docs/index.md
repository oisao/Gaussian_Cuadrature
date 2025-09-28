theme:
  name: readthedocs
theme:
  name: material
  palette:
    primary: red
    accent: amber
  font:
    text: Roboto
    code: Fira Code

markdown_extensions:
  - pymdownx.arithmatex:
      generic: true

extra_javascript:
  - javascripts/mathjax.js
  - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js

Este es un ejemplo en línea: $E = mc^2$.

Y una ecuación en bloque:

$$
\int_{0}^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$

