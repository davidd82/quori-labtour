from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

session = Session(profile_name="default")
polly = session.client("polly")

with open('./myfile.txt') as fname:
    all_lines = fname.readlines()


for line in all_lines:

    filename, text_to_say = line.split(':')

    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text=f"<speak> <prosody rate='90%'> {text_to_say}</prosody></speak>", TextType= 'ssml',OutputFormat="mp3",
                                            VoiceId="Justin", Engine="neural")
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    if "AudioStream" in response:
    # Note: Closing the stream is important because the service throttles on the
    # number of parallel connections. Here we are using contextlib.closing to
    # ensure the close method of the stream object will be called automatically
    # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
            output = f"./audio/{filename}.mp3"

            try:
            # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)