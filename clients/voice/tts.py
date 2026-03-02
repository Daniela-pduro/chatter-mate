def speak(text: str) -> None:
    """Convert text to speech and play it through the speakers.

    TODO: implement using client.audio.speech.create(...)
      - model: "tts-1" or "tts-1-hd"
      - voice: e.g. "alloy", "echo", "nova"
      - input: text
      then play the returned audio bytes with sounddevice.
    """
    raise NotImplementedError
