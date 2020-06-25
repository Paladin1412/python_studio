from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
import base64
import json


# 密钥参数
secret_id = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE"
secret_key = "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE"




def requset_tc(base64_data):
    try:

        cred = credential.Credential(
            "AKIDUO6pHXxSu6EOI5fstc6iMPK6qLXTK8j4", "EAsGk2yjDSQArVxGPEoAF4n2IH0Xpuki")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile)

        req = models.GeneralHandwritingOCRRequest()
        # print(str(base64_data))
        params = "{\"ImageBase64\":\"" + str(base64_data) + "\"}"
        req.from_json_string(params)

        resp = client.GeneralHandwritingOCR(req)
        print(resp.to_json_string())
        return json.loads(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)
        return str(err)


data = []

with open("imgs/final/1.jpg", "rb") as f:
    base64_data = base64.b64encode(f.read())
print(base64_data)
data.append(requset_tc(base64_data))

with open("tc_api_data/response.json", 'w') as fd:
    fd.write(json.dumps(data))
