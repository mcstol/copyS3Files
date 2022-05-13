import  boto3

s3 = boto3.client('s3',
                  region_name='REGION_NAME',
                  aws_access_key_id='ACCESS_KEY_ID',
                  aws_secret_access_key='SECRET_ACCESS_KEY'
                  )

response = s3.list_objects(Bucket='mpmjadmin')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(f' {response["Contents"]}')
    for obj in response['Contents']:
        key = obj['Key']
        # print(key)
        path_list = key.split('/')
        if path_list[0] == 'mpm':
            if path_list[3] == 'partituras':
                file_name = path_list[2]
                download_key = '/'.join(path_list)
                print(download_key)
                upload_key = 'musica/{}/{}.pdf'.format(path_list[2],path_list[2])
                s3.copy_object(
                    Bucket='local.musicasparamissa.com.br',
                    Key= upload_key,
                    CopySource= {
                        'Bucket': 'mpmjadmin',
                        'Key': download_key
                    },
                )
                # # print(path_list[2])
                # s3: // local.musicasparamissa.com.br / musica / a - abstinencia - quaresmal / a - abstinencia - quaresmal.pdf
