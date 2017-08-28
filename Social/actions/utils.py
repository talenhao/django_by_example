from django.contrib.contenttypes.models import ContentType
from .models import Actions
from django.utils import timezone
import datetime


def create_action(user, verb, target):
    """
    一分钟内的连续操作将不被记录
    :param user:
    :param verb:
    :param target:
    :return:
    """
    now = timezone.now()
    # 生成早于1分钟前的提交
    last_minute = now - datetime.timedelta(seconds=60)
    # 从Actions表中过滤user
    similar_actions = Actions.objects.filter(user_id=user.id, verb=verb, timestamp__gte=last_minute)
    # 是否有操作对象?
    if target:
        target_content_type = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(
                target_content_type=target_content_type,
                target_id=target.id
        )
    # 是否已经提交过?
    if not similar_actions:
        action = Actions(user=user, verb=verb, target=target)
        action.save()
        return True
    return False
