class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        ctg = [c for c in self.categories if c.id == category_id]
        if ctg:
            ctg[0].name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        tpc = [t for t in self.topics if t.id == topic_id]
        if tpc:
            tpc[0].topic = new_topic
            tpc[0].storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        doc = [d for d in self.documents if d.id == document_id]
        if doc:
            doc[0].file_name = new_file_name

    def delete_category(self, category_id):
        ctg = [c for c in self.categories if c.id == category_id]
        if ctg:
            self.categories.remove(ctg[0])

    def delete_topic(self, topic_id):
        tpc = [t for t in self.topics if t.id == topic_id]
        if tpc:
            self.topics.remove(tpc[0])

    def delete_document(self, document_id):
        doc = [d for d in self.documents if d.id == document_id]
        if doc:
            self.documents.remove(doc[0])

    def get_document(self, document_id):
        doc = [d for d in self.documents if d.id == document_id]
        if doc:
            return doc[0].__repr__

    def __repr__(self):
        result = ''
        for doc in self.documents:
            result += f'{doc.__repr__}\n'
        return result

