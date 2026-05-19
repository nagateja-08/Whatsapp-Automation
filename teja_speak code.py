import pywhatkit as kit
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()

contacts = {
    "Teja": "+919346033005",
    "Amma": "+916305763747",
    "Sai": "+919652195534",
    "Aishwayra": "+919434590921"
}

def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_contact(person):
    for name in contacts:
        if name.lower() == person.lower():
            return contacts[name]

    print("Contact not found")
    speak("Contact not found sir")
    return None


def send(phone_number, message, contact):
    kit.sendwhatmsg_instantly(
        phone_number,
        message,
        wait_time=20,
        tab_close=True,
        close_time=3
    )

    print(f"Message sent to {contact}")
    speak(f"Message sent to {contact}")


def send_message(cmd):

    words = cmd.split()
    contact = words[0]
    message = " ".join(words[1:])
    phone_number = get_contact(contact)

    if phone_number:
        send(phone_number, message, contact)


if __name__ == "__main__":
    send_message("Teja I am chatting with you")
