# project/config.py

class BaseConfig:
    """Base configaration"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig:
    """Development configaration"""
    DEBUG = True


class TestingConfig:
    """Testing configaration"""
    DEBUG = True
    TESTING = True


class ProductionConfig:
    DEBUG = False
