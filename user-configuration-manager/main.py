class ConfigurationManager:

    def add_setting(self, settings, setting):
        lowerset = tuple(s.lower() for s in setting)
        if lowerset[0] in settings.keys():
            print(f'Setting \'{lowerset[0]}\' already exists! Cannot add a new setting with this name.')
        else:
            newsetting = dict([lowerset])
            settings.update(newsetting)
            print(f'Setting \'{lowerset[0]}\' added with value \'{lowerset[1]}\' successfully!')
        

    def update_setting(self, settings, setting):
        lowerset = tuple(s.lower() for s in setting)
        if lowerset[0] in settings.keys():
            newsetting = dict([lowerset])
            settings.update(newsetting)
            print(f'Setting \'{lowerset[0]}\' updated to value \'{lowerset[1]}\' successfully!') 
        else:
            print(f'Setting \'{setting[0]}\' does not exist! Cannot update a non-existing setting.') 


    def delete_setting(self, settings, setting):
        setting.lower()
        if setting in settings.keys():
            deletedsetting = settings.pop(setting)
            print(f'Setting \'{setting}\' deleted successfully!') 
        else:
            print(f'Setting \'{setting}\' not found!') 
    

    def view_settings(self, settings):
        if not settings:
            return 'No settings available.'
        else:
            return f'Current User Settings:\n{chr(10).join(f"{key}: {value}" for key, value in settings.items())}'
            

def main():
    test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
    instance = ConfigurationManager()
    print(instance.view_settings(test_settings))


if __name__ == "__main__":
    main()