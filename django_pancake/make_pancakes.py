from django_pancake.flatten import flatten, TemplateDirectory
import os


def template_names(input_dir, prefix=''):
    for filename in os.listdir(input_dir):
        template_name = os.path.join(prefix, filename)
        full_name = os.path.join(input_dir, filename)
        if os.path.isdir(full_name):
            for name in template_names(full_name, template_name):
                yield name
        else:
            yield template_name


def make_pancakes(input_dir, output_dir):
    templates = TemplateDirectory(input_dir)
    for template_name in template_names(input_dir):
        print("Writing %s" % template_name)
        pancake = flatten(template_name, templates)
        outfile = os.path.join(output_dir, template_name)
        try:
            os.makedirs(os.path.dirname(outfile))
        except OSError:  # Already exists.
            pass
        with open(outfile, 'w') as fp:
            fp.write(pancake)


def make_one_pancake(template_path) -> None:
    template_name = os.path.basename(template_path)
    template_dir = os.path.dirname(template_path)
    templates = TemplateDirectory(template_dir)
    return flatten(template_name, templates)


if __name__ == "__main__":
    import sys
    make_pancakes(sys.argv[1], sys.argv[2])
