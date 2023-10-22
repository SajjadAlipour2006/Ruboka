from .get_object_by_username import GetObjectByUsername
from .seen_chats import SeenChats
from .send_chat_activity import SendChatActivity


class Chats(GetObjectByUsername, SeenChats, SendChatActivity):
    pass
