from BuildExcel import markdown_to_excel


def main():
    # Read MarkDown File cities-rads.md and Convert to Excel File cities-rads.xlsx
    markdown_path = "DataSet/cities-rads.md"
    excel = "DataSet/cities-rads.xlsx"
    # Read the markdown file to string.
    with open(markdown_path, 'r') as f:
        markdown = f.read()
    markdown_to_excel(markdown, excel)

if __name__ == '__main__':
    main()
