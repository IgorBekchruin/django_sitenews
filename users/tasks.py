from celery import shared_task

from .email import send_email_for_verify


@shared_task
def send_activate_email_message_task(data):
    """
    Отправка письма подтверждения осуществляется через функцию: send_email_for_verify
    """
    return send_email_for_verify(data)

