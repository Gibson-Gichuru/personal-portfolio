import  os

class Config:

    SSL_DISABLE = True
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
    @staticmethod
    def init_app(app):

        pass
    pass


class DevelopmentConfig(Config):

    pass


class ProductionConfig(Config):

    @classmethod
    def init_app(cls):

        pass

    pass


class HerokuConfig(ProductionConfig):

    pass



config = {

    'default':DevelopmentConfig,
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'heroku': HerokuConfig
}