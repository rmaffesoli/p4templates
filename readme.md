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

If you are using parameter tags in your template you can use the -p,--parameter flag to input these values for processing. 
The syntax is as follows with a ':' acting a string delimiter between the key and value. 
Any number of parameters may be passed in separated by a space.
For instance if your template uses the parameters 'project' and 'dept' you would use the following syntax to pass the substitutions into the cli utility. 
Within your json file the syntax for parameters is to use curly braces to identify parameter values. 
For example: 
`{"name": "{project}_{dept}_mainline"}` would result in a streamname of `demo_3D_mainline`

```bash
python ./process_template -n unreal -p project:demo dept:3D
```

To load the editor GUI use the folowing command.
TO NOTE: This is currently a non operational work in progress. The readme will be updated when this is ready for use. In the mean time editing and processing can proceed by using yuor favorite text editor to create the json templates and the above cli for processing. 

```bash
python ./p4_template_gui.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)