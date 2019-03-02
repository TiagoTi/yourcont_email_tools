def helper_load_template(where, type_, name, ext):
    file = ''
    with open(f'{where}/{type_}/{name}.{ext}', 'r') as local_file:
        file += local_file.read()
    return file
