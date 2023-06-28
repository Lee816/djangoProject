import os
from PIL import Image  # 이미지처리 라이브러리
from django.db.models.fields.files import (
    ImageFieldFile,
    ImageField,
)  # 장고 기본 필드클래스를 상속받기 위해


class ThumbnailImageFieldFile(ImageFieldFile):  # 파일 시스템에 직접 파일을 쓰고 지우는 작업을 한다.
    def _add_thumb(
        s,
    ):  # 기존 이미지 파일명을 기준으로 썸네일 파일명을 만들어준다(썸네일 이미지의 경로나 URL을 만들때 사용). 123.jpg -> 123.thumb.jpg
        parts = s.split(".")
        parts.insert(-1, "thumb")
        if parts[-1].lower() not in [
            "jpeg",
            "jpg",
        ]:  # 확장자가 jpeg 또는 jpg 가 아니라면 jpg로 바꾸어준다.
            parts[-1] = "jpg"
        return ".".join(parts)

    # 이미지를 처리하는 필드는 파일의 경로(path)와 URL(url)속성을 제공해야한다.
    @property  # @property 데코레이터를 사용하면 메소드를 멤버변수처럼 사용할 수 있다.
    def thumb_path(self):  # 이 메소드는 원본 파일의 경로인 path 속성에 추가해 썸네일 결로인 thumb_path 속성을 만든다.
        return self._add_thumb(self.path)

    @property
    def thumb_url(self):  # 이 메소드는 원본 파일의 URL인 url 속성에 추가해, 썸네일의 URL인 thumb_url 속성을 만든다.
        return self._add_thumb(self.url)

    def save(self, name, content, save=True):  # 파일을 생성하고 저장하는 메소드
        super().save(
            name, content, save
        )  # 부모 ImageFieldFile 클래스의 save() 메소드를 호출해 원본 이미지를 저장

        img = Image.open(self.path)
        # 원본파일로부터 썸네일 이미지를 만든다. 썸네일 크기의 최대값을 필드 옵션으로 지정할 수 있다.
        size = (self.field.thumb_width, self.field.thumb_height)
        # Image.thumbnail() 함수는 썸네일 이미지를 만드는 함수이다. 이함수는 원본 이미지의 가로세로 비율을 유지한다.
        img.thumbnail(size)
        # RGB 모드인 동일한 크기의 백그라운드 이미지를 생성(255,255,255)는 흰색을 의미
        background = Image.new("RGB", size, (255, 255, 255))
        # 썸네일과 백그라운드 이미지를 합쳐서 썸네일 이미지를 만든다. 빈공간은 백그라운드 이미지에 의해서 하얀색이 된다.
        box = (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
        background.paste(img, box)
        # 합쳐진 최종 썸네일 이미지를 JPEG형식으로 파일 시스템의 thumb_path 경로에 저장한다.
        background.save(self.thumb_path, "JPEG")

    def delete(self, save=True):  # 원본 이미지와 썸네일 이미지도 같이 삭제한다.
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)


class ThumbnailImageField(ImageField):  # ImageField를 상속받아 모델정의에 사용하는 필드
    attr_class = ThumbnailImageFieldFile  # 새로운 FileField 클래스를 정의할 때는 그에 상응하는 File 처리 클래스를 attr_class 속성에 지정하는 것이 필수다.

    def __init__(
        self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs
    ):  # 모델의 필드 정의시 이미지의 최대크기로 옵션을 지정할수 있으며, 지정하지 않으면 128px를 사용한다. verbose_name으로 별핑을 줄수 있다.
        self.thumb_width, self.thumb_height = thumb_width, thumb_height

        super().__init__(
            verbose_name, **kwargs
        )  # 부모 클래스인 ImageField 클래스의 생성자를 호출해 관련속성을 초기화시킨다.
