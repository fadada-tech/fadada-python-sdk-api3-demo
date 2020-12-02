from fdd_sdk.client.template import TemplateClient
from fdd_sdk.utils.hashs import HashUtils
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

from base_demo import fdd_client
from base_demo import token
from base_demo import user_token


# 上传企业模板文件
def upload_company_template_file_demo():
    data = {
        'templateInfo': {
            'fileHash': '',
            'fileType': '1',
            'templateId': '模板编号'
        }
    }

    file = open('D:\\合同模板文件.pdf', 'rb')
    data['templateInfo']['fileHash'] = HashUtils.sha256_file_hex('D:\\合同模板文件.pdf')
    print(TemplateClient.upload_company_template_file(fdd_client, file, data))


# 修改企业模板信息
def update_company_template_demo():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板编号',
                'templateName': '模板名称',
                'sortType': '1',
                'templateRemark': '备注信息',
                'targets': [{
                    'targetId': '',
                    'roleName': '乙方',
                    'roleType': '1'
                }]
            }
        }
        print(TemplateClient.update_company_template(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取合同模板控件维护链接
def get_edit_company_template_url_demo():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板编号'
            }
        }
        print(TemplateClient.get_edit_company_template_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除合同模板文件
def del_company_template_file_demo():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板编号',
                'fileId': '文件编号'
            }
        }
        print(TemplateClient.del_company_template_file(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取模板预览链接
def get_company_template_preview_url_demo():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板编号'
            }
        }
        print(TemplateClient.get_company_template_preview_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 模板列表
def query_company_template_list_demo():
    try:
        data = {
            'queryInfo': {
                'currentPageNo': '1',
                'pageSize': '2',
                'keyword': '关键字'
            }
        }
        print(TemplateClient.query_company_template_list(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 模板文件下载
def download_company_template_file_demo():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板编号'
            }

        }
        res = TemplateClient.download_company_template_file(fdd_client, data)
        with open("D:/模板文件.zip", "wb") as f:
            f.write(res.content)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取模板详请
def get_template_detail_by_id_demo():
    try:
        data = {
            'templateId': '模板编号',
        }
        print(TemplateClient.get_template_detail_by_id(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 填充模板
def create_by_template_id_demo():
    try:
        data = {
            'templateId': '模板编号',
            'templateFiles': {
                'templateFileId': '模板文件编号',
                'formFields': {
                },
                'documentFileName': '文件名称'
            }
        }
        print(TemplateClient.create_by_template_id(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 模板初始化
def template_init_demo():
    try:
        data = {
            'templateInfo': {
                'templateName': '模板名称',
                'templateRemark': '',
                'roles': [{
                    'roleName': '角色名称',
                    'roleType': '1',
                    'rolePermission': '3',
                    'signSort': '1',
                    'fillSort': '1'
                }]
            }
        }
        print(TemplateClient.template_init(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取模板编辑页面链接
def get_template_main_url_demo():
    try:
        data = {
            'templateInfo': {
                'templateId':'模板编号'
            }
        }
        print(TemplateClient.get_template_main_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 模板详请信息
def get_template_detail_demo():
    try:
        data = {
            'templateId': '模板编号'
        }
        print(TemplateClient.get_template_detail(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    fdd_client.set_token(token)
    #  如果是第三方应用就设置userToken
    # fdd_client.set_user_token(user_token)
    upload_company_template_file_demo()
    update_company_template_demo()
    get_edit_company_template_url_demo()
    del_company_template_file_demo()
    get_company_template_preview_url_demo()
    query_company_template_list_demo()
    download_company_template_file_demo()
    get_template_detail_by_id_demo()
    create_by_template_id_demo()
    template_init_demo()
    get_template_main_url_demo()
    get_template_detail_demo()
