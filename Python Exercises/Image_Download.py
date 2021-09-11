import urllib.request

url1 = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fblog.sembolfal.com%2Fkahve-falinda-aslan-gormek%2F&psig=AOvVaw3TjDXK56uTFlzbrkVAQJ7z&ust=1585580683031000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKCu4b_6v-gCFQAAAAAdAAAAABAD"
url2 = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.hurriyet.com.tr%2Fteknoloji%2Fmacbook-kullanicilarina-shadow-of-the-tomb-raider-mujdesi-41025692&psig=AOvVaw2FJXDnC8-6whKda_wibQBd&ust=1585580729638000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIiwp9P6v-gCFQAAAAAdAAAAABAO"

liste= [url1,url2]
say = 1
for url in liste:
    urllib.request.urlretrieve(url,"Resim" + str(say) +".jpg")
    say +=1