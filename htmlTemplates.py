import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64_string}"

user_avatar = get_base64_image("user_avatar.png")
bot_avatar = get_base64_image("bot_avatar.avif")


css = '''
<style>
/* GLOBAL PAGE STYLE */
body {
    background-color: #ffffff; 
    color: #007BFF;
}

.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
}
.chat-message.user {
    background-color: #ffffff; /* White bubble */
    border: 2px solid #007BFF; /* Blue border */
    color: #007BFF; /* Blue text */
}
.chat-message.bot {
    background-color: #007BFF; /* Blue bubble */
    color: #ffffff; /* White text */
}

.chat-message .avatar {
    width: 20%;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
    color: inherit; /* Inherit from parent bubble */
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="message">{{MSG}}</div>
</div>
'''