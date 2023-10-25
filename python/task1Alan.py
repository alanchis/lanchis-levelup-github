import urllib.request  
import json

def validate(datajson):
    thelist = []
    for key, value in datajson.items():
        if isinstance(value, dict):
            listreturned = validate(value)
            thelist= thelist + listreturned
        elif isinstance(value, list) and len(value)==0:
            thelist.append(key)
        elif value=="":
            thelist.append(key)
    return thelist
        
def main():
    urlData = "https://firebasestorage.googleapis.com/v0/b/probando0104.appspot.com/o/object.json?alt=media&token=13cbfde7-0ec0-4521-a98d-a8a342c7aa8d"
        # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read().decode("utf-8")
    # print out our customized results
        datajson = json.loads(data)
        result = validate(datajson)
        print(result)
    else:
        print("Received an error from server, cannot retrieve results " +
        str(webUrl.getcode()))

if __name__ == "__main__":
    main()
