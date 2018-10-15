# ServiceOfAws = {
#   'service_id': int,
#   'name': string,
#   'descriptin': string,
#   'image_url': string,
#   'image_color': string
# }


class ServiceId:
    def __init__(self, service_id: int) -> None:
        self.value = service_id


class Name:
    def __init__(self, name: str) -> None:
        self.value = name


class Description:
    def __init__(self, description: str) -> None:
        self.value = description


class ImageUrl:
    def __init__(self, image_url: str) -> None:
        self.value = image_url


class ImageColor:
    def __init__(self, image_color: str) -> None:
        self.value = image_color


class ServiceOfAws:
    def __init__(self, service_id: ServiceId, name: Name,
                 description: Description, image_url: ImageUrl, image_color: ImageColor) -> None:
        self.service_id = service_id
        self.name = name
        self.description = description
        self.image_url = image_url
        self.image_color = image_color

    def to_dict(self) -> dict:
        pass

    def from_dict(self) -> 'ServiceOfAws':
        pass
