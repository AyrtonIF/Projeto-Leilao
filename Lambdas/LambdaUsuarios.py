import json
from datetime import datetime
import boto3

dynamodb = boto3.resource('dynamodb')

tableLances = dynamodb.Table('TabelaDeUsuarios')

def lambda_handler(event, context):
    data_hora = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    login = str(event['login'])
    senha = str(event['senha'])

    try:
        tableLances.put_item(
            Item={
                'login': login, # Chave de Partição  no Banco
                'senha': senha,
                'data_hora': data_hora, # Chave de Ordenação no Banco
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Usuario '
                               + login
                               + ' e Senha '
                               + senha
                               + ' inseridos no Banco de Dados')
        }

    except:
        print('Erro: LambdaDoJonas terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem')
        }
