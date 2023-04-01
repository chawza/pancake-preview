# Pancake Preview
A forked of [django-pancake](https://github.com/adrianholovaty/django-pancake) with additional features:
- live preview
- html file converter

## Live Preview
Run a live preview server that updated on every template file changes on development
```
Usage: python -m pancake_preview liv[OPTIONS] TARGET

Arguments:  TARGET  [required]
Options:  --help  Show this message and exit
```

## Converter
Convert django template file into flatten html file (optional `css` element inliner)
```
python -m pancake_preview convert [OPTIONS] TARGET

Arguments:
  TARGET  [required]

Options:
  --output TEXT
  --inline / --no-inline    [default: no-inline]
  --replace / --no-replace  [default: no-replace]
  --help                    Show this message and exit.
```