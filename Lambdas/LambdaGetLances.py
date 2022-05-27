import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')

tableMensagens = dynamodb.Table('TabelaDeLances')

def lambda_handler(event, context):
    nome = str(event['nome'])

    try:
        response = tableMensagens.query(
            KeyConditionExpression=Key('nome').eq(nome))

        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }

    except:
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar recuperar mensagens')
        }
