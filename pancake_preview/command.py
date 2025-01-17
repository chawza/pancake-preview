import os

from django_pancake.make_pancakes import make_one_pancake


def get_default_filepath(filepath, text='_pancake'):
    template_dir = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    dot_idx = filename.find('.')
    if dot_idx < 1:
        new_filename = filename + text
    else:
        print(filename)
        new_filename = filename[:dot_idx] + text + filename[dot_idx:]
    return os.path.join(template_dir, new_filename)


def get_deafult_dirpath(outdir, text='_pancake'):
    dirname = os.path.basename(outdir)
    parent_dirname = os.path.dirname(outdir)
    new_dirname = dirname + text
    return os.path.join(parent_dirname, new_dirname)


def inline_html(html: str) -> str:
    from css_inline import CSSInliner
    inliner = CSSInliner(remove_style_tags=True)
    return inliner.inline(html)


def create_one_pancake(target_filepath, output_path=None, inline=False, replace=False):
    pancake = make_one_pancake(target_filepath)

    if not output_path:
        output_path = get_default_filepath(target_filepath)

    if not replace:
        if os.path.isfile(output_path) or os.path.isdir(output_path):
            raise Exception(f"File/Dir existed in {output_path}")

    if inline:
        pancake = inline_html(pancake)

    with open(output_path, 'w') as f:
        f.write(pancake)
        replace_text = 'Replacing ' if replace else ''
        print(f'{replace_text}template saved in {output_path}')


def create_many_pancakes(input_dir, output_dir=None, replace=False, inline=False):
    if not output_dir:
        output_dir = get_deafult_dirpath(output_dir)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        create_one_pancake(filepath, output_path, inline, replace)
