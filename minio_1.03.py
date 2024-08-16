# 导入minio包
from minio import Minio
# 判断异常的包
from minio.error import S3Error
import os

# 连接信息
client = Minio('1.14.126.233:9000', access_key='minioadmin', secret_key='minioadmin', secure=False)
# 判断桶是否存在
found = ''
# 桶的名字
bucket_name = 'demo'

# 1.查找是否有demo的桶
try:
    found = client.bucket_exists(bucket_name)
    print(client.list_buckets())
except S3Error as e:
    print("error:", e)
print('桶是否存在：', found)

# 文件夹路径
path = 'C:/Users/27926/Pictures/demo/'
dirs = os.listdir(path)

# 2.桶存在进行上传操作
try:
    if found:
        for dir in dirs:
            print(path + dir)
            source_file = path + dir
            # 通过 with open 获取文件
            with open(source_file, 'rb') as file:
                # 获取文件大小
                file_size = os.path.getsize(source_file)
                print('文件大小：', file_size)
                # 进行上传操作
                client.put_object(bucket_name, dir, file, file_size, content_type='image/png')
                # 获取URl
                url = client.presigned_get_object(bucket_name, dir)
                print(f'文件 {dir} 上传成功，访问链接：{url}')
except Exception as e:
    print(e)


