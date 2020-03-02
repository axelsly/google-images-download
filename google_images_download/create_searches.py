import json
import argparse
import re
from jinja2 import Environment, FileSystemLoader
import os



def generate_arg_parser():
    desc = u'{0} [Args] [Options]\nDetailed options -h or --help'.format(__file__)
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        '--output-dir',
        type=str,
        default='./',
        help='Output directory of search json'
    )

    return parser


def create_search_json(output_dir):
    # Query user for image types for this dataset
    image_search_type = input("Image search type:\n")
    # search_output_directory = input("Search output directory:\n")
    # chromedriver = input("Chromedriver path:\n")

    jinja_env = Environment(loader=FileSystemLoader(searchpath="./"))
    template = jinja_env.get_template('search.json.template')

    # with open("search.json.template", 'r') as json_template:
    #     template_json_format_string = json_template.read()
    # print (template_json_format_string)

    while(True):
        # Query user for search
        image_search_keywords = input("Image search keywords:\n")
        if image_search_keywords == "":
            break

        # Fill out template
        formatted_json_string = template.render(keywords=image_search_keywords) #, type=image_search_type, output_directory=search_output_directory, chromedriver=chromedriver)
        output_filename = "{0}.json".format(re.sub('\s+', '-', image_search_keywords))
        output_filepath = os.path.join(output_dir, output_filename)

        with open(output_filepath, 'w') as outfile:
            outfile.write(formatted_json_string)


if __name__ == '__main__':
    parser = generate_arg_parser()
    args = parser.parse_args()
    create_search_json(args.output_dir)



