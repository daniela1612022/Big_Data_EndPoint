from flask import Flask, render_template
import boto3

app = Flask(__name__)

# Configurar boto3 para acceder a S3
s3 = boto3.client('s3')

@app.route('/')
def list_buckets():
    # Obtener la lista de buckets
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return render_template('buckets.html', buckets=buckets)

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000, debug=True)

# Comando para verlos en consola aws s3 ls 
