
import webhookbin
import time

print(webhookbin.makebin().text)
print(webhookbin.post({"data":"something"}).text)
print(webhookbin.get().text)
print(webhookbin.patch().text)


for i in range(5):
    webhookbin.post({"counter":i})
    print("Posting:",i)
    time.sleep(1)

while True:
    res = webhookbin.get()
    if res.json()["messid"] is None:
        break
    print("Reading:",res.json()['content'])
    time.sleep(1)
