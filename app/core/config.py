from authx import AuthX, AuthXConfig


#config.py

config = AuthXConfig()
config.JWT_SECRET_KEY = "Nurly_secret_key"
config.JWT_ACCESS_COOKIE_NAME = "COOKIE"
config.JWT_TOKEN_LOCATION = ["cookies"]


security = AuthX(config=config)

