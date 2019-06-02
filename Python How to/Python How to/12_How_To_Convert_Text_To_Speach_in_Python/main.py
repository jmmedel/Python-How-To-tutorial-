from win32com.client import constants, Dispatch

Msg = "Hi this is a test"

speaker = Dispatch("SAPI.SpVoice")  #Create SAPI SpVoice Object
speaker.Speak(Msg)                  #Process TTS
del speaker    