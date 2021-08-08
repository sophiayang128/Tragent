import yaml

AUTH_CONFIG_FILE = 'auth/auth.yaml'

class Auth:
    def get_api_key():
        with open(AUTH_CONFIG_FILE, 'r') as config_file:
            config = yaml.load(config_file)
        return config['google_map']['api_key']