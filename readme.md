# P4 Templates

P4 Templates is a Python library to aid in the quick creation of p4 environments for studios that have quick turn around projects and need to deploy a standard setup often..

## Installation

Currently the main kernal doesn't require any additional libraries beyond Python3 and the P4 commandline tools installed.
The UI currently requires PyQt6, but isn't operational at this time. 

## Usage

To process a specific json template pass in the file path with the -t flag. 
You can find example templates in the `p4_templates/templates` directory. Copy one if these templates, edit to fit your needs, and then process it to add the requested components to your p4d server. To Note: You will need the p4 Permissions level required to complete these actions for the script to succeed.

```bash
python ./process_template.py -t /path/to/template/file.json
```

If you have a specifc template predefined you can use the -n --name option that corresponds to a key value in the preset_templates.json file

```bash
python ./process_template -n unreal
```

To load the GUI, which is currently a non operational work in progress.
```bash
python ./p4_template_gui.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)