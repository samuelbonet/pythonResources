import json
import boto3
import logging

# Configurar el logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Inicializar el cliente de S3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Obtener la información del archivo subido desde el evento de S3
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    try:
        # Descargar el archivo desde S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')
        
        # Contar palabras
        word_count = len(file_content.split())
        
        # Imprimir y retornar el resultado
        logger.info(f'El archivo {file_key} contiene {word_count} palabras.')
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'El archivo {file_key} contiene {word_count} palabras.')
        }
        
    except Exception as e:
        logger.error(f'Error al procesar el archivo {file_key} del bucket {bucket_name}: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error al procesar el archivo {file_key}.')
        }