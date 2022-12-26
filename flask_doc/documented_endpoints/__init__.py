from flask import Blueprint
from flask_restx import Api

from flask_doc.documented_endpoints.telegrambot import namespace as bot

blueprint = Blueprint('documented_api', __name__)

api_extension = Api(
    blueprint,
    title='ATGT',
    version='1.0',
    description='This is API for ATGT module'
)

api_extension.add_namespace(bot)
