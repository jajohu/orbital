import datetime


def test_text_only_message():
    message = Message(text="test text", timestamp=datetime.datetime(2024, 1, 1, 0, 0, 0), id=42)
    assert message.type == MessageType.TEXT_ONLY


def test_report_message():
    ...