import pywhatkit as kit
import pyttsx3
import speech_recognition as sr


contacts = {
    "Teja"     : "+919346033005",
    "Amma"     : "+916305763747",
    "Sai"      : "+919652195534",
    "Aishwayra": "+919434590921"
}
def get_contact(person):
    try:
        
        contact = None
        for name in contacts:
            if name in person:
                contact = name
                break

        phone_number = contacts[contact]
        print(f"Contact found - '{contact}' with number '{phone_number}'")
        return phone_number
    except ContactError
        print("Contact not found in the list.")
        speak("Contact not found, sir!")

def send_message(cmd):
    if "that" in cmd:
        contact = cmd.split()[0]
        phone_number = get_contact(contact)
        message = cmd.replace(contact, "").replace("that", "").strip()
        send(phone_number, message, contact)
    elif "to" in cmd:
        contact = cmd.split()[1]
        phone_number = get_contact(contact)
        speak("Message")
        message = listen()
        send(phone_number, message, contact)
    else:
        print("Could not send message")


def send(phone_number, message, contact):
    kit.sendwhatmsg_instantly(phone_number, message, wait_time=20, tab_close=True, close_time=3)
    print(f"Message sent successfully! to {contact}")
    speak(f"Message sent successfully to {contact}, sir!")

send_message("Teja that I am chatting")