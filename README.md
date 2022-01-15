### Readme

#### How to use

Run sequentially:

1. Fix errors in XML files with `correct.sh`. Note that XML files must be placed within the same directory with Bash script.
2. Parse XML file(s) by running `xml_parser.py` with name(s) of file(s) as mandatory parameters. [JSONL](https://jsonlines.org/) file(s) will be created as a result.
3. Create `*.parquet ` files by running `jsonl_parser.py`. Use `--active` and `--address` parameters in order to parse only active-state entities, and parse address strings into its components.

#### Restrictions

1. You need a lot of space on your drive.
2. Parsing addresses into components somewhen inaccurate. Managers posts too.
