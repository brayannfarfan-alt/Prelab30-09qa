import requests



URL= 'https://jsonplaceholder.typicode.com'

class PostsService:

    def __init__(self):
        self.url = URL

    def obtener_post_por_id(self, post_id):
        url = f"{self.url}/posts/{post_id}"
        return requests.get(url)

    def crear_post(self, title, body, user_id):
        url = f"{self.url}/posts"
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        

        return requests.post(url, json=data)

    def eliminar_post(self, post_id):
        url = f"{self.url}/posts/{post_id}"
        return requests.delete(url)




