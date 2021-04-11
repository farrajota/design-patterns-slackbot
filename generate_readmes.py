import os
from string import capwords
import json


def main(path: str):
    filenames: list = os.listdir(path)

    rows = []
    category_readmes = {}
    category_names = []
    for filename in sorted(filenames):
        filepath = os.path.join(path, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)

        name = data["name"]
        summary = data["summary"]
        categories = data["category"]
        categories_str = ""
        if any(categories):
            categories_str = " ".join([f"[{capwords(category)}]({category.lower().replace(' ', '_')}.md)" for category in categories])
        try:
            examples = data["example"]
        except KeyError:
            exampels = []
        examples_str = ""
        if any(examples):
            examples_str = " ".join([f"[{capwords(example['language'])}]({example['href']})" for example in examples])

        row = f"| {name} | {summary} | {categories_str} | {examples_str} |"

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

    with open("README.md", "w") as f:
        f.write("# Design Patterns\n")
        f.write("\n")
        f.write("List fo design patterns I've found that look promising to learn more about / take a look at.\n")
        f.write("\n")
        f.write("## Catalog of patterns\n")
        f.write("\n")
        f.write("| Pattern | Summary | Category | Implementations |\n")
        f.write("| --- | --- | --- | --- |\n")
        for row in rows:
            f.write(f"{row}\n")
        f.write("\n")
        f.write("## Categories of Design Patterns\n")
        f.write("\n")
        for category in unique_categories:
            f.write(f"- [{capwords(category)}]({category.lower().replace(' ', '_')}.md)\n")
        f.write("\n")
        f.write("# References\n")
        f.write("\n")
        f.write("- https://docs.microsoft.com/en-us/azure/architecture/patterns/index-patterns\n")
        f.write("\n")
        f.write("# License\n")
        f.write("\n")
        f.write("[MIT License](LICENSE)\n")

    for category in unique_categories:
        category_filename = f"{category.lower().replace(' ', '_')}.md"
        with open(category_filename, "w") as f:
            f.write(f"# {capwords(category)} Patterns\n")
            f.write("\n")
            f.write("| Pattern | Summary | Implementations |\n")
            f.write("| --- | --- | --- |\n")
            for row in category_readmes[category_filename]:
                f.write(f"{row}\n")


if __name__ == '__main__':
    main(path='patterns/')
