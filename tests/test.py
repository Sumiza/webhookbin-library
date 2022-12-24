
import webhookbin
import time

print(webhookbin.makebin().text)

for i in range(3):
    webhookbin.post({"counter":i})
    print("Posting:",i)
    time.sleep(1)

while True:
    res = webhookbin.get()
    if res.json()["messid"] is None:
        break
    print("Reading:",res.json()['content'])
    time.sleep(1)

print(webhookbin.makebin().text)

print(webhookbin.post({"data": "here"}).text)

print(webhookbin.get().text)

print(webhookbin.makebin("both").text)

print(webhookbin.makebin("post").text)

print(webhookbin.makebin("get").text)

print(webhookbin.post({"data": "here"},headers={"Customheader": "Something"}).text)

headers = {"Customheader": "Something"}

print(webhookbin.post({"data": "here"},headers=headers,token="DBwIfrB_9BDycs0a4rm0YVRrgsPPpmS2_Vl11ElKpIM").text)

print(webhookbin.get(delete=False).text)

print(webhookbin.get(orderby="acending").text)

print(webhookbin.get(token="DBwIfrB_9BDycs0a4rm0YVRrgsPPpmS2_Vl11ElKpIM").text)

print(webhookbin.patch().text)
