import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')

tableMensagens = dynamodb.Table('TabelaDeUsuarios')

def lambda_handler(event, context):
    login = str(event['login'])

    try:
        response = tableMensagens.query(
            KeyConditionExpression=Key('login').eq(login))

        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }

    except:
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar recuperar mensagens')
        }
