import json
from datetime import datetime
import boto3


dynamodb = boto3.resource('dynamodb')

tableMensagens = dynamodb.Table('TabelaDeLances')


def lambda_handler(event, context):
    data_hora = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    nome = str(event['nome'])
    produto = str(event['produto'])
    lance = str(event['lance'])

    try:
        tableMensagens.put_item(
            Item={
                'nome': nome, # Chave de Partição  no Banco
                'data_hora': data_hora, # Chave de Ordenação no Banco
                'produto': produto,
                'lance': lance
            }
        )

        return {
        # Sucesso
            'statusCode': 200,
            'body': json.dumps('Lance de '
                               + nome
                               + ' ao produto '
                               + produto
                               + ' no valor de '
                               + lance
                               + ' inserida no Banco de Dados')
        }

    except:
        print('Erro: lambda function terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem')
        }
