import sys
import json
import base64
# ............python2......python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode
class Baidu:

    API_KEY = 'q6eXfVjNhTVlQ0UuU8XApKsG'

    SECRET_KEY = '9S4EObGVHPY6LFFWGmFAeYu9AdwYceuZ'


    IMAGE_RECOGNIZE_URL = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"


    """  TOKEN start """
    TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'
    """
        获取token
    """
    def __init__(self):
        # 防止https证书校验不正确
        print('in')

    def plant_identification():
        # 获取access token
        token = self.fetch_token()

        # 拼接图像识别url
        url = self.IMAGE_RECOGNIZE_URL + "?access_token=" + token

        # 植物图1
        print("植物图1")
        self.print_result("./plant.jpg", url)

    def fetch_token(self):
        params = {'grant_type': 'client_credentials',
                  'client_id': self.API_KEY,
                  'client_secret': self.SECRET_KEY}
        post_data = urlencode(params)
        if (IS_PY3):
            post_data = post_data.encode('utf-8')
        req = Request(TOKEN_URL.TOKEN_URL, post_data)
        try:
            f = urlopen(req, timeout=5)
            result_str = f.read()
        except URLError as err:
            print(err)
        if (IS_PY3):
            result_str = result_str.decode()

        result = json.loads(result_str)

        if ('access_token' in result.keys() and 'scope' in result.keys()):
            if not 'brain_all_scope' in result['scope'].split(' '):
                print ('please ensure has check the  ability')
                exit()
            return result['access_token']
        else:
            print ('please overwrite the correct API_KEY and SECRET_KEY')
            exit()

    """
        读取文件
    """
    def read_file(image_path):
        f = None
        try:
            f = open(image_path, 'rb')
            return f.read()
        except:
            print('read image file fail')
            return None
        finally:
            if f:
                f.close()

    """
        调用远程服务
    """
    def request(url, data):
        req = Request(url, data.encode('utf-8'))
        has_error = False
        try:
            f = urlopen(req)
            result_str = f.read()
            if (IS_PY3):
                result_str = result_str.decode()
            return result_str
        except  URLError as err:
            print(err)

    """
        调用菜品识别接口并打印结果
    """
    def print_result(filename, url):
        # 获取图片
        file_content = self.read_file(filename)
        print(urlencode(
            {
                'image': 'a',
                'top_num': 1
            }))
        sys.exit()
        response = self.request(url, urlencode(
            {
                'image': base64.b64encode(file_content),
                'top_num': 1
            }))
        result_json = json.loads(response)

        # 打印图片结果
        print(result_json)