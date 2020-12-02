from fdd_sdk.client.document import DocumentClient
from fdd_sdk.utils.hashs import HashUtils
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

from base_demo import fdd_client
from base_demo import token
from base_demo import user_token


# 上传文件
def upload_file_demo():
    try:
        data = {
            'fileType': '1',
            'fileContentHash': '',
        }
        file = open('C:\\山有木兮木有枝.pdf', 'rb')
        file_hash = HashUtils.sha256_file_hex('C:\\山有木兮木有枝.pdf')
        data['fileContentHash'] = file_hash
        print(DocumentClient.upload_file(fdd_client, file, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 下载签署文档
def get_by_sign_file_id_demo():
    try:
        data = {
            'taskId': '签署任务ID',
            'signFileId': '',
        }
        res = DocumentClient.get_by_sign_file_id(fdd_client, data)
        print(res.text)
        with open("D:/签署文件.zip", "wb") as f:
            f.write(res.content)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 下载草稿文档
def get_by_draft_id_demo():
    try:
        data = {
            'draftId': '草稿ID',
            'draftFileId': '草稿文件ID',
        }
        res = DocumentClient.get_by_draft_id(fdd_client, data)
        with open("D:/草稿文件.zip", "wb") as f:
            f.write(res.content)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 关键字查询坐标
def look_up_coordinates_demo():
    try:
        data = {
            'queryInfo': {
                'fileId': '文件ID',
                'keyword': '山',
                'pageNumber': '',
                'keywordStrategy': ''
            }
        }
        print(DocumentClient.look_up_coordinates(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 合同文件验签
def verify_signature_demo():
    try:
        data = {
            'pdfInfo': {
                'fileHash': ''
            }
        }
        file = open('D:\\合同文件.pdf', 'rb')
        file_hash = HashUtils.sha256_file_hex('D:\\合同文件.pdf')
        data['pdfInfo']['fileHash'] = file_hash
        print(DocumentClient.verify_signature(fdd_client, file, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 下载合同技术报告
def contract_report_download_demo():
    try:
        data = {
            'contractInfo': {
                'taskId': ''
            }
        }
        res = DocumentClient.contract_report_download(fdd_client, data)
        with open("D:/合同技术报告.zip", "wb") as f:
            f.write(res.content)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 下载公证处报告
def download_evidence_report_demo():
    try:
        data = {
            'queryInfo': {
                'type': '2',
                'taskId': '签署任务编号',
                'unionIds': ['unionId值']
            }
        }

        res = DocumentClient.download_evidence_report(fdd_client, data)
        with open("D:/公证处报告.zip", "wb") as f:
            f.write(res.content)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    fdd_client.set_token(token)
    #  如果是第三方应用就设置userToken
    # fdd_client.set_user_token(user_token)
    upload_file_demo()
    get_by_sign_file_id_demo()
    get_by_draft_id_demo()
    look_up_coordinates_demo()
    verify_signature_demo()
    contract_report_download_demo()
    download_evidence_report_demo()
