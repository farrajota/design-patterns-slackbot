import os
from string import capwords
import json


def generate_cloud_design_patterns_readmes(dirpath: str):
    dirpath_patterns: str = os.path.join(dirpath, "patterns")
    filenames: list = os.listdir(dirpath_patterns)

    rows = []
    category_readmes = {}
    category_names = []
    for filename in sorted(filenames):
        filepath = os.path.join(dirpath_patterns, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)

        name = data["name"]
        summary = data["summary"]
        categories = data["category"]
        categories_str = ""
        reference = data["reference"]
        if any(categories):
            categories_str = " ".join([f"[{capwords(category)}]({category.lower().replace(' ', '_')}.md)" for category in categories])

        try:
            examples = data["example"]
        except KeyError:
            examples = []
        examples_str = ""
        if any(examples):
            examples_str = " ".join([f"[{capwords(example['language'])}]({example['href']})" for example in examples])

        try:
            name_href = f"[{name}]({reference[0]['href']})"
        except KeyError:
            name_href = f"[{name}](#)"

        row = f"| {name_href} | {summary} | {categories_str} | {examples_str} |"

        # readme.md
        rows.append(row)

        # design categories (.md)
        for category in categories:
            category_filename = f"{category.lower().replace(' ', '_')}.md"
            if category_filename not in category_readmes:
                category_readmes[category_filename] = []
            category_readmes[category_filename].append(f"| {name} | {summary} | {examples_str} |")

        for category in categories:
            category_names.append(category)

    unique_categories = list(set(category_names))

    with open(os.path.join(dirpath, "README.md"), "w") as f:
        f.write("# Azure Cloud Design Patterns\n")
        f.write("\n")
        f.write("List of design patterns for cloud applications.\n")
        f.write("\n")
        f.write("## Design Patterns Categories\n")
        f.write("\n")
        for category in sorted(unique_categories):
            f.write(f"- [{capwords(category)}]({category.lower().replace(' ', '_')}.md)\n")
        f.write("\n")
        f.write("## Catalog of patterns\n")
        f.write("\n")
        f.write("| Pattern | Summary | Category | Implementations |\n")
        f.write("| --- | --- | --- | --- |\n")
        for row in rows:
            f.write(f"{row}\n")
        f.write("\n")
        f.write("# References\n")
        f.write("\n")
        f.write("- https://docs.microsoft.com/en-us/azure/architecture/patterns/index-patterns\n")

    for category in unique_categories:
        category_filename = f"{category.lower().replace(' ', '_')}.md"
        with open(os.path.join(dirpath, category_filename), "w") as f:
            f.write(f"# {capwords(category)} Patterns\n")
            f.write("\n")
            f.write("| Pattern | Summary | Implementations |\n")
            f.write("| --- | --- | --- |\n")
            for row in sorted(category_readmes[category_filename]):
                f.write(f"{row}\n")


if __name__ == '__main__':
    parent_dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    generate_cloud_design_patterns_readmes(dirpath=parent_dirpath)
