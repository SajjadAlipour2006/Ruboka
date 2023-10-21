from .delete_messages import DeleteMessages
from .edit_message import EditMessage
from .forward_messages import ForwardMessages
from .send_message import SendMessage


class Messages(DeleteMessages, EditMessage, ForwardMessages, SendMessage):
    pass
