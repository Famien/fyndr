import httplib, urllib, base64, json,time

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
def getTags(imageUrl):
    subscription_key = 'a6cac55d66eb432d9dc39d9615337b45'

    # Replace or verify the region.
    #
    # You must use the same region in your REST API call as you used to obtain your subscription keys.
    # For example, if you obtained your subscription keys from the westus region, replace
    # "westcentralus" in the URI below with "westus".
    #
    # NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
    # a free trial subscription key, you should not need to change this region.
    uri_base = 'westcentralus.api.cognitive.microsoft.com'

    headers = {
        # Request headers.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = urllib.urlencode({
        # Request parameters. All of them are optional.
        'visualFeatures': 'Categories,Description,Color',
        'language': 'en',
    })

    # The URL of a JPEG image to analyze.
    body = "{'url':'"+imageUrl+"'}"

    try:
        # Execute the REST API call and get the response.
        conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        # print parsed
        tags = parsed['description']['tags']
        # print tags
        return tags
        print ("Response:")
        print (json.dumps(parsed, sort_keys=True, indent=2))
        conn.close()

    except Exception as e:
        print('Error:')
        print(e)

def getText(imageUrl):
    subscription_key = 'a6cac55d66eb432d9dc39d9615337b45'
    headers = {
        # Request headers.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = urllib.urlencode({
        # Request parameters. The language setting "unk" means automatically detect the language.
        'language': 'unk',
        'detectOrientation ': 'true',
    })

    # The URL of a JPEG image containing text.
    body = "{'url':'"+imageUrl+"'}"
    try:
        # Execute the REST API call and get the response.
        conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        text=[]
        # print len(parsed['regions'])
        for i in range(len(parsed['regions'])):
            # print parsed['regions'][i]['lines'][0]['words'][0]['text']
            text.append(parsed['regions'][i]['lines'][0]['words'][0]['text'])
            # print text
        # print ("Response:")
        # print (json.dumps(parsed, sort_keys=True, indent=2))
        conn.close()
        return text


    except Exception as e:
        print('Error:')
        print(e)

def isMens(imageUrl):
    text = getText(imageUrl)
    texts = []
    for i in text:
        texts.append(i.lower())
    print texts
    if 'men' in texts:
        return True
    else:
        return False

def isWomens(imageUrl):
    text = getText(imageUrl)
    texts = []
    for i in text:
        texts.append(i.lower())
    print texts
    if 'women' in texts:
        return True
    else:
        return False

def isVendingMachine(imageUrl):
    tags = getTags(imageUrl)
    text = getText(imageUrl)
    print tags
    print text
    if 'food' in tags and 'machine' in tags:
        return True
    elif 'pepsi' in text or 'aquafina' in text:
        return True
    else:
        return False

# print isWomens('http://www.safetysign.com/images/source/medium-images/F4916.png')
print isVendingMachine('https://upload.wikimedia.org/wikipedia/commons/1/1d/Push-bar-drinking-fountain.jpg')
