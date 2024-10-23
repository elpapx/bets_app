class DataTransformer:
    @staticmethod
    def transform(data): #transformation data (cleaning, format, etc)
        for item in data:
            item['title'] = item['title'].strip().lower()

        return data