from app.model.demo import MODELS


class demo:
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        return MODELS

    @staticmethod
    def get_by_id(id):
        for model in MODELS:
            if model['id'] == id:
                return model

    @staticmethod
    def create_model(model):
        MODELS.append(model)
        return MODELS
