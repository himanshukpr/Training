from chat import Chat
from conversation import Conversation

chat1 = Chat(message="1 hello")
chat2 = Chat(message="2 hello")
chat3 = Chat(message="3 hello")


dm = Conversation()
dm.add(chat1)
dm.add(chat2)
dm.add(chat3)

chat1.show()