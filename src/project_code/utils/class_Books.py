class Book:
    def __init__(self, title, description):
        if not isinstance(title, str):
            self.title = ""
        else:
            self.title = str(title)

        if not isinstance(description, str):
            self.description = ""
        else:
            self.description = str(description)

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def print_Book(self):
        try:
            title = self.title
        except:
            title = ""

        try:
            description = self.description
        except:
            description = ""

        result = "Título: {} \n Descripcion: {}".format(title, description)
        return result

    def serialize(self):
        return {"title": self.title, "descripcion": self.description}
