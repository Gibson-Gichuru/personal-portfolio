

class Config:
    
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