test_settings  = {
    'theme' : 'dark',
    'notifications' : 'enabled',
    'volume' : 'high'
}

def add_setting(settings, setting):
    # desempacota o tuple settings nas variáveis key e value
    key, value = setting

    # converte ANTES de qualquer verificação
    key = key.lower()
    value = value.lower()

    if key in settings:
        return (f"Setting '{key}' already exists! Cannot add a new setting with this name.")

    settings[key] = value
    return (f"Setting '{key}' added with value '{value}' successfully!")

def update_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return (f"Setting '{key}' updated to '{value}' successfully!")
    
    return (f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting (settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return (f"Setting '{key}' deleted successfully!")
    
    return ("Setting not found!")

def view_settings(settings):
    if not settings:
        return ("No settings available.")
    
    result = "Current User Settings:" # adicionar com o for nessa mensagem para retornar na função

    for key, value in settings.items():
        result += f"\n{key.capitalize()}: {value}" # concatena com a string result
    
    return result