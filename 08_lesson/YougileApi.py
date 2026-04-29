import requests


class YougileApi:
    """Класс для работы с API Yougile (PageObject)"""

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

    # ========== МЕТОДЫ ДЛЯ РАБОТЫ С ПРОЕКТАМИ ==========

    def create_project(self, title, users=None):
        """Создать новый проект (POST /projects)"""
        project_data = {"title": title}
        if users:
            project_data["users"] = users

        resp = requests.post(
            self.base_url + '/projects',
            headers=self.headers,
            json=project_data
        )
        return resp.json()

    def get_project(self, project_id):
        """Получить проект по ID (GET /projects/{id})"""
        resp = requests.get(
            self.base_url + f'/projects/{project_id}',
            headers=self.headers
        )
        return resp.json()

    def update_project(
            self, project_id, new_title, users=None, is_deleted=None):
        """Обновить проект (PUT /projects/{id})"""
        update_data = {"title": new_title}
        if users is not None:
            update_data["users"] = users
        if is_deleted is not None:
            update_data["isDeleted"] = is_deleted

        resp = requests.put(
            self.base_url + f'/projects/{project_id}',
            headers=self.headers,
            json=update_data
        )
        return resp.json()

    def delete_project(self, project_id):
        """Мягкое удаление проекта (PUT с isDeleted=true)"""
        update_data = {
            "title": "to_delete",
            "isDeleted": True
        }
        resp = requests.put(
            self.base_url + f'/projects/{project_id}',
            headers=self.headers,
            json=update_data
        )
        return resp.json()

    def get_project_raw_response(self, project_id):
        """Получить сырой ответ (для проверки статус-кодов)"""
        resp = requests.get(
            self.base_url + f'/projects/{project_id}',
            headers=self.headers
        )
        return resp

    def update_project_raw_response(self, project_id, new_title):
        """Обновить проект и вернуть сырой ответ"""
        update_data = {"title": new_title}
        resp = requests.put(
            self.base_url + f'/projects/{project_id}',
            headers=self.headers,
            json=update_data
        )
        return resp

    def create_project_raw_response(self, title):
        """Создать проект и вернуть сырой ответ"""
        project_data = {"title": title}
        resp = requests.post(
            self.base_url + '/projects',
            headers=self.headers,
            json=project_data
        )
        return resp
