import webview


class Api:
    def submit_form(self, data):
        print(f"First Name: {data['first']}")
        print(f"Last Name: {data['last']}")
        print(f"Date of Birth: {data['dob']}")
        return "Received!"


if __name__ == "__main__":
    api = Api()
    window = webview.create_window("User Form", "user_form.html", js_api=api)
    webview.start()
