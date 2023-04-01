import os

from make_pancakes import make_one_pancake, make_pancakes


def get_default_filepath(filepath, text='_pancake'):
    template_dir = path.dirname(filepath)
    filename = path.basename(filepath)
    dot_idx = filename.find('.')
    if dot_idx < 1:
        new_filename = filename + text
    else:
        print(filename)
        new_filename = filename[:dot_idx] + text + filename[dot_idx:]
    return os.path.join(template_dir, new_filename)


def inline_html(html: str) -> str:
    from css_inline import CSSInliner
    inliner = CSSInliner(remove_style_tags=True)
    return inliner.inline(html)


def create_one_pancake(target_filepath, output_path=None, inline=False):
    pancake = make_one_pancake(target_filepath)

    if not output_path:
        output_path = get_default_filepath(target_filepath)

    if os.path.isfile(output_path) or os.path.isdir(output_path):
        raise Exception(f"File/Dir existed in {output_path}")

    if inline:
        pancake = inline_html(pancake)

    with open(output_path, 'w') as f:
        f.write(pancake)
        print(f'template saved in {output_path}')


def make_many_pancakes(input_dir, output_dir):
    make_pancakes(input_dir, output_dir)


def command_app() -> None:
    import sys
    _, *args = sys.argv

    try:
        target_filepath = args[0]
    except Exception as err:
        raise Exception("Define output path!")

    try:
        target_filepath = args[1]
    except Exception as err:
        output_path = None

    if os.path.isdir(target_filepath):
        make_many_pancakes(target_filepath, output_path)
    else:
        create_one_pancake(target_filepath, None)
