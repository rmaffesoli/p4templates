# P4 Templates

P4 Templates is a Python library to aid in the quick creation of p4 environments for studios that habe quick turn around projects and need to deploy a standard setup often..

## Installation

Currently the main kernal doesn't require any additional libraries beyond python3. 
The UI currently requires PyQt6, but isn't operational at this time. 

## Usage

If you have a specifc template predefined you can use the -n --name option that corresponds to a key value in the preset_templates.json file

```bash
python ./process_template -n unreal
```

To process a specific json template pass in the file path with the -t flag
```bash
python ./process_template.py -t /path/to/template/file.json
```

To load the GUI, which is currently a non operational work in progress.
```bash
python ./p4_template_gui.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)