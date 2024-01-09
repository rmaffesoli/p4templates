# P4 Templates

P4 Templates are a Python library to aid in the quick creation of p4 environments for studios that have quick turn around projects and need to deploy a standard setup often..

## Installation

Currently, the main kernel doesn't require any additional libraries beyond Python3 and the P4 commandline tools installed.
You will need to add this package to your site-packages location or add the root path to your PYTHONPATH env variable.
The UI currently requires PyQt6. 

## Pre-requisites
* Ensure `p4` cli is setup 
  * Link: [https://www.perforce.com/manuals/p4guide/Content/P4Guide/basic-tasks.initial.start-client.html](https://www.perforce.com/manuals/p4guide/Content/P4Guide/basic-tasks.initial.start-client.html)
* Provision (or get the info) a Perforce Helix Core server, note the connection string: `ssl:<ip address>:<port>`
* In the root of this directory, create a `.p4config` file with these lines:
  * P4USER=`perforce`
  * P4PORT=`ssl:<ip>:<port>`
* `p4 set P4CONFIG=.p4config`

## Server Configuration File

* Server configuration is taken from the `/p4_templates/config.json` file found in the route of the project.
  * Valid fields are "port","user","password" and "charset"

## Usage

To process a specific json template pass in the file path with the -t flag. 
You can find example templates in the `p4_templates/templates` directory. Copy one if these templates, edit to fit your needs, and then process it to add the requested components to your p4d server. To Note: You will need the p4 Permissions level required to complete these actions for the script to succeed.

```bash
python ./kernel/process_template.py -t /path/to/template/file.json
```

If you have a specifc template predefined you can use the -n --name option that corresponds to either the name field as defined in the tempate file, or the filename itself.

```bash
python ./kernel/process_template.py -n template_name
```

If you are using parameter tags in your template you can use the -p,--parameter flag to input these values for processing. 
The syntax is as follows with a ':' acting a string delimiter between the key and value. 
Any number of parameters may be passed in separated by a space.
For instance if your template uses the parameters 'project' and 'dept' you would use the following syntax to pass the substitutions into the cli utility. 
Within your json file the syntax for parameters is to use curly braces to identify parameter values. 
For example a template json string of: 
`{"streams": [{"depot": "{dept}_depot", "name": "{project}_{dept}_main"}]}` would result in the creation of mainline stream named `demo_3D_main` within the `3D_depot` depot.

```bash
python ./kernel/process_template -n default_unreal_template -p project:demo dept:3D
```

the -d,--dryrun flag can be used to preview the the template output with the parameter substitutions applied. The output will be printed to the command line instead of being processed by the server. 

```bash
python ./kernel/process_template -n default_unreal_template -p project:demo dept:3D -d
```

To load the editor GUI use the folowing command.
TO NOTE: This is currently a non operational work in progress. The readme will be updated when this is ready for use. In the mean time editing and processing can proceed by using yuor favorite text editor to create the json templates and the above cli for processing. 

```bash
python ./p4_template_tool.py
```

## File Population

The template system utilizes Helix Core's branch mappings and the p4 populate command to duplicate files and folders from one depot position on the server into the new template project. For this to operate correctly I recommend you establish a separate template project depot on your p4d server and then use those boilerplate setups as your duplication source.

For example, in the following snippet we see the branch mapping section from a p4 setup template showing how the view section is defined for file propogation including file renaming.
 
```
  "branches": [
    {
      "name": "{project}_populate",
      "options": [
        "unlocked"
      ],
      "view": {
        "//populate_demo/main/old_project/...": "//{project}_depot/{project}_main/new_project/...",
        "//populate_demo/main/old_project/old_project.py": "//{project}_depot/{project}_main/new_project/new_project.py"
      }
    }
  ],
```

## TODO
- [ ] Test coverage
  - Currently there is no test coverage for this project.
- [X] Server details/server config info
  - Currently The server data that will be in use is what you have stored in your environement variables without a way to define these 
- [ ] Documentation
  - More than a readme is needed 
- [ ] Validation 
  - I would prefer if this tool could validate the entries per tab, and particularly on the typemap to stop and erroneous edits.
- [X] Dry run report
  - Would like a dry run report that will preview paths and creation counts
- [X] Convert to p4python?
  - This should likely be done so that the tool can be independant from the p4 commandline calls.
- [ ] Executable?
  - For cleanliness this requires p4python build.
- [ ] Cleaner CLI entry point other than kernel/process_template.py?
  - [ ] A separate entry point should be stablised beyond reaching into the kernel directly.
 
## License

[MIT](https://choosealicense.com/licenses/mit/)