from src.settings import settings


def test_settings() -> None:
    assert len(settings.model_dump()) == 1

    assert isinstance(settings.app_name, str)
    assert settings.app_name == "Python framework"
